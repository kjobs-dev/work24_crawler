"""Test script for Work24 crawler with hardcoded values."""

import structlog
import sys
from pathlib import Path

from src.crawler.main_crawler import JobCrawler
from src.crawler.core.models import SearchFilters, JobType, ExperienceLevel

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="ISO"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()


def main():
    """Test crawler with Work24 site."""
    try:
        logger.info("Starting Work24 job crawler test")
        
        # Test configuration
        site_name = "work24"
        username = "ckm5430"
        password = "password"
        max_jobs = 5  # Small test
        
        print(f"Testing Work24 crawler:")
        print(f"- Site: {site_name}")
        print(f"- Username: {username}")
        print(f"- Max jobs: {max_jobs}")
        
        # Define search criteria
        search_filters = SearchFilters(
            keywords="developer",
            location="Seoul, Korea",
            job_type=JobType.FULL_TIME,
            experience_level=ExperienceLevel.MID_LEVEL,
            date_posted="7d",
            remote_only=False,
            max_results=max_jobs
        )
        
        # Initialize crawler with credentials
        crawler = JobCrawler(site_name, (username, password))
        
        # Start crawling
        excel_file = crawler.crawl_jobs(search_filters)
        
        if excel_file:
            logger.info(f"Crawling completed successfully. Results saved to: {excel_file}")
            
            # Print session statistics
            stats = crawler.get_session_stats()
            print("\n" + "="*50)
            print("CRAWLING SUMMARY")
            print("="*50)
            print(f"Jobs found: {stats['jobs_found']}")
            print(f"Unique companies: {stats['unique_companies']}")
            print(f"Site crawled: {stats['site_crawled']}")
            print(f"Top locations: {', '.join(stats['locations'][:5])}")
            print(f"Excel file: {excel_file}")
            print("="*50)
        else:
            logger.error("Crawling failed")
            sys.exit(1)
            
    except KeyboardInterrupt:
        logger.info("Crawling interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Application failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()