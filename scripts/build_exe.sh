#!/bin/bash

echo "🏗️  AI-noye Job Crawler - Executable Builder"
echo "=============================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ Python not found! Please install Python first."
        exit 1
    fi
    PYTHON_CMD="python"
else
    PYTHON_CMD="python3"
fi

echo "✅ Python found: $($PYTHON_CMD --version)"

# Check if uv is available
if ! command -v uv &> /dev/null; then
    echo "❌ UV package manager not found! Please install UV first."
    echo "    Visit: https://github.com/astral-sh/uv"
    exit 1
fi

echo "✅ UV package manager found: $(uv --version)"

# Change to project root directory
cd "$(dirname "$0")/.."

# Install dependencies
echo "📦 Installing dependencies..."
if ! uv sync; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✅ Dependencies installed"

# Run the build script
echo "🔨 Building executable..."
uv run python scripts/build_exe.py

echo
echo "🎉 Build process completed!"
echo "📂 Check the 'release' folder for your executable"