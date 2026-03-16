from selenium.webdriver.common.by import By
from basePage import BasePage
from selenium.webdriver.support.ui import Select

class DropdownPage(BasePage):
    PATH = "/dropdown"

    DROPDOWN = (By.ID, "dropdown")
    PAGE_TITLE = (By.TAG_NAME, "h3")

    def open(self):
        super().open(self.PATH)

    def is_loaded(self):
        title = self.wait_for_visibility(self.PAGE_TITLE)
        return "Dropdown List" in title.text

    def get_select(self):
        element = self.wait_for_visibility(self.DROPDOWN)
        return Select(element)

    def select_option_by_visible_text(self, text):
        self.get_select().select_by_visible_text(text)

    def get_selected_option_text(self):
        return self.get_select().first_selected_option.text