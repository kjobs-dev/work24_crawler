"""Main entry point for the job crawler application."""

import structlog
import sys
from pathlib import Path
from typing import Optional
import getpass

from crawler.main_crawler import JobCrawler
from crawler.core.models import SearchFilters, JobType, ExperienceLevel
from crawler.core.config import get_settings

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


def get_user_credentials(site_name: str) -> tuple[str, str]:
    """Get credentials from user input."""
    print(f"\n🔑 {site_name.upper()} 계정 정보를 입력하세요:")
    username = input(f"{site_name.upper()} 아이디/이메일: ").strip()
    password = getpass.getpass(f"{site_name.upper()} 비밀번호: ").strip()
    print("✅ 계정 정보 입력 완료!")
    return username, password


def get_output_directory() -> Path:
    """Get output directory from user input with cross-platform compatibility."""
    import os
    
    print("\n📁 Excel 파일 저장 경로를 설정하세요:")
    print("💡 팁: 경로 예시:")
    print("   Windows: C:\\Users\\사용자명\\Desktop\\채용공고")
    print("   Mac/Linux: /Users/사용자명/Desktop/채용공고 또는 ~/Desktop/채용공고")
    print("   현재 폴더: . (점 하나)")
    
    while True:
        try:
            user_path = input("\n📂 저장 경로를 입력하세요 (엔터 = 현재 폴더의 output): ").strip()
            
            # Default to current directory's output folder
            if not user_path:
                output_dir = Path.cwd() / "output"
                print(f"✅ 기본 경로 사용: {output_dir.absolute()}")
            else:
                # Expand user path (handles ~ on Mac/Linux)
                expanded_path = os.path.expanduser(user_path)
                output_dir = Path(expanded_path).resolve()
                print(f"✅ 설정된 경로: {output_dir.absolute()}")
            
            # Create directory if it doesn't exist
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Test write permissions
            test_file = output_dir / "test_write_permission.tmp"
            try:
                test_file.write_text("test")
                test_file.unlink()  # Delete test file
                print(f"✅ 경로 확인 완료! 파일 저장 가능합니다.")
                return output_dir
            except PermissionError:
                print(f"❌ 권한 오류: '{output_dir}' 경로에 파일을 저장할 수 없습니다.")
                print("   다른 경로를 선택하거나 폴더 권한을 확인해주세요.")
            except Exception as e:
                print(f"❌ 경로 오류: {e}")
                
        except Exception as e:
            print(f"❌ 잘못된 경로입니다: {e}")
            print("   올바른 경로를 입력해주세요.")
        
        print("🔄 다시 시도해주세요...")


def main():
    """Main entry point for the crawler."""
    try:
        logger.info("Starting job crawler application")
        print("안녕하세요! 오늘도 좋은 하루 되세요~ 산자 드림~")
        # Get site selection from user
        print("🌐 사용 가능한 채용 사이트:")
        print("1. LinkedIn(Coming Soon)")
        print("2. Indeed(Coming Soon)")
        print("3. Work24 (고용24)")
        
        while True:
            choice = input("\n사이트를 선택하세요 (1-3): ").strip()
            if choice == "1":
                site_name = "linkedin"
                print("✅ LinkedIn 선택됨")
                break
            elif choice == "2":
                site_name = "indeed"
                print("✅ Indeed 선택됨")
                break
            elif choice == "3":
                site_name = "work24"
                print("✅ Work24 선택됨")
                break
            else:
                print("❌ 잘못된 선택입니다. 1, 2, 3 중에서 선택해주세요.")
        
        # Get credentials from user
        username, password = get_user_credentials(site_name)
        
        # Get output directory from user
        output_directory = get_output_directory()
        
        # Get search keywords from user (optional)
        keywords = input("\n🔍 검색 키워드를 입력하세요 (선택사항, 엔터=키워드 없이 검색): ").strip()
        if keywords:
            print(f"✅ 키워드 설정: '{keywords}'")
        else:
            print("✅ 키워드 없이 카테고리 기반 검색을 진행합니다.")
        
        # Get number of jobs from user
        while True:
            try:
                max_jobs = int(input("\n📊 수집할 채용공고 수를 입력하세요 (1-1000): ").strip())
                if 1 <= max_jobs <= 1000:
                    print(f"✅ 수집 목표: {max_jobs}개")
                    break
                else:
                    print("❌ 1과 1000 사이의 숫자를 입력해주세요.")
            except ValueError:
                print("❌ 올바른 숫자를 입력해주세요.")
        
        # Define search criteria
        search_filters = SearchFilters(
            keywords=keywords if keywords else None,
            location="Seoul, Korea" if site_name == "work24" else "New York, NY",
            job_type=JobType.FULL_TIME,
            experience_level=ExperienceLevel.MID_LEVEL,
            date_posted="7d",  # Last 7 days
            remote_only=False,
            max_results=max_jobs
        )
        
        # Initialize crawler with user credentials and output directory
        crawler = JobCrawler(site_name, (username, password), output_directory)
        
        # Start crawling
        excel_file = crawler.crawl_jobs(search_filters)
        
        if excel_file:
            logger.info(f"Crawling completed successfully. Results saved to: {excel_file}")
            
            # Print session statistics
            stats = crawler.get_session_stats()
            print("\n" + "="*50)
            print("📊 크롤링 완료 요약")
            print("="*50)
            print(f"📋 수집된 채용공고: {stats['jobs_found']}개")
            print(f"🏢 고유 회사 수: {stats['unique_companies']}개")
            print(f"🌐 크롤링 사이트: {stats['site_crawled']}")
            print(f"📍 주요 지역: {', '.join(stats['locations'][:5])}")
            print(f"📄 Excel 파일: {excel_file}")
            print("="*50)
            print("🎉 크롤링이 성공적으로 완료되었습니다!")
        else:
            print("❌ 크롤링 실패")
            logger.error("Crawling failed")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n⏹️ 사용자에 의해 크롤링이 중단되었습니다.")
        logger.info("Crawling interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 애플리케이션 오류: {e}")
        logger.error(f"Application failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()