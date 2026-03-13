from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ToolsPage:
    URL = "https://practicesoftwaretesting.com"

    SEARCH_FORM = (By.ID, "filters")
    TEXT_SEARCH = (By.ID, "search-query")
    BUTTON_SEARCH = (By.XPATH, "//button[@type='submit']")
    SEARCH_TERM = (By.XPATH, "//span[@data-test='search-term']")
    SEARCH_COMPLETED = (By.XPATH, "//div[@data-test='search_completed']")


#    - Vérifiez que ces éléments sont visibles

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def get_form(self):
        return self.driver.find_elements(self.SEARCH_FORM)

    def get_text_search(self):
        return self.driver.find_elements(self.TEXT_SEARCH)
    
    def get_button_search(self):
        return self.driver.find_elements(self.BUTTON_SEARCH)
    
    def get_search_term(self):
        return self.driver.find_elements(self.SEARCH_TERM)
    
    def get_search_completed(self):
        return self.driver.find_elements(self.SEARCH_COMPLETED)






