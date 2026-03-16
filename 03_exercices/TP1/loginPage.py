from selenium.webdriver.common.by import By
from basePage import BasePage

class LoginPage(BasePage):
    PATH = "/login"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")
    PAGE_TITLE = (By.TAG_NAME, "h2")

    def open(self):
        super().open(self.PATH)

    def is_loaded(self):
        title = self.wait_for_visibility(self.PAGE_TITLE)
        return "Login Page" in title.text

    def enter_username(self, username):
        field = self.wait_for_visibility(self.USERNAME_INPUT)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait_for_visibility(self.PASSWORD_INPUT)
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait_for_visibility(self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_flash_message(self):
        return self.wait_for_visibility(self.FLASH_MESSAGE).text