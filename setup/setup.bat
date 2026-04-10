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
set PYTHON_CMD=python-runtime\windows\python.exe
set PYTHON_OK=0

set ERR_PYTHON_MISSING=0
set ERR_SMOKE=0

:: ── 1. Python ──────────────────────────────────────────────
echo Checking Python...

if not exist "%PYTHON_CMD%" (
    echo   [FAIL] Bundled Python not found.
    echo          Expected: python-runtime\windows\python.exe
    echo          Make sure you unzipped the full workshop folder.
    set /a FAIL+=1
    set ERR_PYTHON_MISSING=1
    goto python_done
)

%PYTHON_CMD% --version > "%TEMP%\pyver.tmp" 2>&1
set /p PY_VERSION=<"%TEMP%\pyver.tmp"
del "%TEMP%\pyver.tmp" >nul 2>&1
echo   [ OK ] %PY_VERSION% (bundled)
set /a PASS+=1
set PYTHON_OK=1

:python_done

:: ── 2. Smoke test ──────────────────────────────────────────
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
    goto end
)

echo   %PASS% check(s) passed.  %FAIL% issue(s) need fixing:
echo ==================================================
echo.

set ISSUE_NUM=0

if %ERR_PYTHON_MISSING% == 1 (
    set /a ISSUE_NUM+=1
    echo   ISSUE %ISSUE_NUM%: Bundled Python runtime is missing.
    echo   FIX %ISSUE_NUM%:   Right-click the downloaded .zip and choose "Extract All",
    echo              then run setup.bat from inside the extracted folder.
    echo              Do not run setup.bat from inside the zip file itself.
    echo.
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
