# Exercice 2 : Localiser un Élément par Text
# Site: example.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_localisation_element():
    """
    Localise un élément contenant du texte spécifique
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://example.com")

        # trouver l'element lien de la page
        element = driver.find_element(By.CSS_SELECTOR,"a")
        print(f"Element trouve : {element.text}")

        # verifier que c'est un lien
        tag_name = element.tag_name
        assert tag_name == "a",f"l'element n'est pas un lien : {tag_name}"
        print(f"Type d'element correct : {tag_name}")

        # Verifier que le href est valide
        href = element.get_attribute("href")
        assert href is not None and len(href) > 0,f"URL invalide : {href}"
        print(f"Url valide : {href}")

        print("Test reussie")
        return True

    except Exception as e:
        print(f"Erreur: {e}")
        return False

    finally:
        driver.quit()
        print("Navigateur fermé")

if __name__ == "__main__":
    test_localisation_element()