from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_css_selectors():
    """
    Localise des éléments en utilisant des sélecteurs CSS sur un site e-commerce
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

        # Localiser les cartes produit avec CSS class selector
        product_cards = driver.find_elements(By.CSS_SELECTOR, "a.card")
        print(f"Cartes produit trouvées: {len(product_cards)}")
        assert len(product_cards) > 0, "Aucune carte produit trouvée"

        # Localiser les titres de produits avec CSS
        product_titles = driver.find_elements(By.CSS_SELECTOR, ".card-title")
        print(f"Titres de produits trouvés: {len(product_titles)}")
        for i in range(min(3, len(product_titles))):
            title = driver.find_elements(By.CSS_SELECTOR, ".card-title")[i]
            print(f"  Produit {i+1}: {title.text}")

        # Localiser les prix avec CSS attribute selector
        prices = driver.find_elements(By.CSS_SELECTOR, "[data-test='product-price']")
        filtered_prices = [p for p in prices if '$' in p.text]
        print(f"Prix trouvés: {len(filtered_prices)}")
        for i, price in enumerate(filtered_prices[:3]):
            print(f"  Prix {i+1}: {price.text}")


        print("\nTest réussi!")
        return True

    except Exception as e:
        print(f"Erreur: {e}")
        return False

    finally:
        driver.quit()
        print("Navigateur fermé")


if __name__ == "__main__":
    test_css_selectors()
