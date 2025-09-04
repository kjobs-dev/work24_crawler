"""Authentication manager for job sites."""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import structlog
from typing import Dict, Any

from .base_crawler import StealthCrawler

logger = structlog.get_logger()


class AuthenticationManager:
    """Handles login functionality for different job sites."""
    
    def __init__(self, crawler: StealthCrawler):
        self.crawler = crawler
        self.site_config = crawler.site_config
        self.settings = crawler.settings
        
    def login(self, email: str, password: str) -> bool:
        """
        Perform login for the current site.

        Args:
            email: User email/username
            password: User password

        Returns:
            True if login successful, False otherwise
        """
        try:
            print(f"🔐 {self.crawler.site_name.upper()} 로그인 프로세스를 시작합니다...")
            logger.info(f"Starting login process for {self.crawler.site_name}")
            
            # Navigate to login page
            print("🌐 로그인 페이지로 이동 중...")
            login_url = self.site_config["login_url"]
            self.crawler.driver.get(login_url)
            
            # Wait for page to load and simulate reading
            print("⏳ 페이지 로딩 대기 중...")
            self.crawler.human_behavior.random_delay(2.0, 4.0)
            
            # Handle cookie banners or popups
            print("🍪 팝업 및 쿠키 배너 처리 중...")
            self._handle_popups()
            
            # Handle Work24-specific modal login flow
            if self.crawler.site_name == "work24":
                print("🏢 Work24 전용 로그인 프로세스 실행 중...")
                return self._work24_login(email, password)
            
            # Standard login flow for other sites
            print("📝 표준 로그인 프로세스 실행 중...")
            return self._standard_login(email, password)
            
        except Exception as e:
            print(f"❌ 로그인 실패: {e}")
            logger.error(f"Login failed with exception: {e}")
            return False

    def _work24_login(self, email: str, password: str) -> bool:
        """Handle Work24 login flow with ID/Password popup."""
        import time
        start_time = time.time()
        
        try:
            # Wait for dynamic content to load (reduced from 3-4s to 2-3s)
            logger.info("Waiting for login elements to load dynamically...")
            load_start = time.time()
            self.crawler.human_behavior.random_delay(2.0, 3.0)
            logger.info(f"Dynamic load wait completed in {time.time() - load_start:.2f}s")
            
            # Click the ID/Password login button to open popup
            find_start = time.time()
            login_trigger_selector = self.site_config["selectors"]["login_trigger"]
            login_trigger = self.crawler.wait_for_element(login_trigger_selector, timeout=3)
            
            if not login_trigger:
                logger.error("ID/Password login button not found after waiting")
                return False
            
            logger.info(f"Found ID/Password login button in {time.time() - find_start:.2f}s")
            
            # Scroll to element and wait (reduced wait)
            scroll_start = time.time()
            self.crawler.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", login_trigger)
            self.crawler.human_behavior.random_delay(0.5, 1.0)  # Reduced from 1-2s
            logger.info(f"Scrolling and positioning completed in {time.time() - scroll_start:.2f}s")
            
            # Try JavaScript click to bypass overlay issues
            click_start = time.time()
            try:
                self.crawler.driver.execute_script("arguments[0].click();", login_trigger)
                logger.info("Used JavaScript click for login trigger")
            except Exception:
                # Fallback to regular click
                login_trigger.click()
                logger.info("Used regular click for login trigger")
            
            logger.info(f"Login trigger click completed in {time.time() - click_start:.2f}s")
            
            # Wait for popup to open (reduced wait)
            popup_start = time.time()
            self.crawler.human_behavior.random_delay(1.0, 2.0)  # Reduced from 2-3s
            logger.info(f"Popup wait completed in {time.time() - popup_start:.2f}s")
            
            # Fill credentials in the popup
            cred_start = time.time()
            result = self._standard_login(email, password)
            logger.info(f"Credential filling completed in {time.time() - cred_start:.2f}s")
            
            logger.info(f"Total Work24 login process took {time.time() - start_time:.2f}s")
            return result
            
        except Exception as e:
            logger.error(f"Work24 login failed after {time.time() - start_time:.2f}s: {e}")
            return False

    def _standard_login(self, email: str, password: str) -> bool:
        """Standard login flow for filling credentials."""
        import time
        from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoAlertPresentException
        start_time = time.time()
        
        try:
            # Find and fill email field
            print("📧 이메일 입력 필드를 찾는 중...")
            email_start = time.time()
            email_selector = self.site_config["selectors"]["email_input"]
            email_element = self.crawler.wait_for_element(email_selector, timeout=5)
            
            if not email_element:
                print("❌ 이메일 입력 필드를 찾을 수 없습니다.")
                logger.error("Email input field not found")
                return False
            
            print("✅ 이메일 입력 필드 발견!")
            logger.info(f"Found email field in {time.time() - email_start:.2f}s")
            
            # Scroll element into view and click directly (avoid mouse movement)
            print("📧 이메일 입력 중...")
            self.crawler.driver.execute_script("arguments[0].scrollIntoView(true);", email_element)
            self.crawler.human_behavior.random_delay(0.3, 0.7)  # Reduced wait
            email_element.click()
            self.crawler.human_behavior.human_type(email_element, email)
            print("✅ 이메일 입력 완료!")
            logger.info(f"Email field filled in {time.time() - email_start:.2f}s")
            
            # Random pause between fields (reduced)
            self.crawler.human_behavior.random_delay(0.3, 0.8)
            
            # Find and fill password field
            print("🔒 비밀번호 입력 필드를 찾는 중...")
            pass_start = time.time()
            password_selector = self.site_config["selectors"]["password_input"]
            password_element = self.crawler.wait_for_element(password_selector, timeout=5)
            
            if not password_element:
                print("❌ 비밀번호 입력 필드를 찾을 수 없습니다.")
                logger.error("Password input field not found")
                return False
            
            print("✅ 비밀번호 입력 필드 발견!")
            # Scroll element into view and click directly
            print("🔒 비밀번호 입력 중...")
            self.crawler.driver.execute_script("arguments[0].scrollIntoView(true);", password_element)
            self.crawler.human_behavior.random_delay(0.3, 0.7)  # Reduced wait
            password_element.click()
            self.crawler.human_behavior.human_type(password_element, password)
            print("✅ 비밀번호 입력 완료!")
            logger.info(f"Password field filled in {time.time() - pass_start:.2f}s")
            
            # Pause before clicking login (reduced)
            self.crawler.human_behavior.random_delay(0.5, 1.0)
            
            # Click login button
            print("🚀 로그인 버튼을 찾는 중...")
            login_start = time.time()
            login_button_selector = self.site_config["selectors"]["login_button"]
            login_button = self.crawler.wait_for_clickable(login_button_selector, timeout=5)
            
            if not login_button:
                print("❌ 로그인 버튼을 찾을 수 없습니다.")
                logger.error("Login button not found")
                return False
            
            # Scroll login button into view and click
            print("🖱️ 로그인 버튼 클릭 중...")
            self.crawler.driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
            self.crawler.human_behavior.random_delay(0.3, 0.7)  # Reduced wait
            login_button.click()
            print("✅ 로그인 버튼 클릭 완료!")
            logger.info(f"Login button clicked in {time.time() - login_start:.2f}s")
            
            # IMMEDIATELY handle alerts after login click - this is the key fix
            alert_start = time.time()
            try:
                print("⚠️ 로그인 알림창 확인 중...")
                logger.info("Checking for immediate login alert...")
                
                # Wait for alert to appear - shorter wait since alert appears immediately
                self.crawler.human_behavior.random_delay(0.5, 1.5)
                
                # Check for alert
                alert = self.crawler.driver.switch_to.alert
                alert_text = alert.text
                print(f"📢 알림창 메시지: {alert_text}")
                logger.info(f"Login alert text: {alert_text}")
                
                # Check if alert indicates success - be more flexible with success detection
                success_keywords = ["성공", "Success", "로그인 성공", "성공하였습니다"]
                if any(keyword in alert_text for keyword in success_keywords):
                    print("✅ 로그인 성공 메시지 확인됨!")
                    alert.accept()  # Click OK on the alert
                    print("✅ 알림창 확인 완료!")
                    logger.info(f"Accepted login success alert in {time.time() - alert_start:.2f}s")
                    
                    # Wait for redirect/page change after alert dismissal
                    self.crawler.human_behavior.random_delay(1.0, 2.0)
                    
                    logger.info(f"Total standard login took {time.time() - start_time:.2f}s")
                    return True
                else:
                    print("❌ 로그인 실패 메시지 감지")
                    logger.error(f"Login failed - alert text: {alert_text}")
                    alert.accept()  # Still accept the alert
                    return False
                    
            except NoAlertPresentException:
                logger.debug("No alert found immediately after login")
                # Continue with normal verification if no immediate alert
                
                # Wait for login to process (reduced)
                print("⏳ 로그인 처리 대기 중...")
                self.crawler.human_behavior.random_delay(1.0, 2.0)
                
                # Verify login success
                print("✅ 로그인 성공 여부 확인 중...")
                verify_start = time.time()
                if self._verify_login_success():
                    print("🎉 로그인 성공!")
                    logger.info(f"Login verified successful in {time.time() - verify_start:.2f}s")
                    logger.info(f"Total standard login took {time.time() - start_time:.2f}s")
                    return True
                else:
                    print("❌ 로그인 실패 - 인증 확인 실패")
                    logger.error("Login failed - verification unsuccessful")
                    return False
                    
            except Exception as alert_error:
                logger.error(f"Alert handling error: {alert_error}")
                # Try to handle any unexpected alert issues
                try:
                    # Force check for alert one more time
                    alert = self.crawler.driver.switch_to.alert
                    alert_text = alert.text
                    print(f"📢 예상치 못한 알림창 메시지: {alert_text}")
                    
                    success_keywords = ["성공", "Success", "로그인 성공", "성공하였습니다"]
                    if any(keyword in alert_text for keyword in success_keywords):
                        print("✅ 성공 메시지 확인됨!")
                        alert.accept()
                        self.crawler.human_behavior.random_delay(1.0, 2.0)
                        return True
                    else:
                        alert.accept()
                        return False
                except:
                    # If all alert handling fails, fall back to verification
                    logger.warning("Alert handling failed completely, trying verification")
                    try:
                        self.crawler.human_behavior.random_delay(1.0, 2.0)
                        return self._verify_login_success()
                    except:
                        return False
                        
        except Exception as e:
            print(f"❌ 표준 로그인 실패: {e}")
            logger.error(f"Standard login failed after {time.time() - start_time:.2f}s: {e}")
            return False
    
    def _handle_popups(self) -> None:
        """Handle common popups like cookie banners."""
        common_popup_selectors = [
            "[data-testid='close-button']",
            ".artdeco-global-alert__dismiss",
            "#onetrust-accept-btn-handler",
            ".cookie-banner .accept-button",
            "[aria-label='Dismiss']",
            ".modal-close",
            ".popup-close"
        ]
        
        for selector in common_popup_selectors:
            popup = self.crawler.safe_find_element(selector)
            if popup and popup.is_displayed():
                try:
                    logger.debug(f"Closing popup with selector: {selector}")
                    self.crawler.human_behavior.human_click(popup)
                    self.crawler.human_behavior.random_delay(0.5, 1.0)
                    break
                except Exception as e:
                    logger.debug(f"Could not close popup: {e}")
                    continue
    
    def _verify_login_success(self) -> bool:
        """Verify that login was successful."""
        # Check current URL for login indicators
        current_url = self.crawler.driver.current_url
        
        # Common indicators of successful login
        success_indicators = [
            "/feed",
            "/home",
            "/dashboard",
            "/profile",
            "logged_in",
            "authenticated"
        ]
        
        # Check if URL contains success indicators
        for indicator in success_indicators:
            if indicator in current_url.lower():
                return True
        
        # Check for presence of logout/profile elements
        logout_selectors = [
            "[data-control-name='nav.settings_signout']",  # LinkedIn
            ".account-link",  # Indeed
            ".user-menu",
            "[aria-label='Account menu']",
            ".profile-menu"
        ]
        
        for selector in logout_selectors:
            element = self.crawler.safe_find_element(selector)
            if element:
                return True
        
        # Check that we're not still on login page
        login_page_indicators = [
            "login",
            "signin",
            "sign-in",
            "authenticate"
        ]
        
        for indicator in login_page_indicators:
            if indicator in current_url.lower():
                return False
        
        return True
    
    def get_credentials(self) -> tuple[str, str]:
        """Get credentials for the current site."""
        if self.crawler.site_name == "linkedin":
            return self.settings.linkedin_email, self.settings.linkedin_password
        elif self.crawler.site_name == "indeed":
            return self.settings.indeed_email, self.settings.indeed_password
        elif self.crawler.site_name == "work24":
            return self.settings.work24_email, self.settings.work24_password
        else:
            raise ValueError(f"No credentials configured for site: {self.crawler.site_name}")
    
    def is_logged_in(self) -> bool:
        """Check if user is currently logged in."""
        return self._verify_login_success()