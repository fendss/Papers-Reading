@echo off
title Paper Website Updater
color 0A
echo.
echo =================================
echo    Paper Website Auto Updater   
echo =================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found
    echo Please install Python 3.6 or higher
    pause
    exit /b 1
)

REM 运行Python脚本
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