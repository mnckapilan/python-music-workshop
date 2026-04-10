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

# ── 1. Python ───────────────────────────────────────────────
echo "Checking Python..."

ARCH=$(uname -m)
if [ "$ARCH" = "arm64" ]; then
    PYTHON_CMD="python-runtime/mac-arm64/bin/python3"
else
    PYTHON_CMD="python-runtime/mac-x86/bin/python3"
fi

if [ ! -f "$PYTHON_CMD" ]; then
    echo "  [FAIL] Bundled Python not found."
    echo "         Expected: $PYTHON_CMD"
    echo "         Make sure you unzipped the full workshop folder."
    ISSUES+=("Bundled Python runtime is missing.")
    FIXES+=("Make sure the full workshop folder was unzipped. Do not run setup.command from inside the zip file.")
    ((FAIL++)) || true
else
    # Clear macOS quarantine (set automatically when unzipping a downloaded archive)
    xattr -rd com.apple.quarantine "$(dirname "$(dirname "$PYTHON_CMD")")" 2>/dev/null || true

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
