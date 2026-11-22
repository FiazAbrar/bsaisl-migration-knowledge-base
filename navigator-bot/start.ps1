# Starts the Navigator bot and its ngrok tunnel.
#   .\start.ps1            start (builds the knowledge-base index first if it is missing)
#   .\start.ps1 -Reindex   rebuild the index from KB_DIR, then start
param([switch]$Reindex)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

# Settings from .env
$envVars = @{}
Get-Content .env | Where-Object { $_ -match '^\s*([A-Z_]+)\s*=\s*(.*)$' } | ForEach-Object { $envVars[$Matches[1]] = $Matches[2].Trim() }
$domain = $envVars["PUBLIC_DOMAIN"]
if (-not $domain) { throw "PUBLIC_DOMAIN is empty in .env" }

# Python environment (created on first run)
$py = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $py)) {
    Write-Host "Creating Python environment..."
    python -m venv .venv
    & $py -m pip install -q -r requirements.txt
}

# Knowledge-base index
if ($Reindex -or -not (Test-Path "data\kb.sqlite")) {
    Write-Host "Building knowledge-base index from KB_DIR..."
    & $py -m app.kb_index
}

# ngrok (winget puts it outside PATH until the terminal is reopened)
$ngrok = (Get-Command ngrok -ErrorAction SilentlyContinue).Source
if (-not $ngrok) {
    $ngrok = Get-ChildItem "$env:LOCALAPPDATA\Microsoft\WinGet\Packages" -Filter ngrok.exe -Recurse -ErrorAction SilentlyContinue |
        Select-Object -First 1 -ExpandProperty FullName
}
if (-not $ngrok) { throw "ngrok not found. Install it with: winget install ngrok.ngrok, then run: ngrok update" }

Get-Process ngrok -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Process -FilePath $ngrok -ArgumentList "http 8000 --url https://$domain" -WindowStyle Minimized
Write-Host "Tunnel: https://$domain/webhook  (ngrok runs in a minimized window)"

Write-Host "Starting bot. Press Ctrl+C to stop."
& $py run.py
