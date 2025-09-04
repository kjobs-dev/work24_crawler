#!/usr/bin/env python3
"""Build script for creating Windows executable."""

import subprocess
import sys
import shutil
from pathlib import Path
import platform

def main():
    """Main build function."""
    project_root = Path(__file__).parent.parent.absolute()  # Go up one level from scripts/
    
    print("🏗️  AI-noye Job Crawler - Windows Executable Builder")
    print("=" * 50)
    
    # Check if we have the required files
    logo_path = project_root / "assets" / "ai-noye-logo.png"
    if not logo_path.exists():
        print("❌ Logo file 'assets/ai-noye-logo.png' not found!")
        sys.exit(1)
    
    spec_path = project_root / "scripts" / "build_exe.spec"
    if not spec_path.exists():
        print("❌ Spec file 'scripts/build_exe.spec' not found!")
        sys.exit(1)
    
    main_py = project_root / "src" / "main.py"
    if not main_py.exists():
        print("❌ Main script 'src/main.py' not found!")
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
    
    print("\n🔨 Starting PyInstaller build...")
    print("-" * 30)
    
    try:
        # Run PyInstaller with the spec file
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--clean",
            "--noconfirm", 
            str(spec_path)
        ]
        
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=project_root, check=True, capture_output=True, text=True)
        
        print("✅ Build successful!")
        
        # Check if the executable file was created (with or without .exe extension)
        exe_name = "AI-noye_Job_Crawler.exe" if platform.system() == "Windows" else "AI-noye_Job_Crawler"
        exe_path = dist_dir / exe_name
        if exe_path.exists():
            file_size = exe_path.stat().st_size / (1024 * 1024)  # Size in MB
            print(f"🎉 Executable created: {exe_path}")
            print(f"📊 File size: {file_size:.1f} MB")
            
            # Create a release directory with additional files
            release_dir = project_root / "release"
            if release_dir.exists():
                shutil.rmtree(release_dir)
            release_dir.mkdir()
            
            # Copy executable file
            release_exe_name = "AI-noye_Job_Crawler.exe" if platform.system() == "Windows" else "AI-noye_Job_Crawler"
            shutil.copy2(exe_path, release_dir / release_exe_name)
            
            # Copy logo
            shutil.copy2(logo_path, release_dir / "ai-noye-logo.png")
            
            # Create README for users
            readme_content = """# AI-noye Job Crawler

## 🚀 How to Use

1. **Run the Application**: Double-click `AI-noye_Job_Crawler.exe`
2. **Follow the Prompts**: The application will guide you through:
   - Site selection (LinkedIn, Indeed, Work24)
   - Login credentials
   - Output directory selection
   - Search keywords
   - Number of jobs to collect

## 📋 Requirements

- **Internet Connection**: Required for job site access
- **Chrome Browser**: Must be installed (any version)
- **Windows 10/11**: Recommended operating system

## 📁 Output

- Excel files will be saved to your chosen directory
- Files are named: `{site}_채용정보_{timestamp}.xlsx`
- Batch saving prevents data loss (saves every 10 jobs)
- Automatic duplicate detection

## 🔧 Features

- **Stealth Browsing**: Avoids bot detection
- **Human-like Behavior**: Random delays and mouse movements  
- **Safe Batch Saving**: Data saved every 10 jobs
- **Duplicate Detection**: Skips already collected jobs
- **Cross-site Support**: LinkedIn, Indeed, Work24

## 📞 Support

For issues or questions, contact AI-noye support team.

---
Built with ❤️ by AI-noye Team
"""
            
            with open(release_dir / "README.txt", "w", encoding="utf-8") as f:
                f.write(readme_content)
            
            print(f"📦 Release package created: {release_dir}")
            print("\n🎯 Ready for distribution!")
            
        else:
            print("❌ Executable file not found after build!")
            sys.exit(1)
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()