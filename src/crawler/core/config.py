"""Configuration management for the job crawler."""

from pydantic_settings import BaseSettings
from pydantic import Field
from pathlib import Path
from functools import lru_cache
from typing import Dict, Any


class CrawlerSettings(BaseSettings):
    """Application settings with validation."""
    
    # Job Site Credentials
    linkedin_email: str = ""
    linkedin_password: str = ""
    indeed_email: str = ""
    indeed_password: str = ""
    work24_email: str = ""
    work24_password: str = ""
    
    # Crawler Behavior Settings
    crawl_delay_min: int = Field(default=2, ge=1, le=10)
    crawl_delay_max: int = Field(default=5, ge=2, le=20)
    page_load_timeout: int = Field(default=8, ge=3, le=60)
    implicit_wait: int = Field(default=0, ge=0, le=10)
    
    # Output Settings
    output_dir: Path = Field(default=Path("./output"))
    excel_filename: str = "job_listings_{timestamp}.xlsx"
    
    # Batch Saving Settings
    batch_save_size: int = Field(default=10, ge=1, le=50, description="Number of jobs to save per batch")
    
    # Browser Settings
    headless: bool = False
    window_width: int = Field(default=1920, ge=800)
    window_height: int = Field(default=1080, ge=600)
    
    # Anti-Detection Settings
    user_agent_rotation: bool = True
    viewport_randomization: bool = True
    mouse_movement_simulation: bool = True
    typing_delay_enabled: bool = True
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache()
def get_settings() -> CrawlerSettings:
    """Get cached settings instance."""
    return CrawlerSettings()


class JobSiteConfig:
    """Configuration for different job sites."""
    
    SITES: Dict[str, Dict[str, Any]] = {
        "linkedin": {
            "base_url": "https://www.linkedin.com",
            "login_url": "https://www.linkedin.com/login",
            "jobs_url": "https://www.linkedin.com/jobs/search",
            "selectors": {
                "email_input": "#username",
                "password_input": "#password",
                "login_button": "[type='submit']",
                "job_card": ".job-search-card",
                "job_title": ".job-search-card__title",
                "company_name": ".job-search-card__subtitle",
                "location": ".job-search-card__location",
                "job_link": ".job-search-card__title a",
                "next_page": "[aria-label='Next']",
                "filters": {
                    "location": "#locationFacet",
                    "experience": "#f_E",
                    "job_type": "#f_JT",
                    "date_posted": "#f_TPR"
                }
            }
        },
        "indeed": {
            "base_url": "https://www.indeed.com",
            "login_url": "https://secure.indeed.com/account/login",
            "jobs_url": "https://www.indeed.com/jobs",
            "selectors": {
                "email_input": "#ifl-InputFormField-3",
                "password_input": "#ifl-InputFormField-4",
                "login_button": "#login-submit-button",
                "job_card": "[data-jk]",
                "job_title": "[data-testid='job-title']",
                "company_name": "[data-testid='company-name']",
                "location": "[data-testid='job-location']",
                "job_link": "[data-testid='job-title'] a",
                "next_page": "[aria-label='Next Page']",
                "filters": {
                    "location": "#where",
                    "salary": "#salary-guide-dropdown",
                    "job_type": "#job-type-dropdown",
                    "date_posted": "#date-posted-dropdown"
                }
            }
        },
        "work24": {
            "base_url": "https://www.work24.go.kr",
            "login_url": "https://www.work24.go.kr/cm/z/b/0210/openLginPageForAnyId.do",
            "jobs_url": "https://www.work24.go.kr/wk/a/b/1200/retriveDtlEmpSrchList.do",
            "force_desktop": True,
            "selectors": {
                "login_trigger": "#btnIdPopup",  # ID/Password login button
                "email_input": "#id",
                "password_input": "#pwd", 
                "login_button": "#btnIndvIdLogin",  # Actual login button ID
                "success_alert_ok": "button",  # OK button on success alert
                "job_card": "table#contentArea tbody tr",
                "job_title": "a.t3_sb.underline_hover",
                "company_name": "a.cp_name.underline_hover",
                "location": "td:nth-child(2)",
                "job_link": "a.t3_sb.underline_hover",
                "next_page": "button.btn_page.next",
                "pagination_container": ".box_pagination",
                "pagination_current": "button.active[aria-current='true']",
                "search_keyword": "#srcKeyword",
                "detail_company_name": "a.cp_name.underline_hover",
                "detail_job_title": "a.t3_sb.underline_hover",
                "detail_company_address": "th:contains('근무 예정지') + td",
                "detail_contact_info": "text:contains('지원문의')",
                # Contact information selectors
                "contact_button": "button[onclick*='f_displayEmpChargerInfo']",
                "contact_name": ".b1_sb",
                "contact_phone": "span:contains('전화번호') + *",
                "contact_email": "span:contains('이메일') + *",
                "contact_phone_text": "span.item.fs-16:contains('전화번호')",
                "contact_email_text": "span.item.fs-16:contains('이메일')",
                "filters": {
                    "keywords": "#srcKeyword",
                    # Category expansion button
                    "category_button": "button[onclick=\"fn_show('jobCategory');\"]",
                    # Main category - 연구 및 공학기술
                    "job_category_main": "#chk02",
                    "job_category_main_button": "#btnjobName02",  # Button to expand sub-categories
                    # Sub categories (all tech-related under 연구 및 공학기술)
                    "sub_categories": {
                        "network_security": "#chk025",      # 네트워크 시스템 및 정보보안
                        "data_web": "#chk026",              # 데이터 및 정보시스템·웹 운영
                        "software": "#chk024",              # 소프트웨어
                        "computer_system": "#chk023",       # 컴퓨터시스템
                        "hardware_telecom": "#chk022",      # 컴퓨터하드웨어·통신공학
                        "broadcast": "#chk027"              # 통신·방송 송출
                    },
                    # Region selection
                    "area_button": "button[onclick=\"fn_show('jobCatelocation01', 'jobCatelocation02');\"]",
                    "seoul_region": "#regionOn_11000 button",
                    "seoul_whole": "#subRegion-1",           # 전체 서울 선택
                    "search_button": "button[onclick=\"fn_Search('1');\"]"
                }
            }
        }
    }
    
    @classmethod
    def get_site_config(cls, site_name: str) -> Dict[str, Any]:
        """Get configuration for a specific job site."""
        if site_name not in cls.SITES:
            raise ValueError(f"Unsupported site: {site_name}")
        return cls.SITES[site_name]