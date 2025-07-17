from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.short_wait = WebDriverWait(driver, 3)

    def find_element(self, by_locator, timeout=10):
        """Find element with custom timeout and better error handling"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            print(f"Element not found: {by_locator}")
            raise

    def find_element_clickable(self, by_locator, timeout=10):
        """Find clickable element"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.element_to_be_clickable(by_locator))
        except TimeoutException:
            print(f"Element not clickable: {by_locator}")
            raise

    def click_element(self, by_locator, timeout=10):
        """Click element with retry mechanism"""
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                element = self.find_element_clickable(by_locator, timeout)
                element.click()
                return
            except Exception as e:
                if attempt == max_attempts - 1:
                    print(f"Failed to click element after {max_attempts} attempts: {by_locator}")
                    raise
                time.sleep(1)

    def enter_text(self, by_locator, text, clear_first=True):
        """Enter text with option to clear field first"""
        element = self.find_element(by_locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_element_text(self, by_locator):
        return self.find_element(by_locator).text
    
    def is_element_present(self, by_locator, timeout=3):
        """Check if element is present without throwing exception"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(by_locator))
            return True
        except TimeoutException:
            return False
    
    def wait_for_alert(self, timeout=5):
        """Wait for alert and return alert object"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.alert_is_present())
        except TimeoutException:
            return None
    
    def handle_alert(self, accept=True, timeout=5):
        """Handle alert with better error handling"""
        try:
            alert = self.wait_for_alert(timeout)
            if alert:
                alert_text = alert.text
                if accept:
                    alert.accept()
                else:
                    alert.dismiss()
                return alert_text
            return None
        except Exception as e:
            print(f"Error handling alert: {e}")
            return None

