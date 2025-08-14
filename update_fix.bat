@echo off
chcp 65001 > nul
title Paper Updater
cd /d "%~dp0"

echo =================================
echo    Paper Website Updater
echo =================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found
    echo Please install Python 3.6 or higher
    pause
    exit /b 1
)

echo Starting update...
echo.
python update_papers.py

echo.
echo =================================
echo    Update completed!
echo =================================
echo.
echo Press any key to exit...
pause > nul