#!/bin/bash
# ============================================================
#  Python Music Workshop — Data Explorer (Mac)
#  Double-click this file in Finder to open the explorer.
#
#  If macOS blocks it: right-click → Open → Open
# ============================================================

cd "$(dirname "$0")/.." || exit 1

clear
echo "=================================================="
echo "   Python Music Workshop — Data Explorer"
echo "=================================================="
echo ""

ARCH=$(uname -m)
if [ "$ARCH" = "arm64" ]; then
    PYTHON_CMD="python-runtime/mac-arm64/bin/python3"
else
    PYTHON_CMD="python-runtime/mac-x86/bin/python3"
fi

if [ ! -f "$PYTHON_CMD" ]; then
    echo "  Python runtime not found."
    echo "  Please run setup/setup.command first."
    echo ""
    echo "Press Enter to close..."
    read -r
    exit 1
fi

xattr -rd com.apple.quarantine "$(dirname "$(dirname "$PYTHON_CMD")")" 2>/dev/null || true

echo "  The music library is opening in your browser."
echo ""
echo "  Browse songs, search by artist or genre, and see"
echo "  the Python code to access any song directly."
echo ""
echo "  Press Enter here (or close this window) when you're done."
echo "=================================================="
echo ""

"$PYTHON_CMD" data/explorer.py

echo ""
echo "Explorer stopped. Press Enter to close this window..."
read -r
