#!/bin/bash
# ============================================================
#  Python Music Workshop — Mac Setup
#  Double-click this file in Finder to run it.
#
#  If macOS blocks it: right-click the file → Open → Open
# ============================================================

# Always run from the project root (one level up from setup/)
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
PYTHON_CMD=""
VSCODE_OPEN_CMD=""

# ── 1. Python ───────────────────────────────────────────────
echo "Checking Python..."

for cmd in python3 python python3.11 python3.10 python3.9 python3.8; do
    if command -v "$cmd" &>/dev/null; then
        PYTHON_CMD="$cmd"
        break
    fi
done

if [ -z "$PYTHON_CMD" ]; then
    echo "  [FAIL] Python — not found"
    ISSUES+=("Python 3 is not installed.")
    FIXES+=("Go to https://www.python.org/downloads/ and install Python 3.11 (or newer). Use the macOS installer.")
    ((FAIL++)) || true
else
    PY_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')

    # Use Python itself to check version — avoids fragile string parsing
    if $PYTHON_CMD -c "import sys; exit(0 if sys.version_info >= (3,8) else 1)" 2>/dev/null; then
        echo "  [ OK ] Python $PY_VERSION"
        ((PASS++)) || true
        PYTHON_OK=true
    else
        echo "  [FAIL] Python $PY_VERSION — too old (need 3.8 or newer)"
        ISSUES+=("Python $PY_VERSION is installed but is too old. Need 3.8 or newer.")
        FIXES+=("Go to https://www.python.org/downloads/ and install Python 3.11 (or newer).")
        ((FAIL++)) || true
    fi
fi

# ── 2. VS Code ──────────────────────────────────────────────
echo "Checking VS Code..."

if command -v code &>/dev/null; then
    VSCODE_VER=$(code --version 2>/dev/null | head -1)
    echo "  [ OK ] VS Code $VSCODE_VER"
    ((PASS++)) || true
    VSCODE_OPEN_CMD="code ."
elif [ -d "/Applications/Visual Studio Code.app" ]; then
    echo "  [WARN] VS Code is installed but the 'code' terminal command is missing"
    ISSUES+=("VS Code is installed but its terminal command ('code') has not been set up.")
    FIXES+=("Open VS Code → press Cmd+Shift+P → type 'shell command' → click 'Shell Command: Install code command in PATH'. Then re-run this script.")
    ((FAIL++)) || true
    # We can still open VS Code — just can't use the CLI
    VSCODE_OPEN_CMD="open -a 'Visual Studio Code' ."
else
    echo "  [FAIL] VS Code — not found"
    ISSUES+=("VS Code is not installed.")
    FIXES+=("Go to https://code.visualstudio.com/ and download VS Code for Mac. After installing, open VS Code → press Cmd+Shift+P → type 'shell command' → click 'Shell Command: Install code command in PATH'. Then re-run this script.")
    ((FAIL++)) || true
fi

# ── 3. Smoke test ───────────────────────────────────────────
if [ "$PYTHON_OK" = true ]; then
    echo "Running smoke test..."
    SMOKE_OUTPUT=$($PYTHON_CMD exercises/music_data.py 2>&1)
    SMOKE_EXIT=$?

    if [ "$SMOKE_EXIT" -eq 0 ]; then
        FIRST_LINE=$(echo "$SMOKE_OUTPUT" | head -1)
        echo "  [ OK ] $FIRST_LINE"
        ((PASS++)) || true
    else
        echo "  [FAIL] Music data failed to load"
        echo "         Error: $SMOKE_OUTPUT"
        ISSUES+=("The music data file failed to load.")
        FIXES+=("The workshop folder may still be quarantined by macOS. Ask a volunteer to run: xattr -rd com.apple.quarantine /path/to/python-music-workshop-main")
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
    echo "  VS Code is opening now. Start with:"
    echo "  exercises/exercise_00_setup.md"
    echo ""
    sleep 1
    eval "$VSCODE_OPEN_CMD" 2>/dev/null
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

    if [ -n "$VSCODE_OPEN_CMD" ] && [ "$FAIL" -eq 1 ] && [[ "${ISSUES[0]}" == *"terminal command"* ]]; then
        echo "  (Opening VS Code anyway so you can fix the PATH issue from inside it)"
        sleep 1
        eval "$VSCODE_OPEN_CMD" 2>/dev/null
    fi

    echo "  Re-run this script after fixing the issue(s) above."
    echo "=================================================="
fi

echo ""
echo "Press Enter to close this window..."
read -r
