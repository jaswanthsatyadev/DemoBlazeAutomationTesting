from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def click_element(self, by_locator):
        self.find_element(by_locator).click()

    def enter_text(self, by_locator, text):
        self.find_element(by_locator).send_keys(text)

    def get_element_text(self, by_locator):
        return self.find_element(by_locator).text

