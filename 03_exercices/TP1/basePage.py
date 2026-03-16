from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    BASE_URL = "https://the-internet.herokuapp.com"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, path):
        self.driver.get(f"{self.BASE_URL}{path}")

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_all_presence(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url