from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_extraction_donnees():
    """
    Extrait et traite les données des produits
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Accéder au site
        driver.get("https://practicesoftwaretesting.com/")
        print("Navigation vers practicesoftwaretesting.com")

        # Attendre le chargement des produits
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.card")))
        time.sleep(1)

        # Extraire le nom de chaque produit
        product_names = []
        product_elements = driver.find_elements(By.CSS_SELECTOR, ".card")
        print(f" {len(product_elements)} produits trouvés")

        for product in product_elements:
            try:
                # Extraire le nom (dans .card-title ou h2/h5)
                name_element = product.find_element(By.CSS_SELECTOR, ".card-title")
                name = name_element.text.strip()
                if name:
                    product_names.append(name)
            except:
                pass

        print(f" {len(product_names)} noms extraits")

        #  Extraire les prix ou descriptions disponibles
        product_descriptions = []
        for product in product_elements:
            try:
                # Extraire les textes des paragraphes
                text_elements = product.find_elements(By.CSS_SELECTOR, ".card-text")
                description_texts = [el.text.strip() for el in text_elements if el.text.strip()]
                product_descriptions.append(", ".join(description_texts) if description_texts else "N/A")
            except:
                product_descriptions.append("N/A")

        print(f" {len(product_descriptions)} descriptions extraites")

        #  Créer une liste Python
        products_list = []
        for i, (name, desc) in enumerate(zip(product_names, product_descriptions)):
            if name:
                products_list.append({
                    "index": i + 1,
                    "name": name,
                    "description": desc
                })

        print(f" Liste créée avec {len(products_list)} produits")

        #  Afficher les 5 premiers produits
        print("\n--- 5 Premiers Produits ---")
        for product in products_list[:5]:
            print(f"  {product['index']}. {product['name']}")
            #print(f"      Description: {product['description']}")
            if product['description'] != "N/A":
                print(f"      Description: {product['description']}")

        #  Afficher la liste complète
        print(f"\n--- Tous les Produits ({len(products_list)}) ---")
        for product in products_list:
            print(f"  {product['index']}. {product['name']}")

        print("\n Test réussi!")
        return True

    except Exception as e:
        print(f" Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False

    finally:
        driver.quit()
        print("Navigateur fermé")


if __name__ == "__main__":
    test_extraction_donnees()
