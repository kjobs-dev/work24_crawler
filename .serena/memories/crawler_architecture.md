# Crawler Architecture and Key Components

## Main Classes and Responsibilities

### JobCrawler (src/crawler/main_crawler.py)
- **Main orchestrator** that coordinates the entire crawl process
- Methods: `__init__`, `crawl_jobs`, `_crawl_all_pages`, `get_session_stats`
- Manages the crawling session from start to finish

### Core Components (src/crawler/core/)

#### CrawlerSettings (config.py)
- **Pydantic settings model** with environment variable support
- Manages credentials, crawler behavior, output settings, browser settings
- Anti-detection configuration (user agent rotation, viewport randomization)

#### JobListing (models.py)
- **Comprehensive data model** for job postings
- Fields: title, company, location, description, requirements, benefits
- Salary information, categorization, skills/technologies
- Metadata: posted_date, scraped_at, source_site, job_id

#### Other Core Models (models.py)
- `JobType`: Enum for job types (FULL_TIME, PART_TIME, CONTRACT, etc.)
- `ExperienceLevel`: Enum for experience levels (ENTRY, MID, SENIOR, etc.)
- `SearchFilters`: Model for search criteria and filters
- `CrawlerSession`: Model for tracking crawl session data

### Utility Components (src/crawler/utils/)
- **HumanBehaviorSimulator** (human_behavior.py): Anti-detection behaviors
- **ExcelExporter** (excel_exporter.py): Professional Excel report generation

### Core Modules (src/crawler/core/)
- **base_crawler.py**: StealthCrawler with undetected Chrome setup
- **auth.py**: AuthenticationManager for site-specific login handling
- **search_engine.py**: SearchEngine for filter application and navigation  
- **job_extractor.py**: JobExtractor for data extraction from job pages

## Site Configuration
- Multi-site support through `JobSiteConfig` class
- Site-specific selectors and URLs stored in configuration
- Currently supports LinkedIn and Indeed with extensible architecture

## Anti-Detection Strategy
- Undetected ChromeDriver for stealth browsing
- Human-like delays (2-5 seconds between actions)
- Mouse movement simulation and random behaviors
- User agent rotation and viewport randomization
- Content-based reading pauses and typing simulation