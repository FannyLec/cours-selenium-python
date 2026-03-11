from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Initialiser le driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def test_navigation_simple():
    try:
        # naviguer vers le site
        driver.get("https://example.com")

        # Vérifiez que le titre de la page est exactement "Example Domain"
        assert driver.title == "Example Domain", f"Titre incorrect {driver.title}"
        print(f"Titre vérifié: {driver.title}")

        # Vérifiez que le contenu contient "Example Domain"
        body_text = driver.find_element(By.TAG_NAME,"body").text
        # print(body_text)
        assert "Example Domain" in body_text, "Texte 'Example Domain' non trouvé"
        print("Contenu vérifié: 'Example Domain' trouvé")

        # Verifier que c'est la bonne page
        assert "example" in driver.current_url.lower(), "URL incorrecte"
        print(f"URL correcte: {driver.current_url}")

        print("\nTest réussi!")
        return True


    except AssertionError as e:
        print(f"✗ Erreur d'assertion: {e}")
        return False


    except Exception as e:
        print(f"✗ Erreur: {e}")
        return False

    finally:
        # 5. Fermer le navigateur
        driver.quit()
        print("Navigateur fermé")

if __name__ == "__main__":
    test_navigation_simple()