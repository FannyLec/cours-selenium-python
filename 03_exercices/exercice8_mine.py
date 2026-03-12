from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def alert():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# 3. Cliquez sur "Click for JS Alert"
        js_alerte= driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
        js_alerte.click()
# 4. Acceptez l'alerte (OK)
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert   
        alert.accept() 
# 5. Vérifiez le message affiché après l'acceptation
        output = wait.until (
            EC.visibility_of_element_located((By.ID, "result"))
        )
        assert output.text == "You successfully clicked an alert", "Mauvais message d'alerte JS"
# 6. Cliquez sur "Click for JS Confirm"
        js_confirm= driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
        js_confirm.click()
# 7. Refusez l'alerte (Cancel)
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert  
        alert.dismiss() 
# 8. Vérifiez le message de refus
        output = wait.until (
            EC.visibility_of_element_located((By.ID, "result"))
        )
        assert output.text == "You clicked: Cancel", "Mauvais message de refus"

        print("OK !")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    alert()