"""Job data extraction and processing."""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import structlog
from typing import Optional, List, Dict, Any
import re
from datetime import datetime, timedelta
from decimal import Decimal

from .base_crawler import StealthCrawler
from .models import JobListing, JobType, ExperienceLevel

logger = structlog.get_logger()


class JobExtractor:
    """Extracts detailed job information from job posting pages."""
    
    def __init__(self, crawler: StealthCrawler):
        self.crawler = crawler
        self.site_config = crawler.site_config
        
    def extract_job_listings_from_search(self) -> List[Dict[str, Any]]:
        """Extract basic job information from search results page."""
        print("🔍 페이지에서 채용공고 카드들을 검색 중...")
        job_cards = self.crawler.safe_find_elements(
            self.site_config["selectors"]["job_card"]
        )
        
        if not job_cards:
            print("❌ 채용공고 카드를 찾을 수 없습니다.")
            logger.warning("No job cards found on search results page")
            return []
        
        print(f"✅ {len(job_cards)}개의 채용공고 카드를 발견했습니다!")
        
        jobs = []
        for i, card in enumerate(job_cards):
            try:
                print(f"📝 채용공고 {i+1}/{len(job_cards)} 기본 정보 추출 중...")
                
                # Remove problematic mouse movement that causes "out of bounds" error
                # Just scroll the element into view instead
                try:
                    self.crawler.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
                except Exception:
                    pass  # Ignore scroll errors
                
                # Simple delay instead of mouse movement
                self.crawler.human_behavior.random_delay(0.3, 0.8)
                
                job_data = self._extract_basic_job_info(card)
                if job_data:
                    jobs.append(job_data)
                    self.crawler.session.add_job()
                    print(f"✅ 추출 완료: {job_data.get('title', 'Unknown')}")
                    logger.debug(f"Extracted job {i+1}: {job_data.get('title', 'Unknown')}")
                else:
                    print(f"⚠️ 채용공고 {i+1} 기본 정보 추출 실패")
                
            except Exception as e:
                print(f"❌ 채용공고 {i+1} 추출 실패: {e}")
                logger.warning(f"Failed to extract job {i+1}: {e}")
                self.crawler.session.add_error()
                continue
        
        print(f"📊 총 {len(jobs)}개 채용공고 기본 정보 추출 완료!")
        logger.info(f"Extracted {len(jobs)} jobs from search results")
        return jobs
    
    def _extract_basic_job_info(self, job_card) -> Optional[Dict[str, Any]]:
        """Extract basic information from a job card."""
        try:
            selectors = self.site_config["selectors"]
            
            # Extract title
            title_element = job_card.find_element(By.CSS_SELECTOR, selectors["job_title"])
            title = title_element.text.strip() if title_element else "Unknown"
            
            # Extract company
            company_element = job_card.find_element(By.CSS_SELECTOR, selectors["company_name"])
            company = company_element.text.strip() if company_element else "Unknown"
            
            # Extract location (this may contain mixed data for Work24)
            location_element = job_card.find_element(By.CSS_SELECTOR, selectors["location"])
            raw_location = location_element.text.strip() if location_element else "Unknown"
            
            # Extract job URL
            link_element = job_card.find_element(By.CSS_SELECTOR, selectors["job_link"])
            job_url = link_element.get_attribute("href") if link_element else ""
            
            # Extract job ID from URL or data attributes
            job_id = self._extract_job_id(job_card, job_url)
            
            basic_data = {
                "title": title,
                "company": company,
                "location": raw_location,
                "job_url": job_url,
                "job_id": job_id,
                "source_site": self.crawler.site_name
            }
            
            # For Work24, parse the mixed location data
            if self.crawler.site_name == "work24":
                parsed_data = self._parse_work24_location_data(raw_location)
                # Override location with parsed location
                if parsed_data["location"]:
                    basic_data["location"] = parsed_data["location"]
                # Add other parsed data
                basic_data.update({k: v for k, v in parsed_data.items() 
                                 if k != "location" and v is not None})
            
            return basic_data
            
        except Exception as e:
            logger.warning(f"Failed to extract basic job info: {e}")
            return None
    
    def extract_detailed_job_info(self, job_url: str, basic_info: Dict[str, Any]) -> Optional[JobListing]:
        """Navigate to job page and extract detailed information."""
        try:
            print(f"🔍 상세 페이지 이동: {basic_info['title']}")
            logger.debug(f"Extracting details for: {basic_info['title']}")
            
            # Navigate to job page
            print("🌐 채용공고 상세 페이지로 이동 중...")
            self.crawler.driver.get(job_url)
            self.crawler.human_behavior.random_delay(2.0, 4.0)
            
            # Simulate reading the page
            print("👀 채용공고 내용 읽기 시뮬레이션 중...")
            self.crawler.human_behavior.reading_pause(100)  # Simulate reading job title/summary
            
            # Extract detailed information
            print("📋 상세 정보 추출 중...")
            job_data = self._extract_job_details()
            
            # Merge with basic info
            job_data.update(basic_info)
            
            print("🏗️ 채용공고 데이터 모델 생성 중...")
            # Create JobListing model with proper data handling
            job_listing = JobListing(
                title=job_data.get("title", ""),
                company=job_data.get("company", ""),
                location=job_data.get("location", ""),
                job_url=job_url,
                description=job_data.get("description"),
                requirements=job_data.get("requirements"),
                benefits=job_data.get("benefits"),
                salary_min=job_data.get("salary_min"),
                salary_max=job_data.get("salary_max"),
                salary_currency=job_data.get("salary_currency", "USD"),
                recruiter_name=job_data.get("recruiter_name"),
                recruiter_phone=job_data.get("recruiter_phone"),
                recruiter_email=job_data.get("recruiter_email"),
                job_type=self._parse_job_type(job_data.get("job_type")),
                experience_level=job_data.get("experience_level") or self._parse_experience_level(job_data.get("experience")),
                skills=job_data.get("skills", []),
                technologies=job_data.get("technologies", []),
                posted_date=job_data.get("posted_date"),
                source_site=self.crawler.site_name,
                job_id=job_data.get("job_id"),
                remote_option=job_data.get("remote_option"),
                company_size=job_data.get("company_size"),
                additional_data={
                    "salary_text": job_data.get("salary_text"),
                    "experience": job_data.get("experience"),
                    "education": job_data.get("education"),
                    "work_schedule": job_data.get("work_schedule"),
                    "work_hours": job_data.get("work_hours"),
                    **job_data.get("additional_data", {})
                }
            )
            
            self.crawler.session.complete_job_scrape()
            print(f"✅ 상세 정보 추출 완료: {basic_info['title']}")
            logger.debug(f"Successfully extracted details for: {basic_info['title']}")
            
            return job_listing
            
        except Exception as e:
            print(f"❌ 상세 정보 추출 실패 ({job_url}): {e}")
            logger.error(f"Failed to extract job details from {job_url}: {e}")
            self.crawler.session.add_error()
            return None
    
    def _extract_job_details(self) -> Dict[str, Any]:
        """Extract detailed job information from job page."""
        details = {}
        
        # Site-specific extraction logic
        if self.crawler.site_name == "linkedin":
            details = self._extract_linkedin_details()
        elif self.crawler.site_name == "indeed":
            details = self._extract_indeed_details()
        elif self.crawler.site_name == "work24":
            details = self._extract_work24_details()
        
        return details
    
    def _extract_linkedin_details(self) -> Dict[str, Any]:
        """Extract LinkedIn-specific job details."""
        details = {}
        
        # Job description
        desc_selectors = [
            ".description__text",
            ".jobs-description-content__text",
            ".jobs-description__content"
        ]
        description = self._get_text_from_selectors(desc_selectors)
        if description:
            details["description"] = description
        
        # Company information
        company_selectors = [
            ".jobs-unified-top-card__company-name",
            ".job-details-company-name"
        ]
        company_info = self._get_text_from_selectors(company_selectors)
        
        # Salary information
        salary_selectors = [
            ".jobs-unified-top-card__job-insight",
            ".job-details-salary"
        ]
        salary_text = self._get_text_from_selectors(salary_selectors)
        if salary_text:
            salary_min, salary_max = self._parse_salary(salary_text)
            details["salary_min"] = salary_min
            details["salary_max"] = salary_max
        
        # Job type and experience level
        job_insights = self.crawler.safe_find_elements(
            ".jobs-unified-top-card__job-insight"
        )
        for insight in job_insights:
            text = insight.text.strip().lower()
            if any(jt.value in text for jt in JobType):
                details["job_type"] = text
            if any(exp.value.replace("_", " ") in text for exp in ExperienceLevel):
                details["experience_level"] = text
        
        return details
    
    def _extract_indeed_details(self) -> Dict[str, Any]:
        """Extract Indeed-specific job details."""
        details = {}
        
        # Job description
        desc_selectors = [
            "#jobDescriptionText",
            ".jobsearch-jobDescriptionText",
            ".jobsearch-JobComponent-description"
        ]
        description = self._get_text_from_selectors(desc_selectors)
        if description:
            details["description"] = description
        
        # Salary information
        salary_selectors = [
            ".icl-u-xs-mr--xs .attribute_snippet",
            ".jobsearch-JobMetadataHeader-item"
        ]
        salary_text = self._get_text_from_selectors(salary_selectors)
        if salary_text and "$" in salary_text:
            salary_min, salary_max = self._parse_salary(salary_text)
            details["salary_min"] = salary_min
            details["salary_max"] = salary_max
        
        return details

    def _extract_work24_details(self) -> Dict[str, Any]:
        """Extract Work24-specific job details."""
        details = {}
        
        try:
            print("📋 Work24 상세 정보 추출 중...")
            
            # Extract job description from 직무내용 section
            job_description = self._extract_work24_job_description()
            if job_description:
                details["description"] = job_description
            
            # Extract requirements and qualifications
            requirements = self._extract_work24_requirements()
            if requirements:
                details["requirements"] = requirements
            
            # Extract benefits/welfare information
            benefits = self._extract_work24_benefits()
            if benefits:
                details["benefits"] = benefits
            
            # Extract company information
            company_info = self._extract_work24_company_info()
            details.update(company_info)
            
            # Extract employment details
            employment_details = self._extract_work24_employment_details()
            details.update(employment_details)
            
            # Extract application details
            application_info = self._extract_work24_application_info()
            details.update(application_info)
            
            # Extract contact information by clicking the contact button
            contact_info = self._extract_work24_contact_info()
            details.update(contact_info)
            
            print("✅ Work24 상세 정보 추출 완료")
            
        except Exception as e:
            print(f"⚠️ Work24 상세 정보 추출 중 오류: {e}")
            logger.warning(f"Failed to extract Work24 details: {e}")
        
        return details

    def _extract_work24_contact_info(self) -> Dict[str, Any]:
        """Extract Work24 contact information by clicking the contact button."""
        contact_info = {
            "recruiter_name": None,
            "recruiter_phone": None,
            "recruiter_email": None
        }
        
        try:
            print("📞 채용 담당자 연락처 정보 추출 중...")
            
            # Try multiple approaches to find the contact button
            contact_button = None
            
            # Method 1: Direct onclick attribute selector
            contact_button = self.crawler.safe_find_element("button[onclick*='f_displayEmpChargerInfo']")
            
            # Method 2: XPath with text content (if CSS selector fails)
            if not contact_button:
                try:
                    contact_button = self.crawler.driver.find_element(
                        By.XPATH, "//button[contains(text(), '채용 담당자 개인정보 보기')]"
                    )
                except:
                    pass
            
            # Method 3: Class-based selector
            if not contact_button:
                contact_button = self.crawler.safe_find_element("button.btn.small.type01.fill")
            
            # Method 4: Find all buttons and check text content
            if not contact_button:
                all_buttons = self.crawler.safe_find_elements("button")
                for btn in all_buttons:
                    if "개인정보" in btn.text and "보기" in btn.text:
                        contact_button = btn
                        break
            
            if not contact_button:
                print("⚠️ 채용 담당자 개인정보 보기 버튼을 찾을 수 없습니다. 연락처 정보를 건너뜁니다.")
                return contact_info
            
            print("✅ 채용 담당자 개인정보 버튼 발견!")
            
            # Use JavaScript for faster clicking (speed optimization)
            self.crawler.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", contact_button)
            self.crawler.human_behavior.random_delay(0.3, 0.7)  # Reduced delay
            
            # Click using JavaScript for speed
            self.crawler.driver.execute_script("arguments[0].click();", contact_button)
            print("✅ 채용 담당자 개인정보 보기 버튼 클릭")
            
            # Wait for contact info to load and be revealed
            self.crawler.human_behavior.random_delay(1.5, 2.5)  # Increased wait time
            
            # Debug: Check what elements are available after clicking
            print("🔍 연락처 정보 영역 확인 중...")
            
            # Extract recruiter name - look for pattern like "서울관악고용센터 김태희"
            name_elements = self.crawler.safe_find_elements(".b1_sb")
            print(f"📝 찾은 이름 요소 수: {len(name_elements)}")
            
            for i, element in enumerate(name_elements):
                text = element.text.strip()
                print(f"  이름 요소 {i+1}: '{text}'")
                # Look for Korean names (usually at the end of the text)
                name_match = re.search(r'([가-힣]{2,4})$', text)
                if name_match:
                    contact_info["recruiter_name"] = name_match.group(1)
                    print(f"✅ 담당자명: {contact_info['recruiter_name']}")
                    break
            
            # Extract phone and email using multiple methods
            print("🔍 전화번호 및 이메일 검색 중...")
            
            # Method 1: Look for span elements with phone/email info
            all_spans = self.crawler.safe_find_elements("span")
            print(f"📝 찾은 span 요소 수: {len(all_spans)}")
            
            for i, span in enumerate(all_spans):
                text = span.text.strip()
                if "전화번호" in text:
                    print(f"  전화번호 span {i+1}: '{text}'")
                    phone_match = re.search(r'전화번호\s*([0-9\-\s]+)', text)
                    if phone_match:
                        contact_info["recruiter_phone"] = phone_match.group(1).strip()
                        print(f"✅ 전화번호: {contact_info['recruiter_phone']}")
                    
                if "이메일" in text:
                    print(f"  이메일 span {i+1}: '{text}'")
                    email_match = re.search(r'이메일\s*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', text)
                    if email_match:
                        contact_info["recruiter_email"] = email_match.group(1).strip()
                        print(f"✅ 이메일: {contact_info['recruiter_email']}")
            
            # Method 2: Look in the revealed contact section that appears after clicking
            try:
                # The contact info appears in a specific structure after clicking
                contact_section = self.crawler.safe_find_element(".box_border_type.type_pd24")
                if contact_section:
                    print("🔍 연락처 섹션을 찾았습니다. 내부 검색 중...")
                    section_text = contact_section.text
                    print(f"📝 섹션 전체 텍스트: '{section_text[:200]}...'")
                    
                    # Extract phone from section
                    phone_match = re.search(r'전화번호\s*([0-9\-\s]+)', section_text)
                    if phone_match and not contact_info["recruiter_phone"]:
                        contact_info["recruiter_phone"] = phone_match.group(1).strip()
                        print(f"✅ 섹션에서 전화번호 추출: {contact_info['recruiter_phone']}")
                    
                    # Extract email from section
                    email_match = re.search(r'이메일\s*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', section_text)
                    if email_match and not contact_info["recruiter_email"]:
                        contact_info["recruiter_email"] = email_match.group(1).strip()
                        print(f"✅ 섹션에서 이메일 추출: {contact_info['recruiter_email']}")
                        
            except Exception as section_e:
                print(f"⚠️ 연락처 섹션 검색 실패: {section_e}")
            
            # Final status
            extracted_count = sum([1 for v in contact_info.values() if v])
            print(f"📞 채용 담당자 연락처 정보 추출 완료 ({extracted_count}/3 항목)")
            
        except Exception as e:
            print(f"⚠️ 채용 담당자 연락처 정보 추출 실패: {e}")
            logger.warning(f"Failed to extract Work24 contact info: {e}")
        
        return contact_info

    def _extract_work24_job_description(self) -> Optional[str]:
        """Extract job description from 직무내용 section."""
        try:
            # Look for job description in the 직무내용 section
            description_selectors = [
                ".fold",  # Main content area
                "div:contains('직무내용') + div",
                ".box_border_type .fold"
            ]
            
            for selector in description_selectors:
                element = self.crawler.safe_find_element(selector)
                if element and element.text.strip():
                    text = element.text.strip()
                    # Filter out just the button text
                    if len(text) > 20 and "직무내용" not in text:
                        return text
            
            # Alternative: look for any text containing job-related keywords
            all_text_elements = self.crawler.safe_find_elements("div, p")
            for element in all_text_elements:
                text = element.text.strip()
                if any(keyword in text for keyword in ["Java", "개발", "분석설계", "구현", "시스템"]):
                    if len(text) > 30:
                        return text
                        
        except Exception as e:
            logger.debug(f"Failed to extract job description: {e}")
        
        return None
    
    def _extract_work24_requirements(self) -> Optional[str]:
        """Extract job requirements and qualifications."""
        try:
            requirements = []
            
            # Use XPath instead of :contains() for better compatibility
            # Extract from 지원자격 section
            try:
                qual_elements = self.crawler.driver.find_elements(By.XPATH, "//th[contains(text(), '경력')]/following-sibling::td | //th[contains(text(), '학력')]/following-sibling::td | //th[contains(text(), '자격')]/following-sibling::td")
                for element in qual_elements:
                    text = element.text.strip()
                    if text and text != "-":
                        requirements.append(text)
            except Exception:
                pass
            
            # Extract from 모집요강 table
            table_elements = self.crawler.safe_find_elements(".box_table td")
            for element in table_elements:
                text = element.text.strip()
                if any(keyword in text for keyword in ["경력", "학력", "자격", "필수", "우대"]):
                    if len(text) > 5 and text not in requirements:
                        requirements.append(text)
            
            return " | ".join(requirements) if requirements else None
            
        except Exception as e:
            logger.debug(f"Failed to extract requirements: {e}")
            return None
    
    def _extract_work24_benefits(self) -> Optional[str]:
        """Extract benefits and welfare information."""
        try:
            benefits = []
            
            # Extract from 복리후생 section
            welfare_elements = self.crawler.safe_find_elements(".emp_box_items li:not(.disable) p")
            for element in welfare_elements:
                text = element.text.strip()
                if text and "미제공" not in text:
                    benefits.append(text)
            
            # Extract from 기타 복리후생 using XPath
            try:
                other_benefits = self.crawler.driver.find_element(By.XPATH, "//strong[contains(text(), '기타 복리후생')]/following-sibling::p")
                if other_benefits and other_benefits.text.strip() != "-":
                    benefits.append(other_benefits.text.strip())
            except Exception:
                pass
            
            return ", ".join(benefits) if benefits else None
            
        except Exception as e:
            logger.debug(f"Failed to extract benefits: {e}")
            return None
    
    def _extract_work24_company_info(self) -> Dict[str, Any]:
        """Extract company information."""
        company_info = {}
        
        try:
            # Extract company size using XPath
            try:
                size_element = self.crawler.driver.find_element(By.XPATH, "//em[@class='tit'][contains(text(), '기업규모')]/following-sibling::*")
                if size_element:
                    company_info["company_size"] = size_element.text.strip()
            except Exception:
                pass
            
            # Extract industry using XPath
            try:
                industry_element = self.crawler.driver.find_element(By.XPATH, "//em[@class='tit'][contains(text(), '업종')]/following-sibling::*")
                if industry_element:
                    company_info["industry"] = industry_element.text.strip()
            except Exception:
                pass
            
            # Extract company description/additional info using XPath
            try:
                desc_elements = self.crawler.driver.find_elements(By.XPATH, "//em[@class='tit'][contains(text(), '설립연도') or contains(text(), '연매출액') or contains(text(), '근로자수')]/following-sibling::*")
                company_details = []
                for element in desc_elements:
                    text = element.text.strip()
                    if text:
                        company_details.append(text)
                
                if company_details:
                    company_info["company_description"] = " | ".join(company_details)
            except Exception:
                pass
                
        except Exception as e:
            logger.debug(f"Failed to extract company info: {e}")
        
        return company_info
    
    def _extract_work24_employment_details(self) -> Dict[str, Any]:
        """Extract employment type and work conditions."""
        employment_info = {}
        
        try:
            # Extract job type (고용형태) using XPath
            try:
                job_type_element = self.crawler.driver.find_element(By.XPATH, "//th[contains(text(), '고용 형태')]/following-sibling::td")
                if job_type_element:
                    job_type_text = job_type_element.text.strip()
                    employment_info["job_type_korean"] = job_type_text
                    
                    # Map to English enum if needed
                    if "기간의 정함이 없는" in job_type_text:
                        employment_info["job_type"] = "정규직"
            except Exception:
                pass
            
            # Extract work schedule details using XPath
            try:
                schedule_elements = self.crawler.driver.find_elements(By.XPATH, "//th[contains(text(), '근무 시간') or contains(text(), '근무 형태')]/following-sibling::td")
                schedule_details = []
                for element in schedule_elements:
                    text = element.text.strip()
                    if text:
                        schedule_details.append(text)
                
                if schedule_details:
                    employment_info["work_schedule_details"] = " | ".join(schedule_details)
            except Exception:
                pass
                
        except Exception as e:
            logger.debug(f"Failed to extract employment details: {e}")
        
        return employment_info
    
    def _extract_work24_application_info(self) -> Dict[str, Any]:
        """Extract application deadline and method information."""
        app_info = {}
        
        try:
            # Extract application deadline using XPath
            try:
                deadline_element = self.crawler.driver.find_element(By.XPATH, "//*[@class='cl-red'][contains(text(), '채용시까지') or contains(text(), '마감일')]")
                if deadline_element:
                    app_info["application_deadline_text"] = deadline_element.text.strip()
            except Exception:
                pass
            
            # Extract application method using XPath
            try:
                method_element = self.crawler.driver.find_element(By.XPATH, "//strong[contains(text(), '접수 방법')]/following-sibling::p")
                if method_element:
                    app_info["application_method"] = method_element.text.strip()
            except Exception:
                pass
            
            # Extract required documents using XPath
            try:
                docs_element = self.crawler.driver.find_element(By.XPATH, "//strong[contains(text(), '제출 서류')]/following-sibling::p")
                if docs_element:
                    app_info["required_documents"] = docs_element.text.strip()
            except Exception:
                pass
                
        except Exception as e:
            logger.debug(f"Failed to extract application info: {e}")
        
        return app_info
    
    def _parse_work24_location_data(self, location_text: str) -> Dict[str, Any]:
        """Parse Work24 location data that contains mixed information."""
        parsed_data = {
            "location": None,
            "salary_text": None,
            "experience": None,
            "education": None,
            "work_schedule": None,
            "work_hours": None
        }
        
        if not location_text:
            return parsed_data
        
        # Split by newlines and process each line
        lines = [line.strip() for line in location_text.split('\n') if line.strip()]
        
        location_parts = []
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
                
            # Extract salary information (연봉 pattern)
            if '연봉' in line or '만원' in line:
                parsed_data["salary_text"] = line
                # Try to extract salary range
                salary_match = re.search(r'연봉\s*(\d+(?:,\d+)?)\s*만원\s*~\s*(\d+(?:,\d+)?)\s*만원', line)
                if salary_match:
                    try:
                        min_sal = Decimal(salary_match.group(1).replace(',', '')) * 10000
                        max_sal = Decimal(salary_match.group(2).replace(',', '')) * 10000
                        parsed_data["salary_min"] = min_sal
                        parsed_data["salary_max"] = max_sal
                        parsed_data["salary_currency"] = "KRW"
                    except:
                        pass
                continue
                
            # Extract experience level (경력 pattern)
            if '경력' in line:
                parsed_data["experience"] = line
                # Try to extract years of experience
                exp_match = re.search(r'경력(\d+)년', line)
                if exp_match:
                    years = int(exp_match.group(1))
                    if years <= 2:
                        parsed_data["experience_level"] = ExperienceLevel.ENTRY_LEVEL
                    elif years <= 5:
                        parsed_data["experience_level"] = ExperienceLevel.MID_LEVEL
                    else:
                        parsed_data["experience_level"] = ExperienceLevel.SENIOR_LEVEL
                continue
                
            # Extract education requirement (학력 pattern)
            if '학력' in line:
                parsed_data["education"] = line
                continue
                
            # Extract work schedule (주X일 pattern)
            if '주' in line and ('일' in line or '시간' in line):
                if not parsed_data["work_schedule"]:
                    parsed_data["work_schedule"] = line
                else:
                    parsed_data["work_schedule"] += f" {line}"
                continue
                
            # Extract work hours (시간 pattern like 09:00 ~ 18:00)
            if ':' in line and ('~' in line or '-' in line):
                parsed_data["work_hours"] = line
                continue
                
            # Everything else is likely location information
            # Location patterns: 서울, 경기도, addresses with 구, 로, 길 etc.
            location_keywords = ['서울', '경기', '인천', '부산', '대구', '대전', '광주', '울산', '세종',
                               '구', '로', '길', '동', '면', '읍', '시', '도', '특별시', '광역시']
            
            if any(keyword in line for keyword in location_keywords):
                location_parts.append(line)
        
        # Combine location parts
        if location_parts:
            parsed_data["location"] = ' '.join(location_parts)
        
        return parsed_data
    
    def _get_text_from_selectors(self, selectors: List[str]) -> Optional[str]:
        """Try multiple selectors to get text content."""
        for selector in selectors:
            element = self.crawler.safe_find_element(selector)
            if element:
                text = element.text.strip()
                if text:
                    return text
        return None
    
    def _extract_job_id(self, job_card, job_url: str) -> Optional[str]:
        """Extract job ID from card or URL."""
        # Try data attributes first
        for attr in ["data-jk", "data-job-id", "data-id"]:
            job_id = job_card.get_attribute(attr)
            if job_id:
                return job_id
        
        # Extract from URL
        if job_url:
            # LinkedIn: /jobs/view/{job_id}
            linkedin_match = re.search(r"/jobs/view/(\d+)", job_url)
            if linkedin_match:
                return linkedin_match.group(1)
            
            # Indeed: viewjob?jk={job_id}
            indeed_match = re.search(r"viewjob\?jk=([a-f0-9]+)", job_url)
            if indeed_match:
                return indeed_match.group(1)
        
        return None
    
    def _parse_salary(self, salary_text: str) -> tuple[Optional[Decimal], Optional[Decimal]]:
        """Parse salary information from text."""
        try:
            # Remove common prefixes/suffixes
            salary_text = re.sub(r"[^\d\.,k-]", "", salary_text.lower())
            
            # Handle ranges like "50k-80k" or "$50,000-$80,000"
            range_match = re.search(r"(\d+(?:,\d{3})*(?:\.\d{2})?)\s*[k]?\s*-\s*(\d+(?:,\d{3})*(?:\.\d{2})?)\s*[k]?", salary_text)
            if range_match:
                min_sal = self._convert_salary_to_decimal(range_match.group(1))
                max_sal = self._convert_salary_to_decimal(range_match.group(2))
                return min_sal, max_sal
            
            # Handle single values
            single_match = re.search(r"(\d+(?:,\d{3})*(?:\.\d{2})?)\s*[k]?", salary_text)
            if single_match:
                salary = self._convert_salary_to_decimal(single_match.group(1))
                return salary, salary
            
        except Exception as e:
            logger.debug(f"Failed to parse salary '{salary_text}': {e}")
        
        return None, None
    
    def _convert_salary_to_decimal(self, salary_str: str) -> Optional[Decimal]:
        """Convert salary string to Decimal."""
        try:
            # Remove commas
            salary_str = salary_str.replace(",", "")
            
            # Handle 'k' suffix
            if salary_str.endswith("k"):
                return Decimal(salary_str[:-1]) * 1000
            
            return Decimal(salary_str)
        except Exception:
            return None
    
    def _parse_job_type(self, job_type_text: Optional[str]) -> Optional[JobType]:
        """Parse job type from text."""
        if not job_type_text:
            return None
        
        job_type_text = job_type_text.lower()
        
        type_mappings = {
            "full time": JobType.FULL_TIME,
            "full-time": JobType.FULL_TIME,
            "part time": JobType.PART_TIME,
            "part-time": JobType.PART_TIME,
            "contract": JobType.CONTRACT,
            "temporary": JobType.TEMPORARY,
            "internship": JobType.INTERNSHIP,
            "freelance": JobType.FREELANCE,
        }
        
        for key, job_type in type_mappings.items():
            if key in job_type_text:
                return job_type
        
        return None
    
    def _parse_experience_level(self, exp_text: Optional[str]) -> Optional[ExperienceLevel]:
        """Parse experience level from text."""
        if not exp_text:
            return None
        
        exp_text = exp_text.lower()
        
        exp_mappings = {
            "entry": ExperienceLevel.ENTRY_LEVEL,
            "junior": ExperienceLevel.ENTRY_LEVEL,
            "mid": ExperienceLevel.MID_LEVEL,
            "senior": ExperienceLevel.SENIOR_LEVEL,
            "executive": ExperienceLevel.EXECUTIVE,
            "director": ExperienceLevel.EXECUTIVE,
            "intern": ExperienceLevel.INTERNSHIP,
        }
        
        for key, exp_level in exp_mappings.items():
            if key in exp_text:
                return exp_level
        
        return None