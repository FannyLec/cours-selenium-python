from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def xpath():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://practicesoftwaretesting.com/")

        cards = wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, "//a[contains(@class,'card')]"))
        )
        titles = driver.find_elements(By.XPATH, "//*[@class='card-title']")
        
        first_two_cards = driver.find_elements(
            By.XPATH,
            "//a[contains(@class,'card')][position() <= 2]"
        )
        assert len(first_two_cards) == 2, f"Nombre de cartes limité incorrect : {len(first_two_cards)}"


        cards_without_plier = driver.find_elements(
            By.XPATH,
            "//*[contains(@class, 'card-title') and not(contains(text(), 'Plier'))]"
        )
        assert len(cards_without_plier) == 5, f"Filtrage avec not() incorrect : {len(cards_without_plier)}"

        cards_with_title = driver.find_elements(
            By.XPATH,
            "//a[contains(@class, 'card') and descendant::*[contains(@class, 'card-title')]]"
        )
        assert len(cards_with_title) == 9, f"Recherche avec descendant incorrecte : {len(cards_with_title)}"

        for card in cards:
            assert card.is_displayed(), "Une carte n'est pas visible"
        for title in titles:
            assert title.is_displayed(), "Un titre n'est pas visible"
        
        assert len(cards) == 9, "Nombre de produit incorrect"

        print("Tous les éléments ont été trouvé")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    xpath()