"""Human behavior simulation utilities for anti-detection."""

import random
import time
from typing import Tuple, List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import structlog

logger = structlog.get_logger()


class HumanBehaviorSimulator:
    """Simulates human-like behavior to avoid detection."""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.actions = ActionChains(driver)
    
    def random_delay(self, min_seconds: float = 1.0, max_seconds: float = 3.0) -> None:
        """Sleep for a random duration to mimic human behavior."""
        delay = random.uniform(min_seconds, max_seconds)
        logger.debug(f"Human delay: {delay:.2f}s")
        time.sleep(delay)
    
    def human_scroll(self, element: WebElement, scroll_count: int = 3) -> None:
        """Scroll like a human would - in increments with pauses."""
        for i in range(scroll_count):
            scroll_amount = random.randint(100, 300)
            self.driver.execute_script(
                f"arguments[0].scrollTop += {scroll_amount};", element
            )
            self.random_delay(0.5, 1.5)
    
    def page_scroll(self, direction: str = "down", pixels: int = None) -> None:
        """Scroll the page like a human."""
        if pixels is None:
            pixels = random.randint(200, 600)
        
        if direction == "down":
            self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        elif direction == "up":
            self.driver.execute_script(f"window.scrollBy(0, -{pixels});")
        
        self.random_delay(0.3, 1.0)
    
    def human_type(self, element: WebElement, text: str) -> None:
        """Type text like a human with random delays between keystrokes."""
        element.clear()
        self.random_delay(0.2, 0.5)
        
        for char in text:
            element.send_keys(char)
            # Vary typing speed - some chars take longer
            if char in " .,":
                delay = random.uniform(0.1, 0.3)
            else:
                delay = random.uniform(0.05, 0.15)
            time.sleep(delay)
        
        self.random_delay(0.3, 0.8)
    
    def mouse_movement_to_element(self, element: WebElement) -> None:
        """Move mouse to element in a human-like way."""
        # Get element location
        location = element.location
        size = element.size
        
        # Calculate random point within element
        x_offset = random.randint(0, size["width"])
        y_offset = random.randint(0, size["height"])
        
        # Move to element with human-like curve
        self.actions.move_to_element_with_offset(
            element, x_offset, y_offset
        ).perform()
        
        self.random_delay(0.1, 0.3)
    
    def human_click(self, element: WebElement) -> None:
        """Click element like a human."""
        # Move to element first
        self.mouse_movement_to_element(element)
        
        # Small pause before clicking
        self.random_delay(0.1, 0.4)
        
        # Click
        element.click()
        
        # Pause after clicking
        self.random_delay(0.5, 1.2)
    
    def reading_pause(self, text_length: int = 0) -> None:
        """Pause to simulate reading time based on content length."""
        if text_length == 0:
            base_time = random.uniform(2.0, 4.0)
        else:
            # Approximate reading time: 200 words per minute
            words = text_length / 5  # Rough word count
            reading_time = (words / 200) * 60  # Convert to seconds
            base_time = min(max(reading_time, 2.0), 15.0)  # Between 2-15 seconds
        
        actual_time = random.uniform(base_time * 0.7, base_time * 1.3)
        logger.debug(f"Reading pause: {actual_time:.2f}s")
        time.sleep(actual_time)
    
    def random_mouse_movements(self, count: int = 3) -> None:
        """Make random mouse movements to appear more human."""
        for _ in range(count):
            x = random.randint(100, 800)
            y = random.randint(100, 600)
            self.actions.move_by_offset(x, y).perform()
            self.random_delay(0.1, 0.5)
    
    def browser_back_forward_simulation(self) -> None:
        """Occasionally use browser back/forward to appear human."""
        if random.random() < 0.1:  # 10% chance
            logger.debug("Simulating browser back/forward")
            self.driver.back()
            self.random_delay(1.0, 2.0)
            self.driver.forward()
            self.random_delay(1.0, 2.0)
    
    def tab_switching_simulation(self) -> None:
        """Occasionally switch tabs to appear human."""
        if len(self.driver.window_handles) > 1 and random.random() < 0.05:  # 5% chance
            logger.debug("Simulating tab switching")
            current_handle = self.driver.current_window_handle
            other_handles = [h for h in self.driver.window_handles if h != current_handle]
            
            if other_handles:
                self.driver.switch_to.window(random.choice(other_handles))
                self.random_delay(0.5, 1.5)
                self.driver.switch_to.window(current_handle)
                self.random_delay(0.5, 1.0)