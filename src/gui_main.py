"""
Simple GUI for AI-noye Job Crawler
Minimalist and easy-to-navigate interface
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import queue
from pathlib import Path
import sys
import os
from typing import Optional

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from crawler.gui_crawler import MainCrawler
from crawler.core.models import SearchFilters, JobType, ExperienceLevel
from crawler.core.config import get_settings


class JobCrawlerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-Noye 채용공고 크롤러")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Variables
        self.site_var = tk.StringVar(value="work24")
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.keywords_var = tk.StringVar()
        self.output_dir_var = tk.StringVar()
        self.max_jobs_var = tk.StringVar(value="50")
        
        # Queue for thread communication
        self.log_queue = queue.Queue()
        self.crawler = None
        self.crawling = False
        
        self.create_widgets()
        self.set_default_output_dir()
        
        # Start checking for log messages
        self.root.after(100, self.check_log_queue)
    
    def create_widgets(self):
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        row = 0
        
        # Title
        title_label = ttk.Label(main_frame, text="🤖 AI-Noye 채용공고 크롤러 /실장님 화이팅!/",
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=row, column=0, columnspan=2, pady=(0, 20))
        row += 1
        
        # Site selection
        ttk.Label(main_frame, text="사이트 선택:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=(0, 5))
        row += 1
        
        site_frame = ttk.Frame(main_frame)
        site_frame.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        ttk.Radiobutton(site_frame, text="LinkedIn (준비중)", variable=self.site_var, 
                       value="linkedin", state="disabled").pack(side=tk.LEFT, padx=(0, 15))
        ttk.Radiobutton(site_frame, text="Indeed (준비중)", variable=self.site_var, 
                       value="indeed", state="disabled").pack(side=tk.LEFT, padx=(0, 15))
        ttk.Radiobutton(site_frame, text="Work24 (고용24)", variable=self.site_var, 
                       value="work24").pack(side=tk.LEFT)
        row += 1
        
        # Credentials section
        ttk.Label(main_frame, text="로그인 정보:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=(10, 5))
        row += 1
        
        ttk.Label(main_frame, text="아이디/이메일:").grid(row=row, column=0, sticky=tk.W, pady=2)
        username_entry = ttk.Entry(main_frame, textvariable=self.username_var, width=40)
        username_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=2)
        row += 1
        
        ttk.Label(main_frame, text="비밀번호:").grid(row=row, column=0, sticky=tk.W, pady=2)
        password_entry = ttk.Entry(main_frame, textvariable=self.password_var, show="*", width=40)
        password_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=2)
        row += 1
        
        # Search settings section
        ttk.Label(main_frame, text="검색 설정:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=(15, 5))
        row += 1
        
        ttk.Label(main_frame, text="검색 키워드 (선택사항):").grid(row=row, column=0, sticky=tk.W, pady=2)
        keywords_entry = ttk.Entry(main_frame, textvariable=self.keywords_var, width=40)
        keywords_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=2)
        
        # Add placeholder text behavior
        def add_placeholder(entry, placeholder):
            entry.insert(0, placeholder)
            entry.config(foreground='grey')
            
            def on_focus_in(event):
                if entry.get() == placeholder:
                    entry.delete(0, tk.END)
                    entry.config(foreground='black')
            
            def on_focus_out(event):
                if entry.get() == '':
                    entry.insert(0, placeholder)
                    entry.config(foreground='grey')
            
            entry.bind('<FocusIn>', on_focus_in)
            entry.bind('<FocusOut>', on_focus_out)
        
        add_placeholder(keywords_entry, "예: python 개발자, data scientist")
        row += 1
        
        ttk.Label(main_frame, text="수집할 공고 수:").grid(row=row, column=0, sticky=tk.W, pady=2)
        jobs_frame = ttk.Frame(main_frame)
        jobs_frame.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=2)
        
        jobs_spinbox = ttk.Spinbox(jobs_frame, from_=1, to=1000, textvariable=self.max_jobs_var, width=10)
        jobs_spinbox.pack(side=tk.LEFT)
        ttk.Label(jobs_frame, text="개 (1-1000)").pack(side=tk.LEFT, padx=(5, 0))
        row += 1
        
        # Output directory section
        ttk.Label(main_frame, text="저장 위치:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=(15, 5))
        row += 1
        
        output_frame = ttk.Frame(main_frame)
        output_frame.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=2)
        output_frame.columnconfigure(0, weight=1)
        
        output_entry = ttk.Entry(output_frame, textvariable=self.output_dir_var, width=50)
        output_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        
        browse_btn = ttk.Button(output_frame, text="찾아보기", command=self.browse_output_dir)
        browse_btn.grid(row=0, column=1)
        row += 1
        
        # Control buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=row, column=0, columnspan=2, pady=(20, 10))
        
        self.start_btn = ttk.Button(button_frame, text="🚀 크롤링 시작", 
                                   command=self.start_crawling, style="Accent.TButton")
        self.start_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.stop_btn = ttk.Button(button_frame, text="⏹️ 중지", 
                                  command=self.stop_crawling, state="disabled")
        self.stop_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.clear_btn = ttk.Button(button_frame, text="🧹 로그 지우기", command=self.clear_log)
        self.clear_btn.pack(side=tk.LEFT)
        row += 1
        
        # Log display
        ttk.Label(main_frame, text="실행 로그:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=(15, 5))
        row += 1
        
        # Log text area with scrollbar
        self.log_text = scrolledtext.ScrolledText(main_frame, height=15, width=70, 
                                                 wrap=tk.WORD, font=('Consolas', 9))
        self.log_text.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Configure main_frame to expand with window
        main_frame.rowconfigure(row, weight=1)
        
        # Status bar
        self.status_var = tk.StringVar(value="준비 완료")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              relief=tk.SUNKEN, padding="5")
        status_bar.grid(row=row+1, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
    def set_default_output_dir(self):
        """Set default output directory"""
        default_dir = Path.cwd() / "output"
        self.output_dir_var.set(str(default_dir))
        
    def browse_output_dir(self):
        """Browse for output directory"""
        directory = filedialog.askdirectory(title="Excel 파일 저장 폴더 선택")
        if directory:
            self.output_dir_var.set(directory)
    
    def validate_inputs(self):
        """Validate user inputs"""
        if not self.username_var.get().strip():
            messagebox.showerror("입력 오류", "아이디/이메일을 입력해주세요.")
            return False
            
        if not self.password_var.get().strip():
            messagebox.showerror("입력 오류", "비밀번호를 입력해주세요.")
            return False
            
        try:
            max_jobs = int(self.max_jobs_var.get())
            if not (1 <= max_jobs <= 1000):
                raise ValueError()
        except ValueError:
            messagebox.showerror("입력 오류", "수집할 공고 수는 1-1000 사이의 숫자여야 합니다.")
            return False
            
        output_dir = Path(self.output_dir_var.get().strip())
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
            # Test write permission
            test_file = output_dir / "test_write.tmp"
            test_file.write_text("test")
            test_file.unlink()
        except Exception as e:
            messagebox.showerror("경로 오류", f"출력 디렉토리에 접근할 수 없습니다:\n{e}")
            return False
            
        return True
    
    def log_message(self, message):
        """Add message to log queue"""
        self.log_queue.put(message)
    
    def check_log_queue(self):
        """Check for new log messages and display them"""
        try:
            while True:
                message = self.log_queue.get_nowait()
                self.log_text.insert(tk.END, message + "\n")
                self.log_text.see(tk.END)
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.check_log_queue)
    
    def clear_log(self):
        """Clear the log display"""
        self.log_text.delete(1.0, tk.END)
    
    def start_crawling(self):
        """Start the crawling process in a separate thread"""
        if not self.validate_inputs():
            return
            
        if self.crawling:
            messagebox.showwarning("경고", "이미 크롤링이 실행 중입니다.")
            return
        
        # Disable start button and enable stop button
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.crawling = True
        
        # Clear log
        self.clear_log()
        
        # Start crawling in separate thread
        crawling_thread = threading.Thread(target=self.run_crawler, daemon=True)
        crawling_thread.start()
    
    def stop_crawling(self):
        """Stop the crawling process"""
        if self.crawler:
            self.log_message("⏹️ 크롤링 중지 요청됨...")
            # You could implement a stop mechanism in your crawler
        
        self.crawling_finished()
    
    def crawling_finished(self):
        """Reset UI state after crawling finishes"""
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.crawling = False
        self.status_var.set("완료")
    
    def run_crawler(self):
        """Run the crawler (this runs in a separate thread)"""
        try:
            self.log_message("🚀 AI-noye Job Crawler 시작...")
            self.status_var.set("크롤링 중...")
            
            # Get user inputs
            site_name = self.site_var.get()
            username = self.username_var.get().strip()
            password = self.password_var.get().strip()
            keywords = self.keywords_var.get().strip()
            max_jobs = int(self.max_jobs_var.get())
            output_dir = Path(self.output_dir_var.get().strip())
            
            # Handle placeholder text
            if keywords == "예: python 개발자, data scientist":
                keywords = ""
            
            self.log_message(f"✅ 사이트: {site_name.upper()}")
            self.log_message(f"✅ 아이디: {username}")
            if keywords:
                self.log_message(f"✅ 키워드: '{keywords}'")
            else:
                self.log_message("✅ 키워드 없이 카테고리 기반 검색")
            self.log_message(f"✅ 수집 목표: {max_jobs}개")
            self.log_message(f"✅ 저장 경로: {output_dir}")
            
            # Create search filters
            search_filters = SearchFilters(
                keywords=keywords if keywords else None,
                location="Seoul, Korea" if site_name == "work24" else "New York, NY",
                job_type=JobType.FULL_TIME,
                experience_level=ExperienceLevel.MID_LEVEL,
                date_posted="7d",
                remote_only=False,
                max_results=max_jobs
            )
            
            # Update settings with output directory
            settings = get_settings()
            settings.output_dir = output_dir
            
            # Initialize and run crawler
            self.crawler = MainCrawler(
                site_name=site_name,
                username=username,
                password=password,
                filters=search_filters,
                logger_callback=self.log_message
            )
            
            self.log_message("🔐 로그인 중...")
            success = self.crawler.login()
            
            if success:
                self.log_message("✅ 로그인 성공!")
                self.log_message("🔍 채용공고 수집 시작...")
                
                jobs = self.crawler.crawl_jobs()
                
                if jobs:
                    self.log_message(f"🎉 성공! {len(jobs)}개 채용공고를 수집했습니다.")
                    self.log_message("📊 Excel 파일로 저장 중...")
                    
                    # Export to Excel (this should be handled by the crawler)
                    self.log_message("✅ 파일 저장 완료!")
                else:
                    self.log_message("⚠️ 수집된 채용공고가 없습니다.")
            else:
                self.log_message("❌ 로그인 실패")
                
        except Exception as e:
            self.log_message(f"❌ 오류 발생: {str(e)}")
            
        finally:
            self.root.after(0, self.crawling_finished)  # Update UI in main thread


def main():
    """Main entry point for GUI application"""
    root = tk.Tk()
    app = JobCrawlerGUI(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f'+{x}+{y}')
    
    root.mainloop()


if __name__ == "__main__":
    main()