from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_checkboxes():
    """
    Coche/décoche des cases à cocher et vérifie l'état
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        #  Accéder au site
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        print("Navigation vers la page des checkboxes")

        #  Localiser les checkboxes
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        print(f"{len(checkboxes)} checkboxes trouvées")

        # Vérifier l'état initial
        checkbox_1 = checkboxes[0]
        checkbox_2 = checkboxes[1]

        is_checked_1 = checkbox_1.is_selected()
        is_checked_2 = checkbox_2.is_selected()
        print(f"État initial - Checkbox 1: {'Cochée' if is_checked_1 else 'Décochée'}")
        print(f"État initial - Checkbox 2: {'Cochée' if is_checked_2 else 'Décochée'}")

        # Cocher la première si elle n'est pas cochée
        if not checkbox_1.is_selected():
            checkbox_1.click()
            print("Checkbox 1 cochée")

        # Vérifier que la première est maintenant cochée
        assert checkbox_1.is_selected(), "La checkbox 1 n'est pas cochée"
        print("Vérification: Checkbox 1 est cochée")

        # Décocher la deuxième si elle est cochée
        if checkbox_2.is_selected():
            checkbox_2.click()
            print("Checkbox 2 décochée")

        # Vérifier que la deuxième est maintenant décochée
        assert not checkbox_2.is_selected(), "La checkbox 2 est toujours cochée"
        print("Vérification: Checkbox 2 est décochée")

        print("\nTest réussi!")
        return True

    except Exception as e:
        print(f"Erreur: {e}")
        return False

    finally:
        driver.quit()
        print("Navigateur fermé")


if __name__ == "__main__":
    test_checkboxes()
