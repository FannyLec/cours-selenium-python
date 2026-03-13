from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_dynamic_loading():
    """
    Attend les éléments qui se chargent dynamiquement
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        # Accéder au site
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        print("Navigation vers dynamic_loading/1")

        # Vérifier que le bouton "Start" est visible
        start_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Start')]")
        assert start_button.is_displayed(), "Bouton non visible"
        print("Bouton 'Start' trouvé et visible")

        # Cliquer sur "Start"
        start_button.click()
        print("Bouton 'Start' cliqué")

        # Attendre que le texte "Hello World!" apparaisse (max 10 secondes)
        # Localiser le conteneur de chargement
        loading_message = wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )
        print("Élément 'finish' est maintenant visible")

        # Vérifier le contenu
        message_text = loading_message.text
        assert "Hello World!" in message_text, f"Texte incorrect: {message_text}"
        print(f"Message correct: '{message_text}'")

        # Vérifier que le message ne contient pas "It's gone!"
        assert "It's gone!" not in message_text, "Message d'erreur détecté"
        print("Pas de message d'erreur")


        print("\nTest réussi!")
        return True

    except Exception as e:
        print(f"Erreur: {e}")
        return False

    finally:
        driver.quit()
        print("Navigateur fermé")


if __name__ == "__main__":
    test_dynamic_loading()
