"""Base crawler with stealth capabilities and human-like behavior."""

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from fake_useragent import UserAgent
import random
import structlog
from typing import Optional, List, Dict, Any
from pathlib import Path

from ..utils.human_behavior import HumanBehaviorSimulator
from .config import get_settings, JobSiteConfig
from .models import CrawlerSession, SearchFilters

logger = structlog.get_logger()


class StealthCrawler:
    """Base crawler with anti-detection capabilities."""
    
    def __init__(self, site_name: str, session_filters: SearchFilters):
        self.settings = get_settings()
        self.site_name = site_name
        self.site_config = JobSiteConfig.get_site_config(site_name)
        self.driver: Optional[uc.Chrome] = None
        self.wait: Optional[WebDriverWait] = None
        self.human_behavior: Optional[HumanBehaviorSimulator] = None
        self.session = CrawlerSession(
            session_id=f"{site_name}_{int(random.random() * 1000000)}",
            site_name=site_name,
            filters=session_filters
        )

    def _get_chrome_version(self) -> Optional[int]:
        """Get the installed Chrome version."""
        try:
            import subprocess
            import re
            
            # Try multiple ways to get Chrome version
            commands = [
                ['google-chrome', '--version'],
                ['google-chrome-stable', '--version'],
                ['chromium-browser', '--version'],
                ['chromium', '--version']
            ]
            
            for cmd in commands:
                try:
                    output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, text=True)
                    # Extract version number (e.g., "Google Chrome 140.0.7339.80" -> 140)
                    version_match = re.search(r'(\d+)\.', output)
                    if version_match:
                        version = int(version_match.group(1))
                        print(f"🔍 감지된 Chrome 버전: {version}")
                        return version
                except:
                    continue
            
            print("⚠️ Chrome 버전을 감지할 수 없습니다.")
            return None
            
        except Exception as e:
            print(f"❌ Chrome 버전 감지 중 오류: {e}")
            return None
        
    def _setup_chrome_options(self) -> Options:
        """Configure Chrome options for stealth browsing."""
        options = Options()
        
        if self.settings.headless:
            options.add_argument("--headless=new")
        
        # Anti-detection arguments
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        # Updated anti-detection for newer Chrome versions
        options.add_argument("--disable-extensions-except")
        options.add_argument("--disable-extensions-file-access-check")
        options.add_argument("--disable-automation")
        options.add_argument("--disable-infobars")
        
        # Force desktop user agent for sites that need it
        if self.site_config.get("force_desktop", False):
            desktop_ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            options.add_argument(f"--user-agent={desktop_ua}")
            logger.debug(f"Using forced desktop user agent for {self.site_name}")
        elif self.settings.user_agent_rotation:
            ua = UserAgent()
            user_agent = ua.random
            options.add_argument(f"--user-agent={user_agent}")
            logger.debug(f"Using random user agent: {user_agent}")
        
        # Window size randomization
        if self.settings.viewport_randomization:
            width = random.randint(1200, 1920)
            height = random.randint(800, 1080)
            options.add_argument(f"--window-size={width},{height}")
        else:
            options.add_argument(
                f"--window-size={self.settings.window_width},{self.settings.window_height}"
            )
        
        # Additional stealth options
        options.add_argument("--disable-web-security")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-plugins")
        options.add_argument("--disable-images")  # Faster loading
        
        # Remove problematic JavaScript disable for compatibility
        # options.add_argument("--disable-javascript")  # Can cause issues with modern sites
        
        return options
    
    def start_session(self) -> None:
        """Initialize the browser session."""
        try:
            print("🚀 브라우저 세션을 시작합니다...")
            logger.info(f"Starting crawler session for {self.site_name}")
            
            print("⚙️ Chrome 옵션 설정 중...")
            options = self._setup_chrome_options()
            
            print("🔍 Chrome 버전 감지 중...")
            chrome_version = self._get_chrome_version()
            
            # Try multiple approaches to handle version mismatch
            driver_created = False
            attempts = 0
            max_attempts = 4
            
            while not driver_created and attempts < max_attempts:
                attempts += 1
                try:
                    print(f"🔄 브라우저 시작 시도 {attempts}/{max_attempts}...")
                    
                    if attempts == 1 and chrome_version:
                        # First attempt: Use detected version
                        print(f"📋 감지된 버전 {chrome_version} 사용...")
                        self.driver = uc.Chrome(options=options, version_main=chrome_version)
                    elif attempts == 2:
                        # Second attempt: Auto-detect version (let UC decide)
                        print("🎯 자동 감지 모드...")
                        self.driver = uc.Chrome(options=options, version_main=None)
                    elif attempts == 3:
                        # Third attempt: Try common versions
                        for version in [140, 139, 138]:
                            try:
                                print(f"🔧 버전 {version} 시도...")
                                self.driver = uc.Chrome(options=options, version_main=version)
                                break
                            except:
                                continue
                    else:
                        # Fourth attempt: Use system ChromeDriver if available
                        print("🛠️ 시스템 ChromeDriver 사용...")
                        from selenium import webdriver
                        from selenium.webdriver.chrome.service import Service
                        from selenium.webdriver.chrome.options import Options
                        
                        # Fallback to standard Selenium ChromeDriver
                        chrome_options = Options()
                        for option in options.arguments:
                            chrome_options.add_argument(option)
                        
                        self.driver = webdriver.Chrome(options=chrome_options)
                    
                    # Test if driver works
                    self.driver.get("data:text/html,<html><body>Test</body></html>")
                    driver_created = True
                    print("✅ 브라우저 시작 성공!")
                    
                except Exception as version_error:
                    print(f"❌ 시도 {attempts} 실패: {str(version_error)[:100]}...")
                    if hasattr(self, 'driver') and self.driver:
                        try:
                            self.driver.quit()
                        except:
                            pass
                    
                    if attempts == max_attempts:
                        raise Exception(f"브라우저 시작에 실패했습니다. Chrome 버전 호환성 문제일 수 있습니다. 마지막 오류: {version_error}")
                    print("🔄 다른 방법으로 재시도...")
                    continue
            
            print("🔧 브라우저 설정 조정 중...")
            # Remove webdriver property (only for undetected-chromedriver)
            try:
                self.driver.execute_script(
                    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
                )
            except:
                pass  # Skip if it fails
            
            # Set up wait and human behavior
            print("⏱️ 대기 및 행동 시뮬레이터 설정 중...")
            self.wait = WebDriverWait(self.driver, self.settings.page_load_timeout)
            self.human_behavior = HumanBehaviorSimulator(self.driver)
            
            # Disable implicit wait for faster performance
            self.driver.implicitly_wait(0)
            
            print("🎉 브라우저 세션 시작 완료!")
            logger.info("Browser session started successfully")
            
        except Exception as e:
            print(f"❌ 브라우저 세션 시작 실패: {e}")
            logger.error(f"Failed to start browser session: {e}")
            self.cleanup()
            raise
    
    def navigate_to_site(self) -> None:
        """Navigate to the job site homepage."""
        try:
            print(f"🌐 {self.site_config['base_url']} 사이트로 이동 중...")
            logger.info(f"Navigating to {self.site_config['base_url']}")
            self.driver.get(self.site_config["base_url"])
            
            # Human-like pause after page load
            print("⏳ 사이트 로딩 대기 중...")
            self.human_behavior.random_delay(2.0, 4.0)
            
            # Disable mouse movements that cause "out of bounds" errors
            # print("🖱️ 자연스러운 마우스 움직임 시뮬레이션 중...")
            # self.human_behavior.random_mouse_movements(2)
            print("✅ 페이지 로딩 완료!")
            
            print("✅ 사이트 이동 완료!")
            logger.info("Successfully navigated to site")
            
        except Exception as e:
            print(f"❌ 사이트 이동 실패: {e}")
            logger.error(f"Failed to navigate to site: {e}")
            raise
    
    def wait_for_element(
        self, 
        selector: str, 
        by: By = By.CSS_SELECTOR, 
        timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Wait for element to be present and return it."""
        try:
            timeout = timeout or 5  # Use shorter default timeout
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, selector))
            )
            return element
        except TimeoutException:
            logger.warning(f"Element not found: {selector}")
            return None
    
    def wait_for_clickable(
        self, 
        selector: str, 
        by: By = By.CSS_SELECTOR, 
        timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Wait for element to be clickable and return it."""
        try:
            timeout = timeout or 5  # Use shorter default timeout
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, selector))
            )
            return element
        except TimeoutException:
            logger.warning(f"Element not clickable: {selector}")
            return None
    
    def safe_find_element(self, selector: str, by: By = By.CSS_SELECTOR) -> Optional[Any]:
        """Safely find element without throwing exception."""
        try:
            return self.driver.find_element(by, selector)
        except NoSuchElementException:
            return None
    
    def safe_find_elements(self, selector: str, by: By = By.CSS_SELECTOR) -> List[Any]:
        """Safely find multiple elements."""
        try:
            return self.driver.find_elements(by, selector)
        except NoSuchElementException:
            return []
    
    def cleanup(self) -> None:
        """Clean up browser resources."""
        if self.driver:
            try:
                logger.info("Cleaning up browser session")
                self.driver.quit()
                self.driver = None
            except Exception as e:
                logger.error(f"Error during cleanup: {e}")
    
    def __enter__(self):
        """Context manager entry."""
        self.start_session()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.cleanup()