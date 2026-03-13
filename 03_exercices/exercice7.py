from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_xpath_locators():
    """
    Localise des éléments en utilisant des XPath sur un site e-commerce
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        # Accéder au site
        driver.get("https://practicesoftwaretesting.com/")
        print("Navigation vers practicesoftwaretesting.com")

        # Attendre le chargement des produits
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.card")))
        print("Produits chargés")

        # Localiser les cartes produit avec XPath contains (class peut avoir plusieurs valeurs)
        product_cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'card')]")
        print(f"XPath contains @class: {len(product_cards)} cartes produit trouvées")
        assert len(product_cards) > 0, "Aucune carte produit trouvée"

        # Localiser les titres de produits avec XPath contains
        product_titles = driver.find_elements(By.XPATH, "//*[contains(@class, 'card-title')]")
        for i, title in enumerate(product_titles[:3]):
            print(f"Produit {i+1}: {title.get_attribute('textContent').strip()}")


        # Variantes de XPath
        print("\nVariantes de XPath testées:")

        # XPath avec position
        first_card = driver.find_element(By.XPATH, "//div[contains(@class, 'card')][1]")
        print(f" Position [1]: Première carte trouvée")

        # XPath avec position et attribut
        cards_limited = driver.find_elements(By.XPATH, "(//div[contains(@class, 'card')])[position() <= 5]")
        print(f" Position [1-5]: {len(cards_limited)} cartes trouvées")

        # XPath avec not contains - find elements without "row"
        elements_no_row = driver.find_elements(By.XPATH, "//div[contains(@class, 'card') and not(contains(@class, 'row'))]")
        print(f"  XPath avec not(): {len(elements_no_row)} éléments trouvés")

        # XPath avec descendant - find cards that have titles
        cards_with_descendants = driver.find_elements(By.XPATH, "//div[contains(@class, 'card') and descendant::*[contains(@class, 'card-title')]]")
        print(f"  Descendant: {len(cards_with_descendants)} cartes avec titre")

        print("\nTest réussi!")
        return True

    except Exception as e:
        print(f"Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False

    finally:
        driver.quit()
        print("Navigateur fermé")


if __name__ == "__main__":
    test_xpath_locators()
