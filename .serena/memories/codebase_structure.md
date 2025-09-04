# Codebase Structure

## Directory Layout
```
src/crawler/
├── __init__.py
├── main_crawler.py          # Main orchestrator - coordinates entire crawl process

├── core/                    # Core crawler functionality
│   ├── __init__.py
│   ├── base_crawler.py      # StealthCrawler - undetected Chrome setup & stealth features
│   ├── auth.py             # AuthenticationManager - handles login for different sites
│   ├── search_engine.py    # SearchEngine - applies filters and navigates search pages
│   ├── job_extractor.py    # JobExtractor - extracts job data from listings and detail pages
│   ├── config.py           # Settings (CrawlerSettings) and site configs (JobSiteConfig)
│   └── models.py           # Pydantic models: JobListing, SearchFilters, CrawlerSession

├── utils/                  # Utility modules
│   ├── __init__.py
│   ├── human_behavior.py   # HumanBehaviorSimulator - anti-detection behaviors
│   └── excel_exporter.py   # ExcelExporter - exports jobs to formatted Excel files

└── sites/                  # Site-specific implementations (future extensibility)
    └── __init__.py

output/                     # Generated Excel files
logs/                      # Log files
.env                       # Environment variables (credentials, settings)
```

## Key Files and Their Purposes
- **src/main.py**: Entry point that configures and runs the crawler
- **src/crawler/main_crawler.py**: `JobCrawler` class - main orchestrator
- **src/crawler/core/models.py**: Core data models (`JobListing`, `SearchFilters`, `CrawlerSession`)
- **src/crawler/core/config.py**: Settings management and site configurations
- **pyproject.toml**: Dependencies, tools configuration (ruff, mypy, pytest)
- **.env**: Environment variables for credentials and settings
- **CLAUDE.md**: Comprehensive development guidelines and project instructions