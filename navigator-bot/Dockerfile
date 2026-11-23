# Navigator bot image: the bot code only. The knowledge base is NOT in the image: at start, and then
# every KB_SYNC_MINUTES, the bot pulls the guides from GitHub (KB_REPO) into data/ and rebuilds its index,
# so knowledge-base updates go live without rebuilding or redeploying.
#   docker build -t navigator-bot navigator-bot
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# git fetches the guides (a shallow, sparse clone: no sources/ archives)
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /srv/navigator-bot
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN sed -i 's/\r$//' docker-entrypoint.sh && chmod +x docker-entrypoint.sh \
    && useradd --system --uid 10001 --home-dir /srv/navigator-bot app \
    && mkdir -p data && chown app:app data

# data/ holds the guides' copy, the index and the chat memory (state.sqlite). A volume here keeps
# memory and duplicate checks across restarts; without one the bot still works and re-fetches the guides.
VOLUME ["/srv/navigator-bot/data"]

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=60s --retries=3 \
    CMD python -c "import os,urllib.request; urllib.request.urlopen('http://127.0.0.1:%s/health' % (os.getenv('PORT') or 8000), timeout=4)"

ENTRYPOINT ["./docker-entrypoint.sh"]
