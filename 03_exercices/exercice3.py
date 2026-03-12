from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_remplir_formulaire():
    """
    Remplit un formulaire simple et vérifie la soumission
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Accéder au formulaire
        driver.get("https://demoqa.com/text-box")
        print("Navigation vers le formulaire")

        # 2. Remplir le champ "Full Name"
        fullname_field = driver.find_element(By.ID, "userName")
        fullname_field.send_keys("John Doe")
        print("Champ 'Full Name' rempli: John Doe")

        # 3. Remplir le champ "Email"
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("john@example.com")
        print("Champ 'Email' rempli: john@example.com")

        # 4. Remplir le champ "Current Address"
        address_field = driver.find_element(By.ID, "currentAddress")
        address_field.send_keys("123 Main Street")
        print("Champ 'Address' rempli: 123 Main Street")

        # 5. Cliquer sur le bouton "Submit"
        submit_button = driver.find_element(By.ID, "submit")
        # Scroller jusqu'au bouton
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()
        print("Bouton 'Submit' cliqué")

        # 6. Vérifier que les données sont affichées
        wait.until(EC.presence_of_element_located((By.ID, "output")))
        output = driver.find_element(By.ID, "output")
        output_text = output.text

        assert "John Doe" in output_text, "Nom non trouvé"
        assert "john@example.com" in output_text, "Email non trouvé"
        assert "123 Main Street" in output_text, "Adresse non trouvé"
        print("Données affichées correctement")

        print("\nTest réussi!")
        return True

    except Exception as e:
        print(f"Erreur: {e}")
        return False

    finally:
        driver.quit()
        print("Navigateur fermé")


if __name__ == "__main__":
    test_remplir_formulaire()
