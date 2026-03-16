
from addRemovePage import AddRemovePage
from utils import create_driver
import time


def test_add_remove_elements():
    print("\n" + "=" * 60)
    print("TP1 - TEST 3 : ADD / REMOVE ELEMENTS")
    print("=" * 60)

    driver = create_driver()

    try:
        add_remove_page = AddRemovePage(driver)

        print("\n1. Ouverture de la page Add/Remove Elements...")
        add_remove_page.open()
        assert add_remove_page.is_loaded(), "La page Add/Remove Elements n'est pas correctement chargée"
        print("   Page chargée")

        print("2. Ajout de 3 éléments...")
        add_remove_page.click_add_element_multiple_times(3)
        count_after_add = add_remove_page.get_delete_buttons_count()
        assert count_after_add == 3, f"3 boutons Delete attendus, trouvé(s): {count_after_add}"
        print(f"   {count_after_add} bouton(s) Delete affiché(s)")

        print("3. Suppression d'un élément...")
        add_remove_page.delete_one_element()
        count_after_one_delete = add_remove_page.get_delete_buttons_count()
        assert count_after_one_delete == 2, f"2 boutons Delete attendus, trouvé(s): {count_after_one_delete}"
        print(f"   Il reste {count_after_one_delete} bouton(s) Delete")

        print("4. Suppression de tous les éléments restants...")
        add_remove_page.delete_all_elements()
        final_count = add_remove_page.get_delete_buttons_count()
        assert final_count == 0, f"0 bouton Delete attendu, trouvé(s): {final_count}"
        print("   Tous les éléments ont été supprimés")

        print("\nTEST 3 RÉUSSI")

    except AssertionError as e:
        print(f"\nAssertion échouée: {e}")
        raise
    except Exception as e:
        print(f"\nErreur: {e}")
        raise
    finally:
        driver.quit()
        print("Navigateur fermé")