from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


try:
    driver.get("https://example.com")
    element = driver.find_element(By.TAG_NAME, "a")
    print(f"Élément trouvé : {element.text}")

    element = driver.find_element(By.XPATH, "//a")

    element = driver.find_element(By.CSS_SELECTOR, "body a")

    tag_name = element.tag_name
    assert tag_name == "a", f"L'élément n'est pas un lien, tag trouvé : {tag_name}"
    print(f"Type d'élément vérifié : <{tag_name}>")

    a_href = element.get_attribute("href")
    assert a_href != "", "Le lien est vide"
    print(f"Le lien est valide : {a_href}")

    input("Appuyez sur Entrée pour fermer...")


except AssertionError as e:
    print(f"Erreur d'assertion : {e}")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    driver.quit()