@echo off
rem Double-click to start the bot and its tunnel. Add -Rebuild after the .ps1 to rebuild the web page first.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0start.ps1" %*
pause
