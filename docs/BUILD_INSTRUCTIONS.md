# 🏗️ AI-noye Job Crawler - Build Instructions

## Overview
This document explains how to build a standalone Windows executable (.exe) file for the AI-noye Job Crawler with the company logo as the icon.

## 📋 Prerequisites

### Required Software
- **Python 3.11+** installed and in PATH
- **UV Package Manager** ([Install UV](https://github.com/astral-sh/uv))
- **Google Chrome** browser installed
- **AI-noye Logo** file: `ai-noye-logo.png` in root directory

### Operating Systems Supported for Building
- ✅ **Windows 10/11** (builds .exe files)
- ✅ **Linux** (builds Linux executables)
- ✅ **macOS** (builds macOS executables)

## 🚀 Quick Build (Recommended)

### On Windows
```cmd
# Double-click the batch file or run in Command Prompt
build_exe.bat
```

### On Linux/Mac
```bash
# Make executable and run
chmod +x build_exe.sh
./build_exe.sh
```

## 🛠️ Manual Build Process

```bash
# 1. Install dependencies
uv sync

# 2. Run build script
uv run python build_exe.py
```

## 📂 Build Output

After successful build, you'll find:

```
release/
├── AI-noye_Job_Crawler.exe    # Windows executable (or no .exe on Linux/Mac)
├── ai-noye-logo.png           # Company logo
└── README.txt                 # User instructions
```

## 🎯 Build Configuration

### PyInstaller Settings (build_exe.spec)
- **Icon**: `ai-noye-logo.png` 
- **Console Mode**: Enabled for user interaction
- **Single File**: All dependencies bundled
- **Compression**: UPX enabled for smaller file size
- **Hidden Imports**: All crawler modules included

### Included Dependencies
- Selenium WebDriver
- Undetected ChromeDriver  
- Pandas & OpenPyXL (Excel support)
- Pydantic (data validation)
- All crawler modules and utilities

## 📊 Build Statistics

- **File Size**: ~52MB (standalone executable)
- **Build Time**: 2-5 minutes (depending on system)
- **Dependencies**: 80+ Python packages bundled
- **Platform**: Cross-platform build support

## 🚨 Troubleshooting

### Common Issues

**PyInstaller Not Found**
```bash
uv add --dev pyinstaller
```

**Missing Logo File**
- Ensure `ai-noye-logo.png` exists in root directory
- Check file permissions

**Build Fails on Import Errors**
- Update hidden imports in `build_exe.spec`
- Add missing modules to `hiddenimports` list

**Executable Too Large**
- Review `excludes` section in spec file
- Add unused packages to exclude list

### Build on Different Platforms

**For Windows .exe** (must build on Windows):
- Use Windows machine with Python + UV
- Run `build_exe.bat`
- Output: `AI-noye_Job_Crawler.exe`

**For Linux Binary** (build on Linux):
- Use Linux machine with Python + UV  
- Run `./build_exe.sh`
- Output: `AI-noye_Job_Crawler` (no extension)

**For macOS App** (build on Mac):
- Use Mac machine with Python + UV
- Run `./build_exe.sh` 
- Output: `AI-noye_Job_Crawler` (Mac binary)

## 🎉 Distribution

The `release/` folder is ready for distribution:
1. **Zip the release folder**
2. **Distribute to users**
3. **Users extract and double-click executable**
4. **No Python installation required on target machines**

## ⚙️ Customization

### Changing the Icon
Replace `ai-noye-logo.png` with your desired icon file (PNG format recommended).

### Modifying Build Settings
Edit `build_exe.spec` file:
- Change executable name
- Add/remove dependencies
- Modify compression settings
- Update hidden imports

### Adding Resources
Add files to the `datas` section in `build_exe.spec`:
```python
datas=[
    ('path/to/resource', 'destination/in/exe'),
    ('ai-noye-logo.png', '.'),
]
```

---

**Built with ❤️ for AI-noye Team**