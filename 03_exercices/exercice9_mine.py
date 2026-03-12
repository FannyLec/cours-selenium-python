from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def explicit_wait():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        start = driver.find_element(By.XPATH,"//*[@id='start']/button")
        start.click()
        # 4. Attendez explicitement (max 10 secondes) que le texte "Hello World!" apparaisse
        wait = WebDriverWait(driver, 10) 
        element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='finish']/h4"))
        )
        assert element.text == "Hello World!", f"Le texte est incorrect : {element.text}"
        # 6. Vérifiez que le texte contient "It's gone!"
        assert not "It's gone!" in element.text, "Le texte contient It's gone! "


        print("OK !")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    explicit_wait()