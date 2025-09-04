# Project Overview

## Purpose
Selenium-based job crawler designed to scrape job postings from major job sites (LinkedIn, Indeed) while mimicking human behavior to avoid detection. The crawler logs in, applies filters, searches for jobs, extracts detailed information, and exports results to Excel.

## Tech Stack
- **Python 3.11+** as primary language
- **Selenium 4.15+** for web automation
- **Undetected ChromeDriver 3.5+** for stealth browsing
- **Pydantic 2.5+** for data validation and settings management
- **Pandas 2.1+** and **OpenPyXL 3.1+** for Excel export
- **UV** for blazing-fast package management
- **Structlog** for structured logging
- **Rich** for terminal formatting

## Core Features
- Stealth crawling with anti-detection measures
- Human behavior simulation (delays, mouse movements, typing patterns)
- Multi-site support (LinkedIn, Indeed, extensible architecture)
- Smart authentication with popup/banner handling
- Advanced filtering (job type, location, experience, salary, date)
- Detailed data extraction (descriptions, requirements, benefits, skills)
- Professional Excel export with statistics and formatting

## Key Architecture Components
- `JobCrawler`: Main orchestrator coordinating the entire crawl process
- `StealthCrawler`: Undetected Chrome setup with anti-detection features
- `AuthenticationManager`: Site-specific login handling
- `SearchEngine`: Filter application and search navigation
- `JobExtractor`: Data extraction from job listings and detail pages
- `HumanBehaviorSimulator`: Anti-detection behavior patterns
- `ExcelExporter`: Professional Excel report generation