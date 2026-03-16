from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME = "tomsmith"
    PASSWORD = "SuperSecretPassword!"
    USERNAME_INPUT_ID = "username"
    PASSWORD_INPUT_ID = "password"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def wait_for_page(self):
        self.wait.until(EC.url_to_be(self.URL))
        return self.URL

    def wait_for_title(self):
        title = self.wait.until(EC.presence_of_element_located((By.TAG_NAME,"h2")))
        return title.text

    def type_username(self):
        username_input = self.driver.find_element(By.ID, self.USERNAME_INPUT_ID)
        username_input.send_keys(self.USERNAME)

    def type_password(self):
        password_input = self.driver.find_element(By.ID, self.PASSWORD_INPUT_ID)
        password_input.send_keys(self.PASSWORD)

    def click_login(self):
        button= self.driver.find_element(By.TAG_NAME, "button")
        button.click()


