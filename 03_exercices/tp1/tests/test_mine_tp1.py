from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages_mine.login_page import LoginPage
from pages_mine.secure_area_page import SecurePage
from pages_mine.dropdown_page import DropdownPage
from pages_mine.add_remove_page import AddRemovePage


def create_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver

def test01():
    driver = create_driver()
    page = LoginPage(driver)
    securePage = SecurePage(driver)

    try:
        print("=" * 60)
        print("TEST01 - Login et logout")
        print("=" * 60)

# 1. Ouvrir la page de login.
        print("\n--- Ouvrir la page de login ---")
        page.open()

# 2. Vérifier que le titre ou le contenu de la page correspond bien à une page d’authentification.
        print("\n--- Vérifier que le titre contient Login ---")
        title = page.wait_for_title()
        assert "Login" in title, "Le titre ne contient pas Login"
# 3. Saisir le username et le password fournis.
        print("\n--- Saisir le username et password ---")
        page.type_username()
        page.type_password()
# 4. Cliquer sur le bouton de connexion.
        print("\n--- Cliquer sur connexion ---")
        page.click_login()
# 5. Vérifier que la connexion a réussi.
        print("\n--- Vérifier la connexion ---")
        new_url = securePage.wait_for_page()
        assert driver.current_url == new_url, f"Mauvaise url : {new_url}"
# 6. Vérifier la présence du message de succès.
        print("\n--- Vérifier la présence du message de connexion ---")
        message = securePage.wait_success_message()
        assert message is not None, "Le message de succès n'apparait pas"
# 7. Vérifier la présence du bouton ou lien de logout.
        print("\n--- Vérifier la présence du bouton logout ---")
        button = securePage.wait_button_logout()
        assert button is not None, "Le bouton de logout n'est pas présent"
# 8. Cliquer sur logout.
        print("\n--- Cliquer sur logout ---")
        securePage.click_logout()
# 9. Vérifier que l’utilisateur revient bien sur la page de login.
        print("\n--- Vérifier la déconnexion ---")
        new_url = page.wait_for_page()
        assert driver.current_url == new_url, "Mauvaise url"

        print("\nTest01 RÉUSSI!")

    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()

    finally:
        driver.quit()
    
def test02():
    driver = create_driver()
    page = DropdownPage(driver)

    try:
        print("=" * 60)
        print("TEST02 - Dropdown page")
        print("=" * 60)

    # 1. Ouvrir la page Dropdown.
        print("\n--- Ouvrir la page Dropdown ---")
        page.open()
    # 2. Vérifier que la liste déroulante est présente.
        print("\n--- Vérifier présence Dropdown ---")
        page.wait_for_page
        dropdown = page.wait_for_dropdown()
        assert dropdown is not None, "Le dropdown n'est pas présent"
    # 3. Sélectionner `Option 1`.
        print("\n--- Selectionner option 1 ---")
        selected_option = page.dropdownselect(dropdown, "1")
    # 4. Vérifier que `Option 1` est bien sélectionnée.
        assert "Option 1" in selected_option, f"Option incorrecte: {selected_option}"
    # 5. Sélectionner ensuite `Option 2`.
        print("\n--- Selectionner option 2 ---")
        selected_option = page.dropdownselect(dropdown, "2")
    # 6. Vérifier que `Option 2` est bien sélectionnée.
        assert "Option 2" in selected_option, f"Option incorrecte: {selected_option}"
        
        print("\nTest02 RÉUSSI!")

    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()

    finally:
        driver.quit()


def test03():
    driver = create_driver()
    page = AddRemovePage(driver)

    try:
        print("=" * 60)
        print("TEST03 - AddRemove page")
        print("=" * 60)





    # 1. Ouvrir la page Add/Remove Elements.
        print("\n--- Ouvrir la page Add/Remove ---")
        page.open()
    # 2. Cliquer 3 fois sur `Add Element`.
        print("\n--- Cliquer 3 fois sur `Add Element` ---")
        page.multiple_click_button(3)    
    # 3. Vérifier que 3 boutons `Delete` sont affichés.
        print("\n--- Vérifier nombre de bouton delete ---")
        elements = page.count_delete_elements()
        assert elements == 3, f"Mauvais nombre d'éléments delete {elements}"
    # 4. Supprimer 1 élément.
        print("\n--- Supprimer un element ---")
        page.click_delete_button()
    # 5. Vérifier qu’il reste 2 boutons `Delete`.
        elements = page.count_delete_elements()
        assert elements == 2, f"Mauvais nombre d'éléments delete {elements}"
    # 6. Supprimer tous les éléments restants.
        print("\n--- Supprimer tous les elements restant ---")
        page.click_all_delete_button()
    # 7. Vérifier qu’il ne reste plus aucun bouton `Delete`.
        elements = page.count_delete_elements()
        assert elements == 0, f"Mauvais nombre d'éléments delete {elements}"

        
        print("\nTest03 RÉUSSI!")

    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()

    finally:
        driver.quit()
