# Starts the Navigator bot and its ngrok tunnel on this PC.
#   .\start.ps1             start (installs packages and builds the web page the first time)
#   .\start.ps1 -Rebuild    rebuild the web page first (after changing web/)
param([switch]$Rebuild)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Test-Path .env)) { throw "No .env: copy .env.example to .env and fill it in." }
$envVars = @{}
Get-Content .env | Where-Object { $_ -match '^\s*([A-Z_]+)\s*=\s*(.*)$' } | ForEach-Object { $envVars[$Matches[1]] = $Matches[2].Trim() }
$domain = $envVars["PUBLIC_DOMAIN"]
if (-not $domain) { throw "PUBLIC_DOMAIN is empty in .env" }

$nodeVersion = (node --version) -replace '^v', ''
if ([int]($nodeVersion.Split('.')[0]) -lt 26) { throw "Node $nodeVersion is too old: install Node 26 (winget install OpenJS.NodeJS.LTS)" }

if (-not (Test-Path node_modules)) {
    Write-Host "Installing packages..."
    npm ci --ignore-scripts --no-audit --no-fund
}
if ($Rebuild -or -not (Test-Path web\dist\index.html)) {
    Write-Host "Building the web page..."
    npm run build:web
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
Write-Host "WhatsApp webhook: https://$domain/webhook  (ngrok runs in a minimized window)"
if ($envVars["TELEGRAM_BOT_TOKEN"]) {
    Write-Host "Telegram: https://$domain/telegram  (the bot registers this webhook with Telegram as it starts)"
}
if ($envVars["WEB_CHAT"] -notin @("off", "false", "0", "no")) {
    Write-Host "Web chat: http://localhost:8000/  (this PC)   https://$domain/  (anyone, through ngrok)"
}
Write-Host "Starting the bot. Press Ctrl+C to stop."
node --env-file=.env src/main.ts
