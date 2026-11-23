"""Keep the knowledge base up to date straight from GitHub (used on servers).

With KB_REPO set, the bot keeps its own copy of only the guides it reads (each doc.md, facts.csv and
sources.csv, never the multi-GB sources/ archives) in data/kb-repo, using a shallow, sparse git clone.
Every KB_SYNC_MINUTES it fetches the branch again and rebuilds the index when the commit changed, so a
push to the knowledge base reaches the bot without a redeploy. With KB_REPO empty this does nothing and
the bot reads the repository it sits in (KB_DIR), as on a local PC.

Run once by hand:  python -m app.kb_sync
"""
import logging
import os
import shutil
import subprocess
import threading
import time
from pathlib import Path

from dotenv import load_dotenv

from . import kb_index

ROOT = Path(__file__).resolve().parent.parent
REPO_DIR = ROOT / "data" / "kb-repo"
# Any guide anywhere in the repository (each doc.md with its facts.csv and sources.csv), so a new
# folder needs no change here; never the source archives or the bot's own folder.
PATTERNS = ["doc.md", "facts.csv", "sources.csv", "!/navigator-bot/", "!sources/"]

_lock = threading.Lock()
# What the last sync did, for /health: when it ran, the commit it saw, and any problem.
status: dict = {"last_sync": None, "commit": None, "error": None, "index_refused": None}


def _settings() -> tuple[str, str, int, str]:
    load_dotenv(ROOT / ".env")
    repo = (os.getenv("KB_REPO") or "").strip()
    branch = (os.getenv("KB_BRANCH") or "").strip() or "main"
    minutes = int((os.getenv("KB_SYNC_MINUTES") or "").strip() or 15)
    token = (os.getenv("KB_GITHUB_TOKEN") or "").strip()  # only for a private repository
    return repo, branch, minutes, token


def _git(*args: str, token: str = "", cwd: Path | None = None) -> str:
    cmd = ["git"]
    if token:  # sent as a header, so the token never lands in .git/config or the logs
        cmd += ["-c", f"http.extraHeader=Authorization: Bearer {token}"]
    env = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}
    out = subprocess.run(cmd + list(args), cwd=cwd, env=env, capture_output=True, text=True, timeout=300)
    if out.returncode != 0:
        raise RuntimeError(f"git {args[0]} failed: {out.stderr.strip()[-500:]}")
    return out.stdout.strip()


def _head() -> str:
    return _git("rev-parse", "HEAD", cwd=REPO_DIR)


def sync(force_index: bool = False) -> bool:
    """Fetch the latest guides; rebuild the index if they changed. Returns True if it rebuilt."""
    repo, branch, _, token = _settings()
    if not repo:
        return False
    with _lock:
        if not (REPO_DIR / ".git").is_dir():
            shutil.rmtree(REPO_DIR, ignore_errors=True)
            REPO_DIR.parent.mkdir(parents=True, exist_ok=True)
            try:
                _git("clone", "--depth", "1", "--filter=blob:none", "--no-checkout", "--branch", branch,
                     repo, str(REPO_DIR), token=token)
                _git("sparse-checkout", "set", "--no-cone", *PATTERNS, cwd=REPO_DIR)
                _git("checkout", branch, cwd=REPO_DIR, token=token)
            except Exception:
                shutil.rmtree(REPO_DIR, ignore_errors=True)  # retry from scratch next time
                raise
            before = ""
        else:
            before = _head()
            _git("sparse-checkout", "set", "--no-cone", *PATTERNS, cwd=REPO_DIR)  # in case PATTERNS changed
            _git("fetch", "--depth", "1", "origin", branch, cwd=REPO_DIR, token=token)
            _git("reset", "--hard", "FETCH_HEAD", cwd=REPO_DIR, token=token)
        after = _head()
        status.update(last_sync=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), commit=after[:7], error=None)
        if after == before and not force_index and kb_index.DB_PATH.exists():
            return False
        try:
            counts = kb_index.build(REPO_DIR, extra_meta={"kb_commit": after})
        except kb_index.IndexCheckFailed as e:
            # A suspicious push (a guide gone, or most of one): keep answering from the last good index.
            status["index_refused"] = f"commit {after[:7]}: {e}"
            logging.error("Knowledge base at %s NOT loaded, keeping the last good index: %s", after[:7], e)
            return False
        status["index_refused"] = None
        logging.info("Knowledge base %s: index rebuilt at commit %s (%d sections)",
                     "updated" if before else "loaded", after[:7], sum(counts.values()))
        return True


def start_background_sync():
    """Sync once now (so the index exists before the bot answers), then keep syncing in the background."""
    repo, _, minutes, _ = _settings()
    if not repo:
        return
    try:
        sync(force_index=True)
    except Exception:
        # Keep serving: an index from an earlier run (on the data volume) still works, and the loop retries.
        logging.exception("Knowledge-base sync from GitHub failed at start")

    def loop():
        while True:
            time.sleep(max(minutes, 1) * 60)
            try:
                sync()
            except Exception as e:
                status["error"] = f"{type(e).__name__}: {str(e)[:200]}"
                logging.exception("Knowledge-base sync failed; the bot keeps using the last good index")

    threading.Thread(target=loop, name="kb-sync", daemon=True).start()
    logging.info("Knowledge base syncs from GitHub every %d minutes", minutes)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    if not _settings()[0]:
        raise SystemExit("KB_REPO is empty: nothing to sync (the bot reads the local repository).")
    sync(force_index=True)
    print(f"Index written to {kb_index.DB_PATH}")
