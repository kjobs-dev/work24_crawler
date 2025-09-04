#!/usr/bin/env python3
"""Build script for creating Windows GUI executable."""

import subprocess
import sys
import shutil
from pathlib import Path
import platform

def main():
    """Main build function for GUI version."""
    project_root = Path(__file__).parent.parent.absolute()  # Go up one level from scripts/
    
    print("🖥️  AI-noye Job Crawler GUI - Windows Executable Builder")
    print("=" * 60)
    
    # Check if we have the required files
    logo_path = project_root / "assets" / "ai-noye-logo.png"
    if not logo_path.exists():
        print("❌ Logo file 'assets/ai-noye-logo.png' not found!")
        sys.exit(1)
    
    spec_path = project_root / "scripts" / "build_gui.spec"
    if not spec_path.exists():
        print("❌ Spec file 'scripts/build_gui.spec' not found!")
        sys.exit(1)
    
    gui_main = project_root / "src" / "gui_main.py"
    if not gui_main.exists():
        print("❌ GUI main script 'src/gui_main.py' not found!")
        sys.exit(1)
    
    print("✅ All required files found")
    print(f"📂 Project root: {project_root}")
    print(f"🎨 Using logo: {logo_path.name}")
    print(f"🖥️  Platform: {platform.system()}")
    
    # Clean previous builds
    build_dir = project_root / "build"
    dist_dir = project_root / "dist"
    
    if build_dir.exists():
        print("🧹 Cleaning previous build directory...")
        shutil.rmtree(build_dir)
    
    if dist_dir.exists():
        print("🧹 Cleaning previous dist directory...")
        shutil.rmtree(dist_dir)
    
    print("\n🔨 Starting PyInstaller build for GUI...")
    print("-" * 40)
    
    try:
        # Run PyInstaller with the GUI spec file
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--clean",
            "--noconfirm", 
            str(spec_path)
        ]
        
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=project_root, check=True, capture_output=True, text=True)
        
        print("✅ GUI build successful!")
        
        # Check if the executable file was created (with or without .exe extension)
        exe_name = "AI-noye_Job_Crawler_GUI.exe" if platform.system() == "Windows" else "AI-noye_Job_Crawler_GUI"
        exe_path = dist_dir / exe_name
        if exe_path.exists():
            file_size = exe_path.stat().st_size / (1024 * 1024)  # Size in MB
            print(f"🎉 GUI Executable created: {exe_path}")
            print(f"📊 File size: {file_size:.1f} MB")
            
            # Create a release directory with additional files
            release_dir = project_root / "release_gui"
            if release_dir.exists():
                shutil.rmtree(release_dir)
            release_dir.mkdir()
            
            # Copy executable file
            release_exe_name = "AI-noye_Job_Crawler_GUI.exe" if platform.system() == "Windows" else "AI-noye_Job_Crawler_GUI"
            shutil.copy2(exe_path, release_dir / release_exe_name)
            
            # Copy logo
            shutil.copy2(logo_path, release_dir / "ai-noye-logo.png")
            
            # Create README for GUI users
            readme_content = """# AI-noye Job Crawler GUI Version

## 🚀 How to Use

1. **Run the Application**: Double-click `AI-noye_Job_Crawler_GUI.exe`
2. **Fill the Form**: 
   - Select site (currently Work24 only)
   - Enter login credentials
   - Set search keywords (optional)
   - Choose number of jobs to collect
   - Select output directory
3. **Start Crawling**: Click "🚀 크롤링 시작" button
4. **Monitor Progress**: Watch the log window for real-time updates

## 🖥️ GUI Features

- **User-Friendly Interface**: Simple, clean design
- **Real-time Logging**: See progress as it happens
- **Form Validation**: Prevents common input errors
- **Directory Browser**: Easy output folder selection
- **Progress Updates**: Know exactly what's happening

## 📋 Requirements

- **Internet Connection**: Required for job site access
- **Chrome Browser**: Must be installed (any version)
- **Windows 10/11**: Recommended operating system

## 📁 Output

- Excel files will be saved to your chosen directory
- Files are named: `채용공고_{timestamp}.xlsx`
- Batch saving prevents data loss (saves every 10 jobs)
- Automatic duplicate detection

## 🔧 Features

- **Simple GUI**: No command line needed
- **Stealth Browsing**: Avoids bot detection
- **Human-like Behavior**: Random delays and mouse movements  
- **Safe Batch Saving**: Data saved every 10 jobs
- **Duplicate Detection**: Skips already collected jobs
- **Cross-site Support**: LinkedIn, Indeed, Work24 (Work24 active)

## 📞 Support

For issues or questions, contact AI-noye support team.

---
Built with ❤️ by AI-noye Team
"""
            
            with open(release_dir / "README.txt", "w", encoding="utf-8") as f:
                f.write(readme_content)
            
            print(f"📦 GUI Release package created: {release_dir}")
            print("\n🎯 GUI Version Ready for distribution!")
            print("📝 Note: This is the GUI version - no command line needed!")
            
        else:
            print("❌ GUI executable file not found after build!")
            sys.exit(1)
            
    except subprocess.CalledProcessError as e:
        print(f"❌ GUI build failed: {e}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()