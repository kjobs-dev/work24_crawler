"""Data models for job crawler."""

from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime
from typing import Optional, List, Dict, Any
from decimal import Decimal
from enum import Enum


class JobType(str, Enum):
    """Job type enumeration."""
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    TEMPORARY = "temporary"
    INTERNSHIP = "internship"
    FREELANCE = "freelance"


class ExperienceLevel(str, Enum):
    """Experience level enumeration."""
    ENTRY_LEVEL = "entry_level"
    MID_LEVEL = "mid_level"
    SENIOR_LEVEL = "senior_level"
    EXECUTIVE = "executive"
    INTERNSHIP = "internship"


class JobListing(BaseModel):
    """Job listing data model."""
    
    # Basic Information
    title: str = Field(..., min_length=1, max_length=500)
    company: str = Field(..., min_length=1, max_length=255)
    location: str = Field(..., min_length=1, max_length=255)
    job_url: str
    
    # Detailed Information
    description: Optional[str] = None
    requirements: Optional[str] = None
    benefits: Optional[str] = None
    salary_min: Optional[Decimal] = None
    salary_max: Optional[Decimal] = None
    salary_currency: Optional[str] = "USD"
    
    # Contact Information
    recruiter_name: Optional[str] = None
    recruiter_phone: Optional[str] = None
    recruiter_email: Optional[str] = None
    
    # Categorization
    job_type: Optional[JobType] = None
    experience_level: Optional[ExperienceLevel] = None
    department: Optional[str] = None
    industry: Optional[str] = None
    
    # Skills and Technologies
    skills: List[str] = Field(default_factory=list)
    technologies: List[str] = Field(default_factory=list)
    
    # Metadata
    posted_date: Optional[datetime] = None
    application_deadline: Optional[datetime] = None
    scraped_at: datetime = Field(default_factory=datetime.now)
    source_site: str
    job_id: Optional[str] = None
    
    # Additional Data
    remote_option: Optional[bool] = None
    company_size: Optional[str] = None
    company_description: Optional[str] = None
    additional_data: Dict[str, Any] = Field(default_factory=dict)


class SearchFilters(BaseModel):
    """Search filters for job crawling."""
    
    keywords: Optional[str] = None
    location: Optional[str] = None
    job_type: Optional[JobType] = None
    experience_level: Optional[ExperienceLevel] = None
    salary_min: Optional[Decimal] = None
    date_posted: Optional[str] = None  # "24h", "3d", "7d", "14d", "30d"
    remote_only: bool = False
    company_name: Optional[str] = None
    
    # Advanced filters
    exclude_companies: List[str] = Field(default_factory=list)
    required_skills: List[str] = Field(default_factory=list)
    max_results: int = Field(default=100, ge=1, le=1000)


class CrawlerSession(BaseModel):
    """Crawler session information."""
    
    session_id: str
    site_name: str
    started_at: datetime = Field(default_factory=datetime.now)
    filters: SearchFilters
    jobs_found: int = 0
    jobs_scraped: int = 0
    errors_count: int = 0
    status: str = "active"  # active, completed, failed, paused
    
    def add_job(self) -> None:
        """Increment jobs found counter."""
        self.jobs_found += 1
    
    def complete_job_scrape(self) -> None:
        """Increment jobs scraped counter."""
        self.jobs_scraped += 1
    
    def add_error(self) -> None:
        """Increment error counter."""
        self.errors_count += 1