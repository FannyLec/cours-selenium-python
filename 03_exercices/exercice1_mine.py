from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://example.com")
    assert driver.title == "Example Domain", f"Titre incorrect : {driver.title}"
    print(f"Titre vérifié : {driver.title}")

    heading = driver.find_element(By.TAG_NAME, "h1")
    assert "Example Domain" in heading.text, "Texte attendu non trouvé dans le h1"
    print(f"Contenu vérifié : {heading.text}")

    print(driver.current_url)
    WebDriverWait(driver, 2).until(EC.url_to_be("https://example.com/"))
    # assert driver.current_url == "https://example.com", "URL incorrecte"
    print(f"URL vérifiée : {driver.current_url}")

    input("Appuyez sur Entrée pour fermer...")


except AssertionError as e:
    print(f"Erreur d'assertion : {e}")

finally:
    driver.quit()