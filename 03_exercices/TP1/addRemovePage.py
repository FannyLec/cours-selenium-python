from selenium.webdriver.common.by import By
from basePage import BasePage
from selenium.webdriver.support.ui import Select

class AddRemovePage(BasePage):
    PATH = "/add_remove_elements/"

    ADD_BUTTON = (By.CSS_SELECTOR, "button[onclick='addElement()']")
    DELETE_BUTTONS = (By.CLASS_NAME, "added-manually")
    PAGE_TITLE = (By.TAG_NAME, "h3")

    def open(self):
        super().open(self.PATH)

    def is_loaded(self):
        title = self.wait_for_visibility(self.PAGE_TITLE)
        return "Add/Remove Elements" in title.text

    def click_add_element(self):
        self.wait_for_visibility(self.ADD_BUTTON).click()

    def click_add_element_multiple_times(self, count):
        for _ in range(count):
            self.click_add_element()

    def get_delete_buttons_count(self):
        return len(self.driver.find_elements(*self.DELETE_BUTTONS))

    def delete_one_element(self):
        buttons = self.driver.find_elements(*self.DELETE_BUTTONS)
        if buttons:
            buttons[0].click()

    def delete_all_elements(self):
        while self.get_delete_buttons_count() > 0:
            self.delete_one_element()