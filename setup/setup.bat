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

set ERR_PYTHON=0
set ERR_SMOKE=0

:: ── 1. Python runtime ──────────────────────────────────────
echo Checking Python...

if exist "%PYTHON_CMD%" goto python_ok

:: Runtime missing — try to download it
echo   Runtime not found -- downloading now (~35 MB)...
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0download-python-windows.ps1"

if %errorlevel% neq 0 (
    echo.
    echo   [FAIL] Could not download Python runtime.
    echo          Check your internet connection, or ask a volunteer
    echo          for a USB stick with the complete workshop folder.
    set /a FAIL+=1
    set ERR_PYTHON=1
    goto python_done
)

echo.

:python_ok
if not exist "%PYTHON_CMD%" (
    echo   [FAIL] Python runtime still missing after download attempt.
    set /a FAIL+=1
    set ERR_PYTHON=1
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

    :: Write VS Code settings if VS Code is present
    code --version >nul 2>&1
    if %errorlevel% == 0 (
        if not exist ".vscode" mkdir .vscode
        powershell -NoProfile -Command ^
            "$s = [ordered]@{ 'python.defaultInterpreterPath' = 'python-runtime/windows/python.exe'; 'terminal.integrated.env.windows' = @{ 'PATH' = '${workspaceFolder}/python-runtime/windows;${env:PATH}' } }; ^
            $s | ConvertTo-Json -Depth 3 | Set-Content '.vscode/settings.json' -Encoding UTF8" ^
            >nul 2>&1
    )

    goto end
)

echo   %PASS% check(s) passed.  %FAIL% issue(s) need fixing:
echo ==================================================
echo.

set ISSUE_NUM=0

if %ERR_PYTHON% == 1 (
    set /a ISSUE_NUM+=1
    echo   ISSUE %ISSUE_NUM%: Python runtime is missing.
    echo   FIX %ISSUE_NUM%:   Make sure the full workshop folder was unzipped, or
    echo              check your internet connection and re-run this script.
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
if defined CI goto done
pause
:done
