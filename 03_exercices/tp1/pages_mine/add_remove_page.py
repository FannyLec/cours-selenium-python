
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class AddRemovePage:
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    BUTTON_XPATH = "//button[@onclick='addElement()']"
    DELETE_ELEMENTS_ID = "elements"
    DELETE_BUTTON_XPATH = "//button[@class = 'added-manually']"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def wait_for_page(self):
        self.wait.until(EC.url_to_be(self.URL))
        return self.URL
    def get_button(self):
        button = self.driver.find_element(By.XPATH, self.BUTTON_XPATH)
        return button
    def multiple_click_button(self, times):
        for _ in range(times):
            button = self.get_button()
            button.click()
    def count_delete_elements(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "added-manually")
        return len(elements)
    def click_delete_button(self):
        button = self.driver.find_element(By.XPATH, self.DELETE_BUTTON_XPATH)
        button.click()
    def click_all_delete_button(self):
        while True:
            buttons = self.driver.find_elements(By.XPATH, self.DELETE_BUTTON_XPATH)
            if not buttons:
                break
            buttons[0].click()