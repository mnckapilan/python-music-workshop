#!/bin/bash
# ============================================================
#  Python Music Workshop — Mac Setup
#  Double-click this file in Finder to run it.
#
#  If macOS blocks it: right-click the file → Open → Open
# ============================================================

cd "$(dirname "$0")/.." || exit 1

clear
echo "=================================================="
echo "   Python Music Workshop — Setup Check  (Mac)"
echo "=================================================="
echo ""

PASS=0
FAIL=0
ISSUES=()
FIXES=()
PYTHON_OK=false

# ── Detect architecture ──────────────────────────────────────
ARCH=$(uname -m)
if [ "$ARCH" = "arm64" ]; then
    RUNTIME_DIR="python-runtime/mac-arm64"
    PBS_PATTERN="aarch64-apple-darwin-install_only.tar.gz"
else
    RUNTIME_DIR="python-runtime/mac-x86"
    PBS_PATTERN="x86_64-apple-darwin-install_only.tar.gz"
fi
PYTHON_CMD="$RUNTIME_DIR/bin/python3"

# ── 1. Python runtime ────────────────────────────────────────
echo "Checking Python..."

if [ ! -f "$PYTHON_CMD" ]; then
    echo "  Runtime not found — downloading now (~35 MB)..."
    echo ""

    if ! curl -sf --connect-timeout 5 "https://github.com" > /dev/null 2>&1; then
        echo "  [FAIL] No internet connection."
        ISSUES+=("Python runtime is missing and there is no internet connection.")
        FIXES+=("Ask a volunteer for a USB stick with the complete workshop folder.")
        ((FAIL++)) || true
    else
        API=$(curl -sf "https://api.github.com/repos/astral-sh/python-build-standalone/releases/latest")
        URL=$(echo "$API" \
            | grep -o '"browser_download_url": "[^"]*'"$PBS_PATTERN"'[^"]*"' \
            | head -1 \
            | grep -o 'https://[^"]*')

        if [ -z "$URL" ]; then
            echo "  [FAIL] Could not find Python download URL."
            ISSUES+=("Python runtime download failed.")
            FIXES+=("Ask a volunteer for assistance.")
            ((FAIL++)) || true
        else
            TMP_ARCHIVE=$(mktemp /tmp/python-runtime-XXXXX.tar.gz)
            TMP_DIR=$(mktemp -d /tmp/python-extract-XXXXX)

            curl -L --progress-bar -o "$TMP_ARCHIVE" "$URL"
            tar -xzf "$TMP_ARCHIVE" -C "$TMP_DIR"

            INNER=$(ls "$TMP_DIR" | head -1)
            mkdir -p "$(dirname "$RUNTIME_DIR")"
            mv "$TMP_DIR/$INNER" "$RUNTIME_DIR"

            rm -f "$TMP_ARCHIVE"
            rm -rf "$TMP_DIR"
            echo ""
        fi
    fi
fi

if [ -f "$PYTHON_CMD" ]; then
    xattr -rd com.apple.quarantine "$RUNTIME_DIR" 2>/dev/null || true
    PY_VERSION=$("$PYTHON_CMD" --version 2>&1 | awk '{print $2}')
    echo "  [ OK ] Python $PY_VERSION (bundled)"
    ((PASS++)) || true
    PYTHON_OK=true
fi

# ── 2. Smoke test ───────────────────────────────────────────
if [ "$PYTHON_OK" = true ]; then
    echo "Running smoke test..."
    SMOKE_OUTPUT=$("$PYTHON_CMD" exercises/music_data.py 2>&1)
    SMOKE_EXIT=$?

    if [ "$SMOKE_EXIT" -eq 0 ]; then
        FIRST_LINE=$(echo "$SMOKE_OUTPUT" | head -1)
        echo "  [ OK ] $FIRST_LINE"
        ((PASS++)) || true
    else
        echo "  [FAIL] Music data failed to load"
        echo "         Error: $SMOKE_OUTPUT"
        ISSUES+=("The music data file failed to load.")
        FIXES+=("The workshop folder may still be quarantined by macOS. Ask a volunteer to run: xattr -rd com.apple.quarantine /path/to/python-music-workshop")
        ((FAIL++)) || true
    fi
fi

# ── Result ──────────────────────────────────────────────────
echo ""
echo "=================================================="

if [ "$FAIL" -eq 0 ]; then
    echo "  All $PASS checks passed."
    echo "=================================================="
    echo ""
    echo "  ✅  ALL DONE — YOU'RE GOOD TO GO!"
    echo ""

    # Ensure the root python3 wrapper is executable
    chmod +x python3 2>/dev/null || true

    # Write VS Code settings if VS Code is installed
    if command -v code &>/dev/null || [ -d "/Applications/Visual Studio Code.app" ]; then
        RUNTIME_SUBDIR=$(basename "$RUNTIME_DIR")
        "$PYTHON_CMD" -c "
import json, os
subdir = '$RUNTIME_SUBDIR'
settings = {
    'python.defaultInterpreterPath': 'python-runtime/' + subdir + '/bin/python3',
    'terminal.integrated.env.osx': {
        'PATH': '\${workspaceFolder}/python-runtime/' + subdir + '/bin:\${env:PATH}'
    }
}
os.makedirs('.vscode', exist_ok=True)
with open('.vscode/settings.json', 'w') as f:
    json.dump(settings, f, indent=4)
    f.write('\n')
"
    fi

else
    echo "  $PASS check(s) passed.  $FAIL issue(s) need fixing:"
    echo "=================================================="
    echo ""

    for i in "${!ISSUES[@]}"; do
        NUM=$((i + 1))
        echo "  ISSUE $NUM: ${ISSUES[$i]}"
        echo "  FIX $NUM:   ${FIXES[$i]}"
        echo ""
    done

    echo "  Re-run this script after fixing the issue(s) above."
    echo "=================================================="
fi

echo ""
echo "Press Enter to close this window..."
read -r
