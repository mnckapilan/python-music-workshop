@echo off
:: ============================================================
::  Python Music Workshop — Data Explorer (Windows)
::  Double-click this file in Explorer to open the explorer.
:: ============================================================

cd /d "%~dp0.."

cls
echo ==================================================
echo    Python Music Workshop -- Data Explorer
echo ==================================================
echo.

set PYTHON_CMD=python-runtime\windows\python.exe

if not exist "%PYTHON_CMD%" (
    echo   Python runtime not found.
    echo   Please run setup\setup.bat first.
    echo.
    pause
    exit /b 1
)

echo   The music library is opening in your browser.
echo.
echo   Browse songs, search by artist or genre, and see
echo   the Python code to access any song directly.
echo.
echo   Press Enter here (or close this window) when you're done.
echo ==================================================
echo.

%PYTHON_CMD% data/explorer.py

echo.
echo Explorer stopped.
pause
