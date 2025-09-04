"""
GUI-compatible wrapper for the main crawler with callback support
"""

from typing import Optional, Callable, List
from pathlib import Path
import structlog

from .main_crawler import JobCrawler
from .core.models import SearchFilters, JobListing
from .core.config import get_settings


class MainCrawler:
    """GUI-compatible crawler wrapper with logging callbacks"""
    
    def __init__(self, site_name: str, username: str, password: str, 
                 filters: SearchFilters, logger_callback: Optional[Callable[[str], None]] = None):
        self.site_name = site_name
        self.username = username  
        self.password = password
        self.filters = filters
        self.logger_callback = logger_callback or (lambda msg: print(msg))
        
        # Initialize the actual crawler
        self.crawler = JobCrawler(
            site_name=site_name,
            user_credentials=(username, password),
            output_directory=get_settings().output_dir
        )
        
        # Set up logging
        self.logger = structlog.get_logger()
        
    def log(self, message: str):
        """Send log message to GUI"""
        self.logger_callback(message)
        self.logger.info(message)
    
    def login(self) -> bool:
        """This method is not needed as JobCrawler handles login internally"""
        self.log(f"🌐 {self.site_name.upper()} 준비 중...")
        return True
    
    def crawl_jobs(self) -> List[JobListing]:
        """Crawl jobs with progress updates"""
        try:
            self.log("🚀 크롤링 시작...")
            self.log(f"📊 최대 {self.filters.max_results}개 채용공고 수집 예정")
            
            # The JobCrawler.crawl_jobs method handles everything:
            # - Browser initialization
            # - Login 
            # - Navigation
            # - Search filtering
            # - Job collection
            # - Excel export
            excel_path = self.crawler.crawl_jobs(self.filters)
            
            if excel_path:
                self.log(f"🎉 크롤링 성공!")
                self.log(f"📁 Excel 파일 저장됨: {excel_path}")
                
                # Return the collected jobs for display purposes
                return self.crawler.jobs if hasattr(self.crawler, 'jobs') else []
            else:
                self.log("⚠️ 크롤링 실패 또는 수집된 채용공고가 없습니다.")
                return []
            
        except Exception as e:
            self.log(f"❌ 크롤링 중 오류 발생: {str(e)}")
            return []
    
    def cleanup(self):
        """Clean up resources"""
        try:
            # JobCrawler handles its own cleanup via the context manager
            self.log("🧹 정리 완료")
        except Exception as e:
            self.log(f"⚠️ 정리 중 오류: {str(e)}")