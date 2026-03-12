from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 10)

try:
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()

    full_name_field = driver.find_element(By.ID, "userName")
    email_field = driver.find_element(By.ID, "userEmail")
    address_field = driver.find_element(By.ID, "currentAddress")

    full_name_field.send_keys("John Doe")
    email_field.send_keys("john@example.com")
    address_field.send_keys("123 Main Street")

    # wait.until(EC.text_to_be_present_in_element_value((By.ID, "userEmail"),"john@example.com"))
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    submit_button.click()


    wait.until(EC.presence_of_element_located((By.ID, "output")))

    output_name = driver.find_element(By.ID, "name")
    output_name_text = output_name.text
    output_email = driver.find_element(By.ID, "email")
    output_email_text = output_email.text
    output_adresse = driver.find_element(By.CSS_SELECTOR, "p#currentAddress")
    output_adresse_text = output_adresse.text

    assert "John Doe" in output_name_text, "Nom non trouvé dans le résultat"
    assert "john@example.com" in output_email_text, "Email non trouvé dans le résultat"
    assert  "123 Main Street" in output_adresse_text, "Adresse non trouvée dans le résltat"

    print(f"Résultat vérifié :\n{output_name_text}, {output_email_text}, {output_adresse_text}")


except AssertionError as e:
    print(f"Erreur d'assertion : {e}")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    driver.quit()