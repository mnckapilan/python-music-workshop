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

# Find Python
PYTHON_CMD=""
for cmd in python3 python python3.11 python3.10 python3.9 python3.8; do
    if command -v "$cmd" &>/dev/null; then
        PYTHON_CMD="$cmd"
        break
    fi
done

if [ -z "$PYTHON_CMD" ]; then
    echo "  Python not found. Please run setup/setup.command first."
    echo ""
    echo "Press Enter to close..."
    read -r
    exit 1
fi

echo "  The music library is opening in your browser."
echo ""
echo "  Browse songs, search by artist or genre, and see"
echo "  the Python code to access any song directly."
echo ""
echo "  Press Enter here (or close this window) when you're done."
echo "=================================================="
echo ""

$PYTHON_CMD data/explorer.py

echo ""
echo "Explorer stopped. Press Enter to close this window..."
read -r
