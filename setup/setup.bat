@echo off
:: ============================================================
::  Python Music Workshop — Windows Setup
::  Double-click this file in Explorer to run it.
:: ============================================================

cd /d "%~dp0.."

cls
echo ==================================================
echo    Python Music Workshop -- Setup Check  (Windows)
echo ==================================================
echo.

set PASS=0
set FAIL=0
set PYTHON_CMD=
set PYTHON_OK=0
set VSCODE_OK=0

set ERR_PYTHON_MISSING=0
set ERR_PYTHON_OLD=0
set ERR_VSCODE=0
set ERR_VSCODE_PATH=0
set ERR_SMOKE=0

:: ── 1. Python ──────────────────────────────────────────────
echo Checking Python...

:: Try python, then py (Windows launcher), then python3
python --version >nul 2>&1
if %errorlevel% == 0 ( set PYTHON_CMD=python & goto python_found )

py --version >nul 2>&1
if %errorlevel% == 0 ( set PYTHON_CMD=py & goto python_found )

python3 --version >nul 2>&1
if %errorlevel% == 0 ( set PYTHON_CMD=python3 & goto python_found )

:: Python not found
echo   [FAIL] Python -- not found
set /a FAIL+=1
set ERR_PYTHON_MISSING=1
goto python_done

:python_found
:: Use Python itself to get the version string and check >=3.8
for /f "tokens=*" %%v in ('%PYTHON_CMD% --version 2^>^&1') do set PY_VERSION=%%v

%PYTHON_CMD% -c "import sys; exit(0 if sys.version_info >= (3,8) else 1)" >nul 2>&1
if %errorlevel% == 0 (
    echo   [ OK ] %PY_VERSION%
    set /a PASS+=1
    set PYTHON_OK=1
) else (
    echo   [FAIL] %PY_VERSION% -- too old ^(need 3.8 or newer^)
    set /a FAIL+=1
    set ERR_PYTHON_OLD=1
)

:python_done

:: ── 2. VS Code ─────────────────────────────────────────────
echo Checking VS Code...

code --version >nul 2>&1
if %errorlevel% == 0 (
    for /f "tokens=1" %%v in ('code --version 2^>^&1') do (
        echo   [ OK ] VS Code %%v
        set /a PASS+=1
        set VSCODE_OK=1
        goto vscode_done
    )
)

:: code not in PATH — check common install locations
set VSCODE_EXE=
if exist "%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe" (
    set VSCODE_EXE=%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe
)
if exist "%ProgramFiles%\Microsoft VS Code\Code.exe" (
    set VSCODE_EXE=%ProgramFiles%\Microsoft VS Code\Code.exe
)
if exist "%ProgramFiles(x86)%\Microsoft VS Code\Code.exe" (
    set VSCODE_EXE=%ProgramFiles(x86)%\Microsoft VS Code\Code.exe
)

if not "%VSCODE_EXE%"=="" (
    echo   [WARN] VS Code is installed but the 'code' command is not in PATH
    set /a FAIL+=1
    set ERR_VSCODE_PATH=1
) else (
    echo   [FAIL] VS Code -- not found
    set /a FAIL+=1
    set ERR_VSCODE=1
)

:vscode_done

:: ── 3. Smoke test ──────────────────────────────────────────
if %PYTHON_OK% == 1 (
    echo Running smoke test...
    %PYTHON_CMD% exercises\music_data.py >nul 2>&1
    if %errorlevel% == 0 (
        for /f "tokens=*" %%l in ('%PYTHON_CMD% exercises\music_data.py 2^>^&1') do (
            echo   [ OK ] %%l
            goto smoke_ok
        )
        :smoke_ok
        set /a PASS+=1
    ) else (
        echo   [FAIL] Music data failed to load
        set /a FAIL+=1
        set ERR_SMOKE=1
    )
)

:: ── Result ─────────────────────────────────────────────────
echo.
echo ==================================================

if %FAIL% == 0 (
    echo   All %PASS% checks passed.
    echo ==================================================
    echo.
    echo   *** ALL DONE -- YOU'RE GOOD TO GO! ***
    echo.
    echo   VS Code is opening now. Start with:
    echo   exercises\exercise_00_setup.md
    echo.
    timeout /t 1 /nobreak >nul
    code .
    goto end
)

echo   %PASS% check(s) passed.  %FAIL% issue(s) need fixing:
echo ==================================================
echo.

set ISSUE_NUM=0

if %ERR_PYTHON_MISSING% == 1 (
    set /a ISSUE_NUM+=1
    echo   ISSUE %ISSUE_NUM%: Python is not installed.
    echo   FIX %ISSUE_NUM%:   Go to https://www.python.org/downloads/ and install Python 3.11.
    echo              IMPORTANT: on the first installer screen, tick
    echo              "Add python.exe to PATH" before clicking Install.
    echo.
)

if %ERR_PYTHON_OLD% == 1 (
    set /a ISSUE_NUM+=1
    echo   ISSUE %ISSUE_NUM%: The installed Python version is too old ^(need 3.8 or newer^).
    echo   FIX %ISSUE_NUM%:   Go to https://www.python.org/downloads/ and install Python 3.11.
    echo              IMPORTANT: tick "Add python.exe to PATH" on the first screen.
    echo.
)

if %ERR_VSCODE% == 1 (
    set /a ISSUE_NUM+=1
    echo   ISSUE %ISSUE_NUM%: VS Code is not installed.
    echo   FIX %ISSUE_NUM%:   Go to https://code.visualstudio.com/ and download VS Code.
    echo              During installation, tick:
    echo              "Add 'Open with Code' action to Windows Explorer"
    echo              "Add to PATH (requires shell restart)"
    echo.
)

if %ERR_VSCODE_PATH% == 1 (
    set /a ISSUE_NUM+=1
    echo   ISSUE %ISSUE_NUM%: VS Code is installed but the 'code' command is not in PATH.
    echo   FIX %ISSUE_NUM%:   Uninstall VS Code and reinstall it from https://code.visualstudio.com/
    echo              During installation, tick "Add to PATH (requires shell restart)".
    echo              Then restart the computer and re-run this script.
    echo.
    :: Still open VS Code the long way if we can
    if not "%VSCODE_EXE%"=="" (
        echo   (Opening VS Code now so you can work in the meantime)
        start "" "%VSCODE_EXE%" "%~dp0"
    )
)

if %ERR_SMOKE% == 1 (
    set /a ISSUE_NUM+=1
    echo   ISSUE %ISSUE_NUM%: The music data file failed to load.
    echo   FIX %ISSUE_NUM%:   Make sure the full workshop folder was unzipped before
    echo              running this script. Right-click the downloaded .zip and
    echo              choose "Extract All", then run setup.bat from inside
    echo              the extracted folder.
    echo.
)

echo   Re-run this script after fixing the issue(s) above.
echo ==================================================

:end
echo.
pause
