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

:: Find Python
set PYTHON_CMD=
python --version >nul 2>&1
if %errorlevel% == 0 ( set PYTHON_CMD=python & goto python_found )
py --version >nul 2>&1
if %errorlevel% == 0 ( set PYTHON_CMD=py & goto python_found )
python3 --version >nul 2>&1
if %errorlevel% == 0 ( set PYTHON_CMD=python3 & goto python_found )

echo   Python not found. Please run setup\setup.bat first.
echo.
pause
exit /b 1

:python_found
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
