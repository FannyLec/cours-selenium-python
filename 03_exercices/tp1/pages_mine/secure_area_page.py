from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SecurePage:
    URL = "https://the-internet.herokuapp.com/secure"
    SUCCESS_MESSAGE_ID = "flash"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    # 1. Ouvrir la page de login.
    def open(self):
        self.driver.get(self.URL)
   
    def wait_for_page(self):
        self.wait.until(EC.url_to_be(self.URL))
        return self.URL
    
    def wait_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.ID, self.SUCCESS_MESSAGE_ID))
        )

    def wait_button_logout(self):
        return self.wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "button"))
        )

    
    def click_logout(self):
        button= self.driver.find_element(By.CLASS_NAME, "button")
        button.click()


