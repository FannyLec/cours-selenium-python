from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait



def dropdown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://the-internet.herokuapp.com/dropdown")

        dropdown_element = driver.find_element(By.ID, "dropdown")
        dropdown = Select(dropdown_element)
        dropdown.select_by_value("1")
        selected_option = dropdown.first_selected_option
        assert selected_option.text == "Option 1", f"Texte sélectionné incorrect : {selected_option.text}"
        
        dropdown.select_by_value("2")
        selected_option = dropdown.first_selected_option
        assert selected_option.text == "Option 2", f"Texte sélectionné incorrect : {selected_option.text}"

        print(f"Option selectionnée : {selected_option.text}")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    dropdown()