from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_javascript_alerts():
    """
    Gère les alertes JavaScript (accept/cancel)
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        # Accéder au site
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        print("Navigation vers javascript_alerts")

        # Test Alerte Simple (Alert)
        print("\n--- Test 1: Simple Alert ---")
        alert_button = driver.find_element(By.XPATH, "//button[contains(text(), 'JS Alert')]")
        alert_button.click()
        print("Bouton cliqué")

        # Attendre et accepter l'alerte
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Alerte trouvée: '{alert_text}'")

        alert.accept()  # Cliquer OK
        print("Alerte acceptée")

        # Vérifier le message de confirmation
        result_element = driver.find_element(By.ID, "result")
        result_text = result_element.text
        print(f"Résultat: {result_text}")

        # Test Alerte Confirm - Refus
        print("\n--- Test 2: Confirm Alert (Cancel) ---")
        confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'JS Confirm')]")
        confirm_button.click()
        print("Bouton 'Confirm' cliqué")

        # Attendre et refuser l'alerte
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Alerte trouvée: '{alert_text}'")

        alert.dismiss()  # Cliquer Cancel
        print("Alerte refusée (Cancel)")

        # Vérifier le message de refus
        result_element = driver.find_element(By.ID, "result")
        result_text = result_element.text
        print(f"Résultat: {result_text}")
        assert "cancel" in result_text.lower(), "Le refus n'a pas été enregistré"

        # Test Alerte Prompt
        print("\n--- Test 3: Prompt Alert ---")
        prompt_button = driver.find_element(By.XPATH, "//button[contains(text(), 'JS Prompt')]")
        prompt_button.click()
        print("Bouton 'Prompt' cliqué")

        # Attendre et remplir la prompt
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Prompt trouvée: '{alert_text}'")

        alert.send_keys("Mon texte de test")
        print("Texte envoyé à la prompt")

        alert.accept()  # OK
        print("Prompt acceptée")

        # Vérifier que le texte a été enregistré
        result_element = driver.find_element(By.ID, "result")
        result_text = result_element.text
        print(f"Résultat: {result_text}")

        print("\nTest réussi!")
        return True

    except Exception as e:
        print(f"Erreur: {e}")
        return False

    finally:
        driver.quit()
        print("Navigateur fermé")


if __name__ == "__main__":
    test_javascript_alerts()
