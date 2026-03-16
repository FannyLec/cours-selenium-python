from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from toolsPage import ToolsPage


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    page = ToolsPage(driver)
    wait = WebDriverWait(driver, 10)

    try:
        form = page.get_form()
        assert form.is_displayed(), "Le formulaire n'est pas visible"
        text_search = page.get_text_search()
        assert text_search.is_displayed(), "Le champde text de recherche n'est pas visible"    
        button_search = page.get_button_search()
        assert button_search.is_displayed(), "Le boutton de recherche n'est pas visible"     

        text_search.send_keys("hammer")
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(button_search)
        )
        button.click()
        results = wait.until(
            EC.presence_of_all_elements_located(page.get_search_completed)
        )
        search_term = page.get_search_term
        assert search_term == "hammer", f"Mauvais text recherché {search_term}"


#    - Vérifiez qu'au moins un résultat est affiché

        print("\nTP RÉUSSI!")

    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()

    finally:
        driver.quit()


if __name__ == "__main__":
    main()