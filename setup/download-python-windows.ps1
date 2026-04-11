# download-python-windows.ps1
# Downloads the python-build-standalone Windows runtime and places it at
# python-runtime\windows\ relative to the workshop root.
# Called by setup.bat when the runtime is missing.

$ErrorActionPreference = 'Stop'

$workshopRoot = Split-Path $PSScriptRoot -Parent
$dest = Join-Path $workshopRoot 'python-runtime\windows'

try {
    $api = Invoke-RestMethod 'https://api.github.com/repos/astral-sh/python-build-standalone/releases/latest'
    $asset = $api.assets |
        Where-Object { $_.name -like '*x86_64-pc-windows-msvc-install_only.zip' } |
        Select-Object -First 1

    if (-not $asset) { throw 'Asset not found in release' }

    $url = $asset.browser_download_url
    $tmp = Join-Path $env:TEMP 'python-runtime-workshop.zip'
    $extract = Join-Path $env:TEMP 'python-extract-workshop'

    Write-Host '  Downloading...'
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    Invoke-WebRequest $url -OutFile $tmp -UseBasicParsing

    Write-Host '  Extracting...'
    if (Test-Path $extract) { Remove-Item $extract -Recurse -Force }
    Expand-Archive $tmp -DestinationPath $extract

    $inner = Get-ChildItem $extract | Select-Object -First 1 -ExpandProperty FullName

    $runtimeParent = Split-Path $dest -Parent
    if (-not (Test-Path $runtimeParent)) { New-Item -ItemType Directory -Path $runtimeParent | Out-Null }

    Move-Item $inner $dest

    Remove-Item $tmp
    Remove-Item $extract -Recurse
} catch {
    Write-Host "  Download failed: $_"
    exit 1
}
