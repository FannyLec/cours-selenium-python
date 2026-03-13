from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from exercice11_page_mine import BooksPage
import logging

def main():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("tests.log"),
            logging.StreamHandler()  # Console aussi
        ]
    )
    logger = logging.getLogger(__name__)

    try:
        logger.info("Exercice 11")
        page = BooksPage(driver)

        logger.info("Ouverture de la page")
        page.open()

        logger.info("Attendre le chargement des livres")
        books = page.wait_books()

        logger.info("Récupérer les éléments nécessaires à l’extraction")
        liste = page.get_books(books)
        logger.info(liste)

        assert len(liste) == 20, f"Nombre de livre inccorect {len(liste)}"
        logger.info("Nombre de livre correct")

        logger.info(f"Les informations des premiers livres extraits : \n {liste[0]} \n {liste[1]} \n {liste[2]} \n {liste[3]}")

    except AssertionError as e:
        logger.error(f"❌ Erreur d'assertion: {e}")
        return False

    except Exception as e:
        logger.error(f"❌ Erreur : {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()