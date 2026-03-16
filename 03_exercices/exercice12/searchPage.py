from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    URL = "https://practicesoftwaretesting.com"
    RESULT_CARDS_XPATH = "//a[contains(@class,'card')]"

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def wait_for_page_ready(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "search-query")))

    def get_search_field(self):
        return self.driver.find_element(By.ID, "search-query")

    def get_search_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    def search_products(self, query):
        search_field = self.get_search_field()
        search_field.clear()
        search_field.send_keys(query)

        search_button = self.get_search_button()
        search_button.click()

    def wait_for_results(self):
        # self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card"))) 
        # ne vérifie pas que toutes les cartes finales sont là
        # ne vérifie pas qu’elles sont visibles
        # ne vérifie pas que le rechargement dynamique est terminé
        # ne vérifie pas non plus que les sous-éléments internes sont prêts


        self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.RESULT_CARDS_XPATH)))

    def get_result_cards(self):
        return self.driver.find_elements(By.CLASS_NAME, "card")

    def extract_product_data(self):
        products_data = []
        self.wait_for_results()
        products = self.driver.find_elements(By.CSS_SELECTOR, "a.card")

        for i, product in enumerate(products):
            try:
                name_elem = product.find_element(By.TAG_NAME, "h5")
                name = name_elem.text

                price_elem = product.find_element(By.CSS_SELECTOR, "[data-test='product-price']")
                price_text = price_elem.text.replace("$", "").strip()
                price = float(price_text)

                try:
                    rating_elem = product.find_element(By.CSS_SELECTOR, '[data-test="co2-rating-badge"] .co2-letter.active')
                    rating = rating_elem.text
                except:
                    rating = "N/A"

                products_data.append({
                    "id": i + 1,
                    "name": name,
                    "price": price,
                    "rating": rating
                })

            except Exception as e:
                print(f"Erreur extraction produit {i+1}: {e}")

        return products_data