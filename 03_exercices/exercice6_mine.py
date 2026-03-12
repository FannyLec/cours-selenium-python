from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def CSS_selector():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://practicesoftwaretesting.com/")
        cards = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".card"))
        )
        titles = driver.find_elements(By.CSS_SELECTOR, ".card-title")
        
        for card in cards:
            assert card.is_displayed(), "Une carte n'est pas visible"
        for title in titles:
            assert title.is_displayed(), "Un titre n'est pas visible"
        
        assert len(cards) == 9, "Nombre de produit incorrect"

        print("Tous les produits sont chargés !")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    CSS_selector()