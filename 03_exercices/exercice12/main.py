from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from searchPage import SearchPage
from report import generate_report




def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    page = SearchPage(driver)

    try:
        print("=" * 60)
        print("RECHERCHE ET EXTRACTION DE DONNÉES")
        print("=" * 60)

        print("\n--- Phase 1: Navigation et Localisation ---")
        page.open()
        print("Accédé à practicesoftwaretesting.com")

        page.wait_for_page_ready()
        print("Champ de recherche trouvé")
        print("Bouton de recherche trouvé")
        print("Les éléments sont visibles")

        print("\n--- Phase 2: Recherche de 'hammer' ---")
        page.search_products("hammer")
        print("'hammer' saisi dans le champ")
        print("Bouton soumis")

        page.wait_for_results()
        print("Résultats chargés")

        results = page.get_result_cards()
        assert len(results) > 0, "Aucun résultat trouvé"
        print(f"{len(results)} résultat(s) trouvé(s)")

        print("\n--- Phase 3: Extraction de Données ---")
        products = page.extract_product_data()

        for product in products:
            print(f"Produit {product['id']}: {product['name']} - ${product['price']:.2f}")

        generate_report(products)

        print("\nTP RÉUSSI!")

    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()

    finally:
        driver.quit()


if __name__ == "__main__":
    main()