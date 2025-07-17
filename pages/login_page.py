from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "loginusername")
    PASSWORD_FIELD = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#logInModal .btn-primary")
    WELCOME_USER = (By.ID, "nameofuser")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)
        
        # Handle potential Google password leak alert or other security alerts
        self._handle_security_alerts()
    
    def _handle_security_alerts(self):
        """Handle various security alerts that might appear during login"""
        import time
        max_attempts = 3
        
        for attempt in range(max_attempts):
            try:
                # Wait a bit for alert to appear
                time.sleep(1)
                alert = self.driver.switch_to.alert
                alert_text = alert.text.lower()
                
                if any(keyword in alert_text for keyword in ['password', 'leak', 'security', 'breach', 'compromised']):
                    print(f"Security alert detected: {alert.text}")
                    alert.accept()
                    return True
                else:
                    print(f"Other alert detected: {alert.text}")
                    alert.accept()
                    return True
                    
            except Exception as e:
                if attempt == max_attempts - 1:
                    print("No security alerts found.")
                    return False
                time.sleep(0.5)
        
        return False

    def get_welcome_message(self):
        return self.find_element(self.WELCOME_USER).text


