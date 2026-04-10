@echo off
:: Convenience wrapper — runs the bundled Python runtime.
:: Usage from project root:
::   python3 exercises\exercise_01_variables_and_strings.py
if exist "%~dp0python-runtime\windows\python.exe" (
    "%~dp0python-runtime\windows\python.exe" %*
) else (
    echo Python runtime not found. Please run setup\setup.bat first.
    exit /b 1
)
