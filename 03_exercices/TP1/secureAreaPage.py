from selenium.webdriver.common.by import By
from basePage import BasePage

class SecureAreaPage(BasePage):
    FLASH_MESSAGE = (By.ID, "flash")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button.secondary.radius")
    PAGE_TITLE = (By.TAG_NAME, "h2")

    def is_loaded(self):
        title = self.wait_for_visibility(self.PAGE_TITLE)
        return "Secure Area" in title.text

    def get_flash_message(self):
        return self.wait_for_visibility(self.FLASH_MESSAGE).text

    def is_logout_visible(self):
        return self.wait_for_visibility(self.LOGOUT_BUTTON).is_displayed()

    def click_logout(self):
        self.wait_for_visibility(self.LOGOUT_BUTTON).click()