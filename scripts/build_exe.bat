@echo off
echo AI-noye Job Crawler - Windows Executable Builder
echo ==================================================

REM Check if Python is available (try multiple commands)
python --version >nul 2>&1
if errorlevel 1 (
    python3 --version >nul 2>&1
    if errorlevel 1 (
        py --version >nul 2>&1
        if errorlevel 1 (
            echo  Python not found! Please install Python first.
            echo    Tried: python, python3, py commands
            pause
            exit /b 1
        ) else (
            echo  Python found via 'py' command
        )
    ) else (
        echo Python found via 'python3' command
    )
) else (
    echo Python found via 'python' command
)

echo Python found

REM Check if uv is available
uv --version >nul 2>&1
if errorlevel 1 (
    echo UV package manager not found! Installing UV...
    echo    Installing UV via PowerShell...
    powershell -Command "irm https://astral.sh/uv/install.sh | iex"
    if errorlevel 1 (
        echo  Failed to install UV. Please install manually:
        echo    Visit: https://github.com/astral-sh/uv
        echo    Or use: pip install uv
        pause
        exit /b 1
    )
    echo UV installed successfully
) else (
    echo UV package manager found
)

REM Change to project root directory
cd /d "%~dp0.."

REM Install dependencies
echo Installing dependencies...
uv sync
if errorlevel 1 (
    echo  Failed to install dependencies
    pause
    exit /b 1
)

echo Dependencies installed

REM Run the build script
echo Building executable...
uv run python scripts/build_exe.py

echo.
echo  Build process completed!
echo  Check the 'release' folder for your executable
pause