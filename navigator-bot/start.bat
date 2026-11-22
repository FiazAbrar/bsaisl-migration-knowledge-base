@echo off
rem Double-click to start the bot and its tunnel. Add -Reindex after the .ps1 to rebuild the index first.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0start.ps1" %*
pause
