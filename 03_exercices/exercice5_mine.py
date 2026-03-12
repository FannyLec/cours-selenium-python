from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait



def checkbox():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        checkbox_1 = checkboxes[0]
        checkbox_2 = checkboxes[1]

        assert not checkbox_1.is_selected(), "La checkbox 1 devrait être décochée au départ"
        assert checkbox_2.is_selected(), "La checkbox 2 devrait être cochée au départ"

        if not checkbox_1.is_selected():
            checkbox_1.click()
        assert checkbox_1.is_selected(), "La checkbox 1 devrait être cochée"

        if checkbox_2.is_selected():
            checkbox_2.click()
        assert not checkbox_2.is_selected(), "La checkbox 2 devrait être décochée"

        print("Checkboxes ok")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    checkbox()