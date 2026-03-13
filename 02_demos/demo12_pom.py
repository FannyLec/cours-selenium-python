from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DropdowPage:
    URL = "https://the-internet.herokuapp.com/dropdown"
    DROPDOWN = (By.ID,"dropdown")

    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self):
        self.driver.get(self.URL)

    def select_option_by_text(self,text):
        element = self.wait.until(EC.visibility_of_element_located(self.DROPDOWN))
        Select(element).select_by_visible_text(text)

    def get_selected_option_text(self):
        element = self.wait.until(EC.visibility_of_element_located(self.DROPDOWN))
        return Select(element).first_selected_option.text
    

def main():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        print("Demo POM dropdown")
        page = DropdowPage(driver)

        print("Ouverture de la page")
        page.open()

        print("Selectionner Option")
        page.select_option_by_text("Option 1")

        print("Lecture de l'Option")
        selected = page.get_selected_option_text()
        print("Option selectionner : ",selected)

        assert selected == "Option 1"
        print("verification OK")

        print("Selectionner Option")
        page.select_option_by_text("Option 2")

        print("Lecture de l'Option")
        selected = page.get_selected_option_text()
        print("Option selectionner : ",selected)

        assert selected == "Option 2"
        print("verification OK")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()






