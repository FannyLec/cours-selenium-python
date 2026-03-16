from loginPage import LoginPage
from secureAreaPage import SecureAreaPage
from utils import create_driver
import time



def test_login_logout():
    print("\n" + "=" * 60)
    print("TP1 - TEST 1 : LOGIN / LOGOUT")
    print("=" * 60)

    driver = create_driver()

    try:
        login_page = LoginPage(driver)
        secure_page = SecureAreaPage(driver)

        print("\n1. Ouverture de la page de login...")
        login_page.open()
        assert login_page.is_loaded(), "La page login n'est pas correctement chargée"
        print("   Page login chargée")

        print("2. Vérification du titre de page...")
        assert "The Internet" in login_page.get_page_title(), "Titre inattendu"
        print(f"   Titre correct : {login_page.get_page_title()}")

        print("3. Saisie des identifiants...")
        login_page.login("tomsmith", "SuperSecretPassword!")
        print("   Identifiants saisis et formulaire envoyé")

        time.sleep(3)

        print("4. Vérification de la connexion...")
        assert "/secure" in secure_page.get_current_url(), "Redirection vers /secure absente"
        assert secure_page.is_loaded(), "La page sécurisée n'est pas chargée"
        print("   Connexion réussie")

        print("5. Vérification du message de succès...")
        success_message = secure_page.get_flash_message()
        assert "You logged into a secure area!" in success_message, "Message de succès absent"
        print(f"   Message trouvé : {success_message.strip()}")

        print("6. Vérification du bouton logout...")
        assert secure_page.is_logout_visible(), "Bouton logout non visible"
        print("   Bouton logout visible")

        print("7. Clic sur logout...")
        secure_page.click_logout()

        time.sleep(5)

        print("8. Vérification du retour à la page login...")
        assert "/login" in login_page.get_current_url(), "Retour vers /login absent"
        logout_message = login_page.get_flash_message()
        assert "You logged out of the secure area!" in logout_message, "Message de logout absent"
        print(f"   Retour login validé : {logout_message.strip()}")

        print("\nTEST 1 RÉUSSI")

    except AssertionError as e:
        print(f"\nAssertion échouée: {e}")
        raise
    except Exception as e:
        print(f"\nErreur: {e}")
        raise
    finally:
        driver.quit()
        print("Navigateur fermé")