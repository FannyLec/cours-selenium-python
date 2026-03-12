from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def boucle():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://practicesoftwaretesting.com/")
        cards = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".card"))
        )
        cards = driver.find_elements(By.CSS_SELECTOR, ".card")

        products = []
        for index, card in enumerate(cards, start=1):
            name = card.find_element(By.CSS_SELECTOR, ".card-title").text.strip()
            text_elements = card.find_elements(By.CSS_SELECTOR, ".card-footer")
            text_values = [element.text.strip() for element in text_elements if element.text.strip()]

            products.append({
                "index": index,
                "name": name,
                "details": text_values,
            })


        # 7. Affichez les 5 premiers produits
        for index, product in enumerate(products[0:5], start=1):
            print(index, product)
        # 8. Affichez la liste complète
        for index, product in enumerate(products, start=1):
            print(index, product)        
        
        assert len(products) == 9, f"Liste de produits incorrecte : {len(products)}"
        assert products[0]["name"] == "Combination Pliers", f"Mauvais produit {products[0]["name"]}"

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    boucle()