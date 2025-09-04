"""Main job crawler orchestrator."""

import structlog
from typing import List, Optional, Dict, Any
from pathlib import Path
import random
import time

from .core.base_crawler import StealthCrawler
from .core.auth import AuthenticationManager
from .core.search_engine import SearchEngine
from .core.job_extractor import JobExtractor
from .utils.excel_exporter import ExcelExporter
from .core.models import SearchFilters, JobListing, CrawlerSession
from .core.config import get_settings

logger = structlog.get_logger()


class JobCrawler:
    """Main job crawler that orchestrates the entire crawling process."""
    
    def __init__(self, site_name: str, user_credentials: Optional[tuple[str, str]] = None, output_directory: Optional[Path] = None):
        self.site_name = site_name
        self.settings = get_settings()
        self.jobs: List[JobListing] = []
        self.user_credentials = user_credentials
        
        # Override output directory if provided by user
        if output_directory:
            self.settings.output_dir = output_directory
            logger.info(f"Using custom output directory: {output_directory}")
        
    def crawl_jobs(self, filters: SearchFilters) -> Optional[Path]:
        """
        Main crawling method that coordinates the entire process.
        
        Args:
            filters: Search criteria for job filtering
            
        Returns:
            Path to exported Excel file, or None if crawling failed
        """
        try:
            logger.info(f"Starting job crawl for {self.site_name}")
            print(f"🚀 {self.site_name.upper()} 채용공고 크롤링을 시작합니다...")
            
            # Initialize Excel file path tracker
            self.excel_file_path = None
            
            with StealthCrawler(self.site_name, filters) as crawler:
                # Initialize components
                print("⚙️ 크롤러 구성 요소를 초기화하는 중...")
                auth_manager = AuthenticationManager(crawler)
                search_engine = SearchEngine(crawler)
                job_extractor = JobExtractor(crawler)
                
                # Step 1: Navigate to site
                print(f"🌐 {self.site_name.upper()} 사이트로 이동 중...")
                crawler.navigate_to_site()
                
                # Step 2: Login if credentials are available
                if self.user_credentials:
                    email, password = self.user_credentials
                    print("🔐 사용자 계정으로 로그인 중...")
                    login_success = auth_manager.login(email, password)
                    if not login_success:
                        print("❌ 로그인 실패! 크롤링을 중단합니다.")
                        logger.error("Login failed, aborting crawl")
                        return None
                    print("✅ 로그인 성공!")
                else:
                    email, password = auth_manager.get_credentials()
                    if email and password:
                        print("🔐 저장된 계정 정보로 로그인 중...")
                        login_success = auth_manager.login(email, password)
                        if not login_success:
                            print("❌ 로그인 실패! 크롤링을 중단합니다.")
                            logger.error("Login failed, aborting crawl")
                            return None
                        print("✅ 로그인 성공!")
                    else:
                        print("ℹ️ 계정 정보가 없어 로그인 없이 진행합니다.")
                        logger.info("No credentials provided, proceeding without login")
                
                # Step 3: Navigate to jobs page and apply filters
                print("🔍 채용공고 검색 페이지로 이동 중...")
                search_engine.navigate_to_jobs_page()
                print(f"🎯 검색 필터 적용 중... (키워드: '{filters.keywords}')")
                search_engine.apply_search_filters(filters)
                
                # Step 4: Crawl job listings with batch saving and duplicate detection
                print(f"📋 채용공고 수집 시작... (최대 {filters.max_results}개)")
                print(f"💾 {self.settings.batch_save_size}개씩 배치 저장으로 데이터 손실을 방지합니다.")
                print("🔍 중복 채용공고 자동 스킵 기능이 활성화되었습니다.")
                self._crawl_all_pages(crawler, job_extractor, filters.max_results)
                
                # Step 5: Check results and provide summary
                if self.jobs:
                    print(f"🎉 크롤링 성공! 총 {len(self.jobs)}개 채용공고를 수집했습니다.")
                    print("📊 배치 저장으로 모든 데이터가 안전하게 보관되었습니다.")
                    
                    # Check if we have the Excel file path from batch saving
                    if hasattr(self, 'excel_file_path') and self.excel_file_path:
                        excel_path = self.excel_file_path
                        
                        # Create summary report (for logging purposes)
                        from crawler.utils.excel_exporter import ExcelExporter
                        exporter = ExcelExporter()
                        summary = exporter.create_summary_report(self.jobs)
                        logger.info(f"Crawl completed: {summary}")
                        print(f"✅ 크롤링 완료! Excel 파일: {excel_path.name}")
                        
                        return excel_path
                    else:
                        # Fallback: try to find the most recent Excel file
                        print("🔍 Excel 파일 경로를 찾는 중...")
                        output_dir = self.settings.output_dir
                        excel_files = list(output_dir.glob(f"{self.site_name}_채용정보_*.xlsx"))
                        
                        if excel_files:
                            # Get the most recent file
                            excel_path = max(excel_files, key=lambda x: x.stat().st_mtime)
                            print(f"✅ Excel 파일 발견: {excel_path.name}")
                            return excel_path
                        else:
                            logger.warning("No Excel files found after crawling")
                            print("⚠️ Excel 파일을 찾을 수 없습니다.")
                            return None
                else:
                    print("⚠️ 수집된 채용공고가 없습니다.")
                    logger.warning("No jobs found to export")
                    return None
                    
        except Exception as e:
            print(f"❌ 크롤링 중 오류 발생: {e}")
            logger.error(f"Crawling failed: {e}")
            return None
    
    def _crawl_all_pages(
        self, 
        crawler: StealthCrawler, 
        job_extractor: JobExtractor, 
        max_results: int
    ) -> None:
        """Crawl all pages of search results with configurable batch saving for data safety."""
        page_num = 1
        jobs_processed = 0
        
        # Batch saving configuration
        BATCH_SIZE = self.settings.batch_save_size
        batch_jobs = []
        batch_num = 1
        excel_file_path = None  # Track the Excel file path
        exporter = None  # Initialize when needed
        existing_job_ids = set()  # Track existing job IDs to avoid duplicates
        
        # Generate base filename for this crawl session
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = f"{self.site_name}_채용정보_{timestamp}"
        
        # Check if there are existing Excel files to load job IDs from (for duplicate detection across sessions)
        try:
            output_dir = self.settings.output_dir
            existing_excel_files = list(output_dir.glob(f"{self.site_name}_채용정보_*.xlsx"))
            if existing_excel_files:
                # Get the most recent file to load existing job IDs
                latest_file = max(existing_excel_files, key=lambda x: x.stat().st_mtime)
                try:
                    import pandas as pd
                    existing_df = pd.read_excel(latest_file, sheet_name="채용공고")
                    if "채용ID" in existing_df.columns:
                        existing_job_ids = set(existing_df["채용ID"].dropna().astype(str))
                        print(f"🔍 기존 Excel 파일에서 {len(existing_job_ids)}개 채용공고 ID를 로드했습니다.")
                        logger.info(f"Loaded {len(existing_job_ids)} existing job IDs for duplicate detection")
                except Exception as load_error:
                    logger.warning(f"Could not load existing job IDs: {load_error}")
                    existing_job_ids = set()
        except Exception:
            existing_job_ids = set()
        
        while jobs_processed < max_results:
            try:
                print(f"📄 {page_num}페이지 처리 중...")
                logger.info(f"Processing page {page_num}")
                
                # Save current page URL for navigation back
                current_search_url = crawler.driver.current_url
                print(f"🔗 현재 검색 결과 페이지 URL 저장: {current_search_url}")
                
                # Extract job listings from current page
                print("🔍 현재 페이지에서 채용공고 목록 추출 중...")
                job_listings = job_extractor.extract_job_listings_from_search()
                
                if not job_listings:
                    print(f"⚠️ {page_num}페이지에서 채용공고를 찾을 수 없습니다.")
                    logger.warning(f"No jobs found on page {page_num}")
                    break
                
                print(f"📋 {len(job_listings)}개의 채용공고를 발견했습니다.")
                
                # Process each job listing
                for i, job_data in enumerate(job_listings, 1):
                    if jobs_processed >= max_results:
                        break
                    
                    try:
                        print(f"📝 채용공고 {jobs_processed + 1}/{max_results} 처리 중... ({i}/{len(job_listings)})")
                        
                        # Extract detailed job information
                        print("🔍 상세 정보 추출 중...")
                        detailed_job = job_extractor.extract_detailed_job_info(
                            job_data["job_url"], job_data
                        )
                        
                        if detailed_job:
                            # Check for duplicate job ID
                            if detailed_job.job_id and detailed_job.job_id in existing_job_ids:
                                print(f"⚠️ 중복 채용공고 스킵: {detailed_job.job_id} - {detailed_job.title}")
                                logger.info(f"Skipping duplicate job ID: {detailed_job.job_id}")
                                continue
                            
                            # Add to current batch
                            batch_jobs.append(detailed_job)
                            # Also keep in main list for backward compatibility
                            self.jobs.append(detailed_job)
                            # Track this job ID
                            if detailed_job.job_id:
                                existing_job_ids.add(detailed_job.job_id)
                            
                            jobs_processed += 1
                            print(f"✅ 완료: {detailed_job.title} - {detailed_job.company}")
                            
                            logger.debug(
                                f"Processed job {jobs_processed}/{max_results}: "
                                f"{detailed_job.title} at {detailed_job.company}"
                            )
                            
                            # Check if we need to save a batch
                            if len(batch_jobs) >= BATCH_SIZE:
                                # Initialize exporter if needed
                                if exporter is None:
                                    from crawler.utils.excel_exporter import ExcelExporter
                                    exporter = ExcelExporter()
                                
                                try:
                                    if batch_num == 1:
                                        # First batch - create new file
                                        print(f"💾 첫 번째 배치 저장 중... ({BATCH_SIZE}개 채용공고)")
                                        excel_file_path = exporter.save_incremental_batch(
                                            batch_jobs, batch_num, base_filename, is_first_batch=True
                                        )
                                        print(f"✅ 배치 {batch_num} 저장 완료: {excel_file_path.name}")
                                    else:
                                        # Subsequent batches - append
                                        print(f"💾 배치 {batch_num} 추가 저장 중... ({len(batch_jobs)}개 채용공고)")
                                        exporter.save_incremental_batch(
                                            batch_jobs, batch_num, base_filename, is_first_batch=False
                                        )
                                        print(f"✅ 배치 {batch_num} 저장 완료")
                                    
                                    # Clear batch and increment counter
                                    batch_jobs = []
                                    batch_num += 1
                                    
                                    logger.info(f"Successfully saved batch {batch_num - 1} with {BATCH_SIZE} jobs")
                                    
                                except Exception as batch_save_error:
                                    print(f"❌ 배치 저장 실패: {batch_save_error}")
                                    logger.error(f"Failed to save batch {batch_num}: {batch_save_error}")
                                    # Continue crawling even if batch save fails
                            
                        else:
                            print("⚠️ 상세 정보 추출 실패")
                        
                        # Navigate back to search results page after each job
                        print("🔙 검색 결과 페이지로 돌아가는 중...")
                        crawler.driver.get(current_search_url)
                        crawler.human_behavior.random_delay(1.5, 2.5)  # Wait for page load
                        
                        # Human-like delay between job extractions (reduced for speed)
                        print("⏳ 잠시 대기 중...")
                        crawler.human_behavior.random_delay(
                            max(1.0, self.settings.crawl_delay_min - 1.0),  # Reduced delay
                            max(2.0, self.settings.crawl_delay_max - 2.0)   # Reduced delay
                        )
                        
                    except Exception as e:
                        print(f"❌ 채용공고 처리 실패: {e}")
                        logger.warning(f"Failed to process job listing: {e}")
                        crawler.session.add_error()
                        # Navigate back to search results in case of error
                        try:
                            crawler.driver.get(current_search_url)
                            crawler.human_behavior.random_delay(1.0, 2.0)
                        except:
                            pass
                        continue
                
                # Check if we should continue to next page
                if jobs_processed < max_results:
                    print(f"📊 진행 상황: {jobs_processed}/{max_results} 완료, 다음 페이지 확인 중...")
                    
                    from crawler.core.search_engine import SearchEngine
                    search_engine = SearchEngine(crawler)
                    
                    if search_engine.has_next_page():
                        print("➡️ 다음 페이지로 이동 중...")
                        
                        if search_engine.go_to_next_page():
                            page_num += 1
                            print(f"✅ {page_num}페이지로 이동 완료")
                            # Shorter pause between pages for speed
                            crawler.human_behavior.random_delay(2.0, 4.0)  # Reduced from 3.0-7.0
                        else:
                            print("❌ 다음 페이지로 이동할 수 없습니다. 크롤링을 종료합니다.")
                            logger.info("Could not navigate to next page, ending crawl")
                            break
                    else:
                        print("📄 더 이상 페이지가 없습니다.")
                        logger.info("No more pages available")
                        break
                else:
                    print(f"🎯 목표 수집량 달성! ({max_results}개)")
                    logger.info(f"Reached maximum results limit: {max_results}")
                    break
                    
            except Exception as e:
                print(f"❌ {page_num}페이지 처리 중 오류 발생: {e}")
                logger.error(f"Error processing page {page_num}: {e}")
                break
        
        # Save any remaining jobs in the final batch
        if batch_jobs:
            # Initialize exporter if needed
            if exporter is None:
                from crawler.utils.excel_exporter import ExcelExporter
                exporter = ExcelExporter()
            
            try:
                print(f"💾 마지막 배치 저장 중... ({len(batch_jobs)}개 채용공고)")
                if batch_num == 1:
                    # Only one partial batch - create new file
                    excel_file_path = exporter.save_incremental_batch(
                        batch_jobs, batch_num, base_filename, is_first_batch=True
                    )
                    print(f"✅ 최종 배치 저장 완료: {excel_file_path.name}")
                else:
                    # Append remaining jobs
                    exporter.save_incremental_batch(
                        batch_jobs, batch_num, base_filename, is_first_batch=False
                    )
                    print(f"✅ 최종 배치 {batch_num} 저장 완료")
                
                logger.info(f"Successfully saved final batch with {len(batch_jobs)} jobs")
                
            except Exception as final_batch_error:
                print(f"❌ 최종 배치 저장 실패: {final_batch_error}")
                logger.error(f"Failed to save final batch: {final_batch_error}")
        
        # Store the Excel file path for main crawler to find
        if excel_file_path:
            self.excel_file_path = excel_file_path
        
        print(f"🏁 크롤링 완료! 총 {jobs_processed}개 채용공고를 {page_num}페이지에서 수집했습니다.")
        if batch_num > 1 or batch_jobs:
            total_batches = batch_num - 1 + (1 if batch_jobs else 0)
            print(f"💾 총 {total_batches}개 배치로 안전하게 저장되었습니다.")
            if excel_file_path:
                print(f"📄 Excel 파일: {excel_file_path.name}")
        logger.info(f"Crawling completed. Processed {jobs_processed} jobs across {page_num} pages")
    
    def get_session_stats(self) -> Dict[str, Any]:
        """Get statistics about the current crawling session."""
        return {
            "jobs_found": len(self.jobs),
            "site_crawled": self.site_name,
            "unique_companies": len(set(job.company for job in self.jobs)),
            "locations": list(set(job.location for job in self.jobs))[:10],  # Top 10
            "avg_jobs_per_company": len(self.jobs) / len(set(job.company for job in self.jobs)) if self.jobs else 0
        }