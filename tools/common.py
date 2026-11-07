"""Shared settings for the tools. Run every tool from inside your country folder, e.g.
  cd countries/malaysia && python3 ../../tools/build.py
"""
import datetime, glob, os, sys

BASE = os.getcwd()
if not glob.glob(os.path.join(BASE, "*.src.md")) and not os.path.isdir(os.path.join(BASE, "raw")):
    sys.exit("Run this from inside a country folder (countries/<country>/).")
RAW = os.path.join(BASE, "raw")
_t = datetime.date.today()
# A page dated before this (12 months ago) or undated counts as "possibly outdated".
CUTOFF = _t.replace(year=_t.year - 1).isoformat() if not (_t.month == 2 and _t.day == 29) else f"{_t.year - 1}-02-28"
