#!/bin/bash
# ============================================================
#  Python Music Workshop — Distribution Preparation Tool
#
#  Run this ONCE before the workshop to:
#   1. Download Python runtimes for Mac (arm64 + x86) and Windows
#   2. Create ready-to-distribute workshop zip files:
#        dist/workshop-mac.zip      (both Mac architectures)
#        dist/workshop-windows.zip
#
#  Requirements: curl, tar, unzip, zip (all standard on Mac)
#
#  Usage:
#    chmod +x tools/prepare-distribution.sh
#    ./tools/prepare-distribution.sh
# ============================================================

set -e
cd "$(dirname "$0")/.."
ROOT="$(pwd)"

echo "=================================================="
echo "   Python Music Workshop — Prepare Distribution"
echo "=================================================="
echo ""

# ── Configuration ───────────────────────────────────────────
RUNTIME_DIR="$ROOT/python-runtime"
DOWNLOADS_DIR="$RUNTIME_DIR/.downloads"
DIST_DIR="$ROOT/dist"

mkdir -p "$DOWNLOADS_DIR" "$DIST_DIR"

# ── Fetch latest python-build-standalone release info ────────
echo "Fetching latest python-build-standalone release..."
RELEASE_JSON=$(curl -sf "https://api.github.com/repos/astral-sh/python-build-standalone/releases/latest")
if [ -z "$RELEASE_JSON" ]; then
    echo "ERROR: Could not reach GitHub API. Check your internet connection."
    exit 1
fi

get_url() {
    echo "$RELEASE_JSON" \
        | grep -o '"browser_download_url": "[^"]*'"$1"'[^"]*"' \
        | head -1 \
        | grep -o 'https://[^"]*'
}

MAC_ARM64_URL=$(get_url "aarch64-apple-darwin-install_only.tar.gz")
MAC_X86_URL=$(get_url "x86_64-apple-darwin-install_only.tar.gz")
WIN_URL=$(get_url "x86_64-pc-windows-msvc-install_only.zip")

if [ -z "$MAC_ARM64_URL" ] || [ -z "$MAC_X86_URL" ] || [ -z "$WIN_URL" ]; then
    echo "ERROR: Could not find all required assets in the latest release."
    echo "URLs found:"
    echo "  mac-arm64 : $MAC_ARM64_URL"
    echo "  mac-x86   : $MAC_X86_URL"
    echo "  windows   : $WIN_URL"
    exit 1
fi

# Extract Python version from URL for display
PY_VERSION=$(echo "$MAC_ARM64_URL" | grep -o 'cpython-[0-9.]*' | head -1 | sed 's/cpython-//')
echo "  Python version : $PY_VERSION"
echo "  mac arm64      : $MAC_ARM64_URL"
echo "  mac x86_64     : $MAC_X86_URL"
echo "  windows        : $WIN_URL"
echo ""

# ── Helper: download and extract ────────────────────────────
download_and_extract() {
    local name="$1"
    local url="$2"
    local dest="$3"

    if [ -d "$dest" ]; then
        echo "  [$name] Already present — skipping download."
        return 0
    fi

    local filename
    filename=$(basename "$url")
    local archive="$DOWNLOADS_DIR/$filename"

    echo "  [$name] Downloading..."
    curl -L --progress-bar -o "$archive" "$url"

    echo "  [$name] Extracting..."
    local tmpdir="$DOWNLOADS_DIR/extract-$$"
    mkdir -p "$tmpdir"

    if [[ "$filename" == *.zip ]]; then
        unzip -q "$archive" -d "$tmpdir"
    else
        tar -xzf "$archive" -C "$tmpdir"
    fi

    # python-build-standalone install_only archives contain a single "python" directory
    local inner
    inner=$(ls "$tmpdir")
    mv "$tmpdir/$inner" "$dest"
    rm -rf "$tmpdir"

    echo "  [$name] Done → $dest"
}

# ── Download runtimes ────────────────────────────────────────
echo "── Downloading Python runtimes ──────────────────────"
download_and_extract "mac-arm64" "$MAC_ARM64_URL" "$RUNTIME_DIR/mac-arm64"
download_and_extract "mac-x86"   "$MAC_X86_URL"   "$RUNTIME_DIR/mac-x86"
download_and_extract "windows"   "$WIN_URL"        "$RUNTIME_DIR/windows"
echo ""

# ── Verify ──────────────────────────────────────────────────
echo "── Verifying runtimes ───────────────────────────────"
for runtime in mac-arm64 mac-x86; do
    BIN="$RUNTIME_DIR/$runtime/bin/python3"
    if [ ! -f "$BIN" ]; then
        echo "  ERROR: $BIN not found — extraction may have failed."
        exit 1
    fi
    echo "  $runtime OK"
done
WIN_BIN="$RUNTIME_DIR/windows/python.exe"
if [ ! -f "$WIN_BIN" ]; then
    echo "  ERROR: $WIN_BIN not found — extraction may have failed."
    exit 1
fi
echo "  windows OK"
echo ""

# ── Build list of files to include in the workshop zips ─────
# Excludes: .git, slides, tools, CLAUDE.md, python-runtime (added per-platform)
COMMON_INCLUDES=(
    "exercises"
    "data"
    "setup"
    "instructions"
    "README.md"
)

# ── Create Mac zip ───────────────────────────────────────────
echo "── Creating dist/workshop-mac.zip ──────────────────"
MAC_ZIP="$DIST_DIR/workshop-mac.zip"
rm -f "$MAC_ZIP"

# Zip common files first
zip -r "$MAC_ZIP" "${COMMON_INCLUDES[@]}" \
    --exclude "*.DS_Store" \
    --exclude "*__pycache__*" \
    --exclude "*.pyc" \
    -q

# Add both Mac runtimes
zip -r "$MAC_ZIP" \
    "python-runtime/mac-arm64" \
    "python-runtime/mac-x86" \
    --exclude "*.DS_Store" \
    -q

echo "  Created: $MAC_ZIP"
MAC_SIZE=$(du -sh "$MAC_ZIP" | awk '{print $1}')
echo "  Size   : $MAC_SIZE"
echo ""

# ── Create Windows zip ───────────────────────────────────────
echo "── Creating dist/workshop-windows.zip ──────────────"
WIN_ZIP="$DIST_DIR/workshop-windows.zip"
rm -f "$WIN_ZIP"

zip -r "$WIN_ZIP" "${COMMON_INCLUDES[@]}" \
    --exclude "*.DS_Store" \
    --exclude "*__pycache__*" \
    --exclude "*.pyc" \
    -q

zip -r "$WIN_ZIP" \
    "python-runtime/windows" \
    -q

echo "  Created: $WIN_ZIP"
WIN_SIZE=$(du -sh "$WIN_ZIP" | awk '{print $1}')
echo "  Size   : $WIN_SIZE"
echo ""

# ── Done ─────────────────────────────────────────────────────
echo "=================================================="
echo "  Distribution ready in: dist/"
echo ""
echo "  workshop-mac.zip      ($MAC_SIZE) — for Mac attendees"
echo "    Contains Python for both Apple Silicon and Intel Macs."
echo "    No installation required."
echo ""
echo "  workshop-windows.zip  ($WIN_SIZE) — for Windows attendees"
echo "    Contains Python for Windows x86-64."
echo "    No installation required."
echo ""
echo "  NOTE: VS Code is NOT bundled. Attendees still need VS Code."
echo "  Download from: https://code.visualstudio.com/"
echo ""
echo "  IMPORTANT (Mac): After copying workshop-mac.zip to USB sticks or"
echo "  sharing via Google Drive / Dropbox, recipients may see a macOS"
echo "  security warning the first time they run setup.command."
echo "  Instruct them to: right-click setup.command → Open → Open."
echo "  The bundled Python quarantine is cleared automatically by setup.command."
echo "=================================================="
