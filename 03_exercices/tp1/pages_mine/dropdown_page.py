from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"
    DROPDOWN_ID = "dropdown"


    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def wait_for_page(self):
        self.wait.until(EC.url_to_be(self.URL))
        return self.URL

    def wait_for_dropdown(self):
        dropdown_element = self.wait.until(EC.visibility_of_element_located((By.ID,self.DROPDOWN_ID)))
        dropdown = Select(dropdown_element)
        return dropdown
    
    def dropdownselect(self, dropdown, value):
        dropdown.select_by_value(value)
        selected_option = dropdown.first_selected_option.text
        return selected_option






