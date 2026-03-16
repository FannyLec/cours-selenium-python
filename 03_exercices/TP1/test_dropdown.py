from dropdownpage import DropdownPage
from utils import create_driver
import time

def test_dropdown():
    print("\n" + "=" * 60)
    print("TP1 - TEST 2 : DROPDOWN")
    print("=" * 60)

    driver = create_driver()

    try:
        dropdown_page = DropdownPage(driver)

        print("\n1. Ouverture de la page dropdown...")
        dropdown_page.open()
        assert dropdown_page.is_loaded(), "La page dropdown n'est pas correctement chargée"
        print("   Page dropdown chargée")

        print("2. Vérification de la liste déroulante...")
        select = dropdown_page.get_select()
        assert select is not None, "Liste déroulante introuvable"
        print("   Liste déroulante présente")

        print("3. Sélection de Option 1...")
        dropdown_page.select_option_by_visible_text("Option 1")
        assert dropdown_page.get_selected_option_text() == "Option 1", "Option 1 non sélectionnée"
        print("   Option 1 sélectionnée")

        print("4. Sélection de Option 2...")
        dropdown_page.select_option_by_visible_text("Option 2")
        assert dropdown_page.get_selected_option_text() == "Option 2", "Option 2 non sélectionnée"
        print("   Option 2 sélectionnée")

        print("\nTEST 2 RÉUSSI")

    except AssertionError as e:
        print(f"\nAssertion échouée: {e}")
        raise
    except Exception as e:
        print(f"\nErreur: {e}")
        raise
    finally:
        driver.quit()
        print("Navigateur fermé")

if __name__ == "__main__":
    test_dropdown()        