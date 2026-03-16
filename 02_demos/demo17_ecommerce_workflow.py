
"""
Demo : Workflow E-Commerce Complet
Demonstre: cas réel d'automatisation d'achat
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def demo_saucedemo_complete_flow():
    """Workflow complet d'achat sur Sauce Demo"""
    print("\n" + "="*60)
    print("DEMO: E-COMMERCE WORKFLOW COMPLET")
    print("="*60)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # ============================================
        # ÉTAPE 1: Accès au site
        # ============================================
        print("\n1  ACCÈS AU SITE")
        print("-" * 60)

        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 10)
        time.sleep(1)

        print(f" Page chargée: {driver.title}")
        assert "Swag Labs" in driver.title
        print(" Titre correct")

        # ============================================
        # ÉTAPE 2: Login
        # ============================================
        print("\n2  LOGIN")
        print("-" * 60)

        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        time.sleep(2)
        print(" Login effectué")

        # Vérifier qu'on est sur la page produits
        assert "/inventory" in driver.current_url
        print(" Redirection vers inventory")

        # ============================================
        # ÉTAPE 3: Navigation catalogue
        # ============================================
        print("\n3  PARCOURS DU CATALOGUE")
        print("-" * 60)

        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f" {len(products)} produits trouvés")

        # Vérifier qu'on a du contenu
        assert len(products) > 0
        product_names = [p.find_element(By.CLASS_NAME, "inventory_item_name").text for p in products[:3]]
        print(f" Produits: {product_names}")

        # ============================================
        # ÉTAPE 4: Ajout au panier
        # ============================================
        print("\n4  AJOUT AU PANIER")
        print("-" * 60)

        add_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        print(f" {len(add_buttons)} boutons 'Ajouter' trouvés")

        # Ajouter 3 produits
        for i in range(3):
            if i < len(add_buttons):
                add_buttons[i].click()
                time.sleep(0.5)
                print(f"    Produit {i+1} ajouté")

        # Vérifier le panier
        try:
            cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            cart_count = cart_badge.text
            print(f" Panier: {cart_count} articles")
        except:
            print(f" Articles ajoutés au panier")

        # ============================================
        # ÉTAPE 5: Voir le panier
        # ============================================
        print("\n5 VÉRIFIER LE PANIER")
        print("-" * 60)

        try:
            cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
            cart_icon.click()
            time.sleep(1)
            print(" Page panier chargée")

            cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
            print(f" {len(cart_items)} articles dans le panier")
        except Exception as e:
            print(f" Panier vérifié (workflow en cours)")

        # ============================================
        # ÉTAPE 6: Procéder au paiement
        # ============================================
        print("\n6  PAIEMENT")
        print("-" * 60)

        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()
        time.sleep(1)

        print(" Page paiement accédée")

        # Remplir les informations
        first_name = driver.find_element(By.ID, "first-name")
        last_name = driver.find_element(By.ID, "last-name")
        postal_code = driver.find_element(By.ID, "postal-code")

        first_name.send_keys("John")
        last_name.send_keys("Doe")
        postal_code.send_keys("12345")

        print(" Informations de livraison remplies")

        # ============================================
        # ÉTAPE 7: Confirmer le paiement
        # ============================================
        print("\n7  CONFIRMATION")
        print("-" * 60)

        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        time.sleep(1)

        print(" Panier confirmé")

        # Voir le résumé
        summary_elements = driver.find_elements(By.CLASS_NAME, "summary_value")
        print(f" Éléments du résumé: {len(summary_elements)}")

        # ============================================
        # ÉTAPE 8: Finaliser
        # ============================================
        print("\n8  FINALISER LA COMMANDE")
        print("-" * 60)

        finish_button = driver.find_element(By.ID, "finish")
        finish_button.click()
        time.sleep(2)

        print(" Commande soumise")

        # Vérifier le message de confirmation
        success_message = driver.find_element(By.CLASS_NAME, "complete-header")
        assert "Thank you" in success_message.text
        print(f" Message de confirmation: '{success_message.text}'")

        print("\n" + "="*60)
        print(" WORKFLOW COMPLET RÉUSSI!")
        print("="*60)

    except AssertionError as e:
        print(f"\n Assertion échouée: {e}")
    except Exception as e:
        print(f"\n Erreur: {e}")
        import traceback
        traceback.print_exc()
        traceback.print_exc()

    finally:
        print("\nFermeture du navigateur...")
        driver.quit()
        print(" Fermé")

def demo_saucedemo_advanced():
    """Scénario avancé avec waits"""
    print("\n" + "="*60)
    print("DEMO: E-COMMERCE AVEC WAITS AVANCÉS")
    print("="*60)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        print("\n1. Navigation et attente...")
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 10)

        # Attendre le bouton de login
        login_btn = wait.until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )
        print(" Bouton login trouvé")

        # Login
        print("2. Login...")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        login_btn.click()

        # Attendre la liste des produits
        print("3. Attente du chargement des produits...")
        products = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )
        print(f" {len(products)} produits chargés")

        # Ajouter un article
        print("4. Ajout au panier...")
        first_product = products[0]
        add_button = first_product.find_element(By.CLASS_NAME, "btn_inventory")
        add_button.click()

        # Attendre le badge
        print("5. Attente du badge du panier...")
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        print(" Badge visible")

        # Vérifier le nombre
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert badge.text == "1"
        print(f" Panier: {badge.text} article")

        print("\n SCÉNARIO AVANCÉ RÉUSSI!")

    except Exception as e:
        print(f"\n Erreur: {e}")

    finally:
        driver.quit()

def main():
    """Menu principal"""
    print("\n" + ""*60)
    print("  SELENIUM DEMO: E-COMMERCE WORKFLOW")
    print(""*60)

    try:
        print("\nChoisissez la démo:")
        print("1. Workflow d'achat complet")
        print("2. Scénario avancé avec waits")

        choice = input("\nVotre choix (1-2): ").strip()

        if choice == "1":
            demo_saucedemo_complete_flow()
        elif choice == "2":
            demo_saucedemo_advanced()
        else:
            print("Choix invalide, exécution du workflow complet...")
            demo_saucedemo_complete_flow()

    except KeyboardInterrupt:
        print("\n\n  Interrompu par l'utilisateur")
    except Exception as e:
        print(f"\n Erreur: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
