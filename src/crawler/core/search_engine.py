"""Job search and filtering engine."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import structlog
from typing import List, Dict, Any, Optional
import urllib.parse

from .base_crawler import StealthCrawler
from .models import SearchFilters, JobType, ExperienceLevel

logger = structlog.get_logger()


class SearchEngine:
    """Handles job search and filtering operations."""
    
    def __init__(self, crawler: StealthCrawler):
        self.crawler = crawler
        self.site_config = crawler.site_config
        
    def navigate_to_jobs_page(self) -> None:
        """Navigate to the jobs search page."""
        import time
        start_time = time.time()
        
        try:
            jobs_url = self.site_config["jobs_url"]
            print(f"🔗 채용공고 검색 페이지로 이동 중: {jobs_url}")
            logger.info(f"Navigating to jobs page: {jobs_url}")
            
            nav_start = time.time()
            self.crawler.driver.get(jobs_url)
            print("✅ 페이지 이동 완료!")
            logger.info(f"Jobs page navigation completed in {time.time() - nav_start:.2f}s")
            
            # Wait for page to load (reduced from 2-4s)
            print("⏳ 페이지 로딩 대기 중...")
            load_start = time.time()
            self.crawler.human_behavior.random_delay(1.0, 2.0)
            logger.info(f"Jobs page load wait completed in {time.time() - load_start:.2f}s")
            
            # Remove problematic mouse movements that cause "out of bounds" errors
            # self.crawler.human_behavior.random_mouse_movements(2)  # DISABLED
            
            # Simulate reading page content
            print("👀 페이지 내용 읽기 시뮬레이션 중...")
            read_start = time.time()
            self.crawler.human_behavior.reading_pause(100)  # Reduced from 500
            print("✅ 페이지 준비 완료!")
            logger.info(f"Page reading simulation completed in {time.time() - read_start:.2f}s")
            
            logger.info(f"Successfully navigated to jobs page in {time.time() - start_time:.2f}s")
            
        except Exception as e:
            print(f"❌ 채용공고 페이지 이동 실패: {e}")
            logger.error(f"Failed to navigate to jobs page after {time.time() - start_time:.2f}s: {e}")
            raise
    
    def apply_search_filters(self, filters: SearchFilters) -> None:
        """Apply search filters based on the search criteria."""
        import time
        start_time = time.time()
        
        try:
            print("🎯 검색 필터 적용을 시작합니다...")
            logger.info("Applying search filters")
            
            # Use Work24-specific filter flow
            if self.crawler.site_name == "work24":
                print("🏢 Work24 전용 필터 적용 중...")
                self._apply_work24_filters(filters)
                print("✅ Work24 필터 적용 완료!")
                logger.info(f"Work24 filters applied in {time.time() - start_time:.2f}s")
                return
            
            # Standard filter flow for other sites
            print("📝 표준 필터 적용 프로세스 시작...")
            
            # Apply keyword search
            if filters.keywords:
                print(f"🔤 키워드 필터 적용 중: '{filters.keywords}'")
                self._apply_keyword_filter(filters.keywords)
                print("✅ 키워드 필터 적용 완료!")
            
            # Apply location filter
            if filters.location:
                print(f"📍 위치 필터 적용 중: '{filters.location}'")
                self._apply_location_filter(filters.location)
                print("✅ 위치 필터 적용 완료!")
            
            # Apply job type filter
            if filters.job_type:
                print(f"💼 고용 형태 필터 적용 중: {filters.job_type.value}")
                self._apply_job_type_filter(filters.job_type)
                print("✅ 고용 형태 필터 적용 완료!")
            
            # Apply experience level filter
            if filters.experience_level:
                print(f"🎓 경력 수준 필터 적용 중: {filters.experience_level.value}")
                self._apply_experience_filter(filters.experience_level)
                print("✅ 경력 수준 필터 적용 완료!")
            
            # Apply date posted filter
            if filters.date_posted:
                print(f"📅 게시일 필터 적용 중: {filters.date_posted}")
                self._apply_date_filter(filters.date_posted)
                print("✅ 게시일 필터 적용 완료!")
            
            # Apply remote work filter
            if filters.remote_only:
                print("🏠 원격근무 필터 적용 중...")
                self._apply_remote_filter()
                print("✅ 원격근무 필터 적용 완료!")
            
            # Submit search
            print("🚀 검색 실행 중...")
            self._submit_search()
            print("✅ 검색 필터 적용 및 실행 완료!")
            
            logger.info(f"Search filters applied successfully in {time.time() - start_time:.2f}s")
            
        except Exception as e:
            print(f"❌ 검색 필터 적용 실패: {e}")
            logger.error(f"Failed to apply search filters after {time.time() - start_time:.2f}s: {e}")
            raise

    def _apply_work24_filters(self, filters: SearchFilters) -> None:
        """Apply Work24-specific search filters with proper section expansion."""
        import time
        
        try:
            logger.info("Applying Work24-specific search filters")
            print("🏢 Work24 통합 검색 필터 적용 시작...")
            start_time = time.time()
            
            # 1. Enter keyword in search field (optional)
            if filters.keywords:
                print(f"🔤 검색어 입력 중: '{filters.keywords}'")
                keyword_field = self.crawler.wait_for_element("#srcKeyword", timeout=10)
                if keyword_field:
                    keyword_field.clear()
                    self.crawler.human_behavior.human_type(keyword_field, filters.keywords)
                    print("✅ 검색어 입력 완료!")
                    logger.info(f"Entered keywords: {filters.keywords}")
                else:
                    print("❌ 검색어 입력 필드를 찾을 수 없습니다.")
                    logger.warning("Could not find keyword input field")
            else:
                print("ℹ️ 키워드 없이 카테고리 기반 검색을 진행합니다.")
            
            # 2. Click "직종선택" button to expand job categories
            print("📂 직종선택 버튼 클릭하여 카테고리 섹션 확장 중...")
            try:
                category_button = self.crawler.wait_for_element(
                    self.site_config["selectors"]["filters"]["category_button"], timeout=10
                )
                if category_button:
                    self.crawler.driver.execute_script("arguments[0].scrollIntoView(true);", category_button)
                    self.crawler.human_behavior.random_delay(0.8, 1.5)
                    self.crawler.driver.execute_script("arguments[0].click();", category_button)
                    print("✅ 직종선택 버튼 클릭 완료!")
                    logger.info("Clicked category expansion button")
                    
                    # Wait for categories to expand
                    print("⏳ 카테고리 섹션 확장 대기 중...")
                    self.crawler.human_behavior.random_delay(2.0, 3.5)
                else:
                    print("❌ 직종선택 버튼을 찾을 수 없습니다.")
                    logger.error("Category expansion button not found")
                    raise Exception("직종선택 버튼 찾기 실패")
            except Exception as e:
                print(f"❌ 카테고리 섹션 확장 실패: {e}")
                logger.error(f"Category section expansion failed: {e}")
                raise
            
            # 3. Select main job category (연구 및 공학기술)
            print("🏗️ 주 카테고리 선택 중: 연구 및 공학기술")
            try:
                main_job_checkbox = self.crawler.wait_for_element(
                    self.site_config["selectors"]["filters"]["job_category_main"], timeout=8
                )
                if main_job_checkbox:
                    self.crawler.driver.execute_script("arguments[0].scrollIntoView(true);", main_job_checkbox)
                    self.crawler.human_behavior.random_delay(0.8, 1.5)
                    self.crawler.driver.execute_script("arguments[0].click();", main_job_checkbox)
                    print("✅ 주 카테고리 체크박스 선택 완료!")
                    logger.info("Selected main job category checkbox")
                    
                    # Wait a moment before clicking the button
                    self.crawler.human_behavior.random_delay(0.8, 1.2)
                    
                    # 3.1. Click the main category button to expand sub-categories
                    print("🔘 연구 및 공학기술 버튼 클릭하여 서브 카테고리 확장 중...")
                    main_category_button = self.crawler.wait_for_element(
                        self.site_config["selectors"]["filters"]["job_category_main_button"], timeout=8
                    )
                    if main_category_button:
                        self.crawler.driver.execute_script("arguments[0].scrollIntoView(true);", main_category_button)
                        self.crawler.human_behavior.random_delay(0.8, 1.5)
                        self.crawler.driver.execute_script("arguments[0].click();", main_category_button)
                        print("✅ 연구 및 공학기술 버튼 클릭 완료!")
                        logger.info("Clicked main category button to expand sub-categories")
                        
                        # Wait for sub-categories to load
                        print("⏳ 서브 카테고리 로딩 대기 중...")
                        self.crawler.human_behavior.random_delay(3.0, 4.5)
                    else:
                        print("❌ 연구 및 공학기술 버튼을 찾을 수 없습니다.")
                        logger.error("Main category button not found")
                        raise Exception("주 카테고리 버튼 찾기 실패")
                else:
                    print("❌ 주 카테고리 체크박스를 찾을 수 없습니다.")
                    logger.error("Main job category checkbox not found")
                    raise Exception("주 카테고리 체크박스 찾기 실패")
            except Exception as e:
                print(f"❌ 주 카테고리 선택 실패: {e}")
                logger.error(f"Main category selection failed: {e}")
                raise
            
            # 4. Select all relevant sub-categories
            print("🔧 모든 관련 서브 카테고리 선택 중...")
            sub_categories = self.site_config["selectors"]["filters"]["sub_categories"]
            selected_count = 0
            
            for category_name, selector in sub_categories.items():
                try:
                    print(f"📋 {category_name} 카테고리 선택 시도...")
                    category_checkbox = self.crawler.wait_for_element(selector, timeout=8)
                    if category_checkbox:
                        self.crawler.driver.execute_script("arguments[0].scrollIntoView(true);", category_checkbox)
                        self.crawler.human_behavior.random_delay(0.5, 1.0)
                        self.crawler.driver.execute_script("arguments[0].click();", category_checkbox)
                        selected_count += 1
                        print(f"✅ {category_name} 선택 완료!")
                        logger.info(f"Selected sub-category: {category_name}")
                    else:
                        print(f"⚠️ {category_name} 카테고리를 찾을 수 없습니다. 건너뜁니다.")
                        logger.warning(f"Sub-category not found: {category_name}")
                except Exception as e:
                    print(f"⚠️ {category_name} 선택 실패: {e}")
                    logger.debug(f"Sub-category selection failed for {category_name}: {e}")
                    continue
            
            print(f"📊 총 {selected_count}개 서브 카테고리 선택 완료!")
            
            # 5. Click "지역별" button to expand region selection
            print("📍 지역별 버튼 클릭하여 지역 선택 섹션 확장 중...")
            try:
                area_button = self.crawler.wait_for_element(
                    self.site_config["selectors"]["filters"]["area_button"], timeout=10
                )
                if area_button:
                    self.crawler.driver.execute_script("arguments[0].scrollIntoView(true);", area_button)
                    self.crawler.human_behavior.random_delay(0.8, 1.5)
                    self.crawler.driver.execute_script("arguments[0].click();", area_button)
                    print("✅ 지역별 버튼 클릭 완료!")
                    logger.info("Clicked area expansion button")
                    
                    # Wait for region list to appear
                    print("⏳ 지역 목록 확장 대기 중...")
                    self.crawler.human_behavior.random_delay(2.5, 4.0)
                else:
                    print("❌ 지역별 버튼을 찾을 수 없습니다.")
                    logger.error("Area expansion button not found")
                    raise Exception("지역별 버튼 찾기 실패")
            except Exception as e:
                print(f"❌ 지역 섹션 확장 실패: {e}")
                logger.error(f"Area section expansion failed: {e}")
                raise
                
            # 6. Select Seoul region
            print("🏙️ 서울 지역 선택 중...")
            try:
                seoul_button = self.crawler.wait_for_element(
                    self.site_config["selectors"]["filters"]["seoul_region"], timeout=10
                )
                if seoul_button:
                    self.crawler.driver.execute_script("arguments[0].scrollIntoView(true);", seoul_button)
                    self.crawler.human_behavior.random_delay(0.8, 1.5)
                    self.crawler.driver.execute_script("arguments[0].click();", seoul_button)
                    print("✅ 서울 지역 선택 완료!")
                    logger.info("Selected Seoul region")
                    
                    # Wait for Seoul sub-region options to load
                    print("⏳ 서울 하위 지역 옵션 로딩 대기 중...")
                    self.crawler.human_behavior.random_delay(2.5, 3.5)
                else:
                    print("❌ 서울 지역 버튼을 찾을 수 없습니다.")
                    logger.error("Seoul region button not found")
                    raise Exception("서울 지역 선택 실패")
            except Exception as e:
                print(f"❌ 서울 지역 선택 실패: {e}")
                logger.error(f"Seoul region selection failed: {e}")
                raise
            
            # 7. Select whole Seoul area
            print("🌐 서울 전체 지역 선택 중...")
            try:
                seoul_whole = self.crawler.wait_for_element(
                    self.site_config["selectors"]["filters"]["seoul_whole"], timeout=8
                )
                if seoul_whole:
                    self.crawler.driver.execute_script("arguments[0].scrollIntoView(true);", seoul_whole)
                    self.crawler.human_behavior.random_delay(0.5, 1.0)
                    self.crawler.driver.execute_script("arguments[0].click();", seoul_whole)
                    print("✅ 서울 전체 지역 선택 완료!")
                    logger.info("Selected whole Seoul region")
                    
                    # Wait for selection to be processed
                    self.crawler.human_behavior.random_delay(1.5, 2.5)
                else:
                    print("⚠️ 서울 전체 선택 옵션을 찾을 수 없습니다.")
                    logger.warning("Seoul whole region checkbox not found")
            except Exception as e:
                print(f"⚠️ 서울 전체 지역 선택 실패: {e}")
                logger.debug(f"Seoul whole region selection failed: {e}")
            
            # 8. Submit search
            print("🚀 통합 검색 실행 중...")
            try:
                search_start = time.time()
                search_button = self.crawler.wait_for_element(
                    self.site_config["selectors"]["filters"]["search_button"], timeout=12
                )
                if search_button:
                    self.crawler.driver.execute_script("arguments[0].scrollIntoView(true);", search_button)
                    self.crawler.human_behavior.random_delay(1.0, 2.0)
                    self.crawler.driver.execute_script("arguments[0].click();", search_button)
                    print("✅ 검색 버튼 클릭 완료!")
                    logger.info(f"Clicked search button in {time.time() - search_start:.2f}s")
                    
                    # Wait for search results to load
                    print("⏳ 검색 결과 로딩 대기 중 (6초)...")
                    self.crawler.human_behavior.random_delay(6.0, 8.0)
                    print("✅ 검색 결과 로딩 완료!")
                else:
                    print("❌ 검색 버튼을 찾을 수 없습니다!")
                    logger.error("Search button not found")
                    raise Exception("검색 버튼 찾기 실패")
            except Exception as e:
                print(f"❌ 검색 실행 실패: {e}")
                logger.error(f"Search execution failed: {e}")
                raise
            
            print("🎉 Work24 통합 필터 적용 완료!")
            print(f"📋 적용된 필터: 연구 및 공학기술 > {selected_count}개 서브카테고리 > 서울 전체")
            if filters.keywords:
                print(f"🔤 추가 키워드: '{filters.keywords}'")
            logger.info(f"Work24 comprehensive filters applied successfully in {time.time() - start_time:.2f}s")
            
        except Exception as e:
            print(f"❌ Work24 통합 필터 적용 실패: {e}")
            logger.error(f"Failed to apply Work24 comprehensive filters: {e}")
            raise
    
    def _apply_keyword_filter(self, keywords: str) -> None:
        """Apply keyword search filter."""
        keyword_selectors = [
            "#keywords",
            "[data-testid='keywords-input']",
            ".jobs-search-box__text-input",
            "input[placeholder*='keyword']",
            "input[placeholder*='title']"
        ]
        
        keyword_input = None
        for selector in keyword_selectors:
            keyword_input = self.crawler.safe_find_element(selector)
            if keyword_input:
                break
        
        if keyword_input:
            logger.debug(f"Applying keyword filter: {keywords}")
            self.crawler.human_behavior.human_click(keyword_input)
            self.crawler.human_behavior.human_type(keyword_input, keywords)
            self.crawler.human_behavior.random_delay(0.5, 1.0)
    
    def _apply_location_filter(self, location: str) -> None:
        """Apply location search filter."""
        location_selectors = [
            "#where",
            "[data-testid='location-input']",
            ".jobs-search-box__text-input[placeholder*='location']",
            "input[placeholder*='location']",
            "input[placeholder*='city']"
        ]
        
        location_input = None
        for selector in location_selectors:
            location_input = self.crawler.safe_find_element(selector)
            if location_input:
                break
        
        if location_input:
            logger.debug(f"Applying location filter: {location}")
            self.crawler.human_behavior.human_click(location_input)
            self.crawler.human_behavior.human_type(location_input, location)
            self.crawler.human_behavior.random_delay(0.5, 1.0)
    
    def _apply_job_type_filter(self, job_type: JobType) -> None:
        """Apply job type filter."""
        if self.crawler.site_name == "linkedin":
            self._apply_linkedin_job_type(job_type)
        elif self.crawler.site_name == "indeed":
            self._apply_indeed_job_type(job_type)
    
    def _apply_linkedin_job_type(self, job_type: JobType) -> None:
        """Apply LinkedIn job type filter."""
        job_type_mapping = {
            JobType.FULL_TIME: "F",
            JobType.PART_TIME: "P",
            JobType.CONTRACT: "C",
            JobType.TEMPORARY: "T",
            JobType.INTERNSHIP: "I"
        }
        
        if job_type in job_type_mapping:
            filter_button = self.crawler.safe_find_element(
                f"input[value='{job_type_mapping[job_type]}']"
            )
            if filter_button:
                self.crawler.human_behavior.human_click(filter_button)
    
    def _apply_indeed_job_type(self, job_type: JobType) -> None:
        """Apply Indeed job type filter."""
        job_type_dropdown = self.crawler.safe_find_element("#job-type-dropdown")
        if job_type_dropdown:
            self.crawler.human_behavior.human_click(job_type_dropdown)
            self.crawler.human_behavior.random_delay(0.5, 1.0)
            
            # Find the appropriate option
            job_type_text = job_type.value.replace("_", " ").title()
            option = self.crawler.safe_find_element(
                f"option[value*='{job_type.value}'], option:contains('{job_type_text}')"
            )
            if option:
                self.crawler.human_behavior.human_click(option)
    
    def _apply_experience_filter(self, experience: ExperienceLevel) -> None:
        """Apply experience level filter."""
        # Implementation varies by site
        if self.crawler.site_name == "linkedin":
            exp_mapping = {
                ExperienceLevel.ENTRY_LEVEL: "1",
                ExperienceLevel.MID_LEVEL: "3",
                ExperienceLevel.SENIOR_LEVEL: "4",
                ExperienceLevel.EXECUTIVE: "5",
                ExperienceLevel.INTERNSHIP: "2"
            }
            
            if experience in exp_mapping:
                exp_filter = self.crawler.safe_find_element(
                    f"input[value='{exp_mapping[experience]}']"
                )
                if exp_filter:
                    self.crawler.human_behavior.human_click(exp_filter)
    
    def _apply_date_filter(self, date_posted: str) -> None:
        """Apply date posted filter."""
        date_selectors = [
            "#date-posted-dropdown",
            ".jobs-search-dropdown[data-control-name='date_posted']"
        ]
        
        for selector in date_selectors:
            date_dropdown = self.crawler.safe_find_element(selector)
            if date_dropdown:
                self.crawler.human_behavior.human_click(date_dropdown)
                self.crawler.human_behavior.random_delay(0.5, 1.0)
                
                # Map date options
                date_option = self.crawler.safe_find_element(
                    f"option[value*='{date_posted}']"
                )
                if date_option:
                    self.crawler.human_behavior.human_click(date_option)
                break
    
    def _apply_remote_filter(self) -> None:
        """Apply remote work filter."""
        remote_selectors = [
            "input[value='remote']",
            "label:contains('Remote')",
            ".filter-pill:contains('Remote')"
        ]
        
        for selector in remote_selectors:
            remote_filter = self.crawler.safe_find_element(selector)
            if remote_filter:
                self.crawler.human_behavior.human_click(remote_filter)
                break
    
    def _submit_search(self) -> None:
        """Submit the search form."""
        search_button_selectors = [
            "button[type='submit']",
            ".jobs-search-form__submit-button",
            "#searchform button",
            ".search-button",
            "[data-testid='search-button']"
        ]
        
        for selector in search_button_selectors:
            search_button = self.crawler.wait_for_clickable(selector)
            if search_button:
                logger.debug("Submitting search")
                self.crawler.human_behavior.human_click(search_button)
                
                # Wait for search results to load
                self.crawler.human_behavior.random_delay(3.0, 6.0)
                return
        
        # If no search button found, try pressing Enter on keyword field
        keyword_input = self.crawler.safe_find_element("#keywords, input[placeholder*='keyword']")
        if keyword_input:
            keyword_input.send_keys("\n")
            self.crawler.human_behavior.random_delay(3.0, 6.0)
    
    def has_next_page(self) -> bool:
        """Check if there's a next page of results."""
        if self.crawler.site_name == "work24":
            return self._has_next_page_work24()
        else:
            # Standard logic for other sites
            next_button = self.crawler.safe_find_element(
                self.site_config["selectors"]["next_page"]
            )
            return next_button is not None and next_button.is_enabled()
    
    def _has_next_page_work24(self) -> bool:
        """Check if Work24 has next page by looking at pagination buttons."""
        try:
            print("🔍 다음 페이지 존재 여부 확인 중...")
            
            # First, check if pagination container exists
            pagination_container = self.crawler.safe_find_element(
                self.site_config["selectors"]["pagination_container"]
            )
            
            if not pagination_container:
                print("❌ 페이지네이션 컨테이너를 찾을 수 없습니다.")
                return False
            
            # Get current page number
            current_page_element = self.crawler.safe_find_element(
                self.site_config["selectors"]["pagination_current"]
            )
            
            if not current_page_element:
                print("⚠️ 현재 페이지 번호를 찾을 수 없습니다.")
                # Try alternative method - check if next button exists
                next_button = self.crawler.safe_find_element(
                    self.site_config["selectors"]["next_page"]
                )
                has_next = next_button is not None and next_button.is_enabled()
                print(f"🔄 대안 방법으로 다음 페이지 존재 여부: {has_next}")
                return has_next
            
            current_page = int(current_page_element.text.strip())
            next_page = current_page + 1
            
            print(f"📄 현재 페이지: {current_page}, 확인할 다음 페이지: {next_page}")
            
            # Method 1: Check if specific next page button exists (most reliable)
            next_page_button = self.crawler.safe_find_element(
                f"button[onclick*='fn_Move({next_page})']"
            )
            
            if next_page_button and next_page_button.is_enabled():
                print(f"✅ 페이지 {next_page} 버튼 발견! 다음 페이지로 이동 가능합니다.")
                return True
            
            # Method 2: Check the general next button
            next_button = self.crawler.safe_find_element(
                self.site_config["selectors"]["next_page"]
            )
            
            if next_button and next_button.is_enabled():
                print(f"✅ 일반 다음 버튼 발견! 다음 페이지로 이동 가능합니다.")
                return True
            
            # Method 3: Look for any numbered page buttons higher than current
            all_page_buttons = self.crawler.safe_find_elements(
                "button[onclick*='fn_Move']"
            )
            
            max_available_page = current_page
            for button in all_page_buttons:
                onclick_attr = button.get_attribute("onclick")
                if onclick_attr:
                    # Extract page number from fn_Move(X)
                    page_match = re.search(r'fn_Move\((\d+)\)', onclick_attr)
                    if page_match:
                        page_num = int(page_match.group(1))
                        max_available_page = max(max_available_page, page_num)
            
            has_more_pages = max_available_page > current_page
            print(f"📊 사용 가능한 최대 페이지: {max_available_page}, 다음 페이지 존재: {has_more_pages}")
            
            return has_more_pages
            
        except Exception as e:
            print(f"⚠️ 다음 페이지 확인 중 오류: {e}")
            logger.warning(f"Error checking next page: {e}")
            return False
    
    def go_to_next_page(self) -> bool:
        """Navigate to the next page of results."""
        try:
            if self.crawler.site_name == "work24":
                return self._go_to_next_page_work24()
            else:
                return self._go_to_next_page_standard()
                
        except Exception as e:
            logger.warning(f"Failed to navigate to next page: {e}")
            return False
    
    def _go_to_next_page_work24(self) -> bool:
        """Navigate to next page for Work24 using fn_Move() function."""
        try:
            # Get current page number
            current_page_element = self.crawler.safe_find_element(
                self.site_config["selectors"]["pagination_current"]
            )
            
            if not current_page_element:
                logger.warning("Could not find current page indicator")
                return False
            
            current_page = int(current_page_element.text.strip())
            next_page = current_page + 1
            
            print(f"📄 페이지 {current_page} → {next_page} 이동 중...")
            
            # Look for the specific next page button
            next_page_button = self.crawler.safe_find_element(
                f"button[onclick*='fn_Move({next_page})']"
            )
            
            if next_page_button:
                # Use JavaScript to execute fn_Move directly for faster navigation
                print(f"🚀 JavaScript로 페이지 {next_page} 이동...")
                self.crawler.driver.execute_script(f"fn_Move({next_page}); return false;")
                
                # Shorter wait for page load (optimized for speed)
                self.crawler.human_behavior.random_delay(2.0, 3.0)
                
                # Verify page change by checking current page indicator
                new_page_element = self.crawler.safe_find_element(
                    self.site_config["selectors"]["pagination_current"]
                )
                
                if new_page_element and int(new_page_element.text.strip()) == next_page:
                    print(f"✅ 페이지 {next_page} 이동 완료!")
                    logger.info(f"Successfully navigated to page {next_page}")
                    return True
                else:
                    print(f"⚠️ 페이지 이동 확인 실패")
                    return False
            else:
                # Check if we can use the general next button
                next_button = self.crawler.safe_find_element(
                    self.site_config["selectors"]["next_page"]
                )
                
                if next_button and next_button.is_enabled():
                    print(f"🔄 일반 다음 버튼으로 페이지 이동...")
                    next_button.click()
                    self.crawler.human_behavior.random_delay(2.0, 3.0)
                    return True
                    
                print(f"❌ 다음 페이지 버튼을 찾을 수 없습니다")
                return False
                
        except Exception as e:
            logger.warning(f"Work24 pagination failed: {e}")
            return False
    
    def _go_to_next_page_standard(self) -> bool:
        """Standard pagination for LinkedIn/Indeed."""
        try:
            next_button = self.crawler.wait_for_clickable(
                self.site_config["selectors"]["next_page"]
            )
            
            if next_button:
                logger.debug("Navigating to next page")
                
                # Scroll to see the next button
                self.crawler.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", next_button
                )
                self.crawler.human_behavior.random_delay(1.0, 2.0)
                
                # Click next page
                self.crawler.human_behavior.human_click(next_button)
                
                # Wait for page to load
                self.crawler.human_behavior.random_delay(3.0, 6.0)
                
                return True
            
            return False
            
        except Exception as e:
            logger.warning(f"Standard pagination failed: {e}")
            return False