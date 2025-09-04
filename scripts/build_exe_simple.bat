@echo off
echo 🏗️  AI-noye Job Crawler - Simple Windows Builder
echo ===============================================

REM Check if Python is available
py --version >nul 2>&1
if errorlevel 1 (
    python --version >nul 2>&1
    if errorlevel 1 (
        echo ❌ Python not found! Please install Python from python.org
        pause
        exit /b 1
    )
    set PYTHON_CMD=python
) else (
    set PYTHON_CMD=py
)

echo ✅ Python found

REM Change to project root
cd /d "%~dp0.."

REM Install PyInstaller if not available
%PYTHON_CMD% -m pip install pyinstaller --quiet

REM Install project dependencies
echo 📦 Installing dependencies...
%PYTHON_CMD% -m pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo ❌ Failed to install from requirements.txt, trying pyproject.toml...
    %PYTHON_CMD% -m pip install . --quiet
)

REM Build executable
echo 🔨 Building executable...
%PYTHON_CMD% scripts/build_exe.py

echo.
echo 🎉 Build process completed!
echo 📂 Check the 'release' folder for your executable
pause