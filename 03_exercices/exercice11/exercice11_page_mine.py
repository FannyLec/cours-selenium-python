from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# * charger la page ;
# * attendre que les livres soient disponibles ;
# * récupérer les éléments nécessaires à l’extraction.

class BooksPage:
    URL = "https://books.toscrape.com"
    ELEMENTS = (By.CSS_SELECTOR,".product_pod")
    BOOKS = []


    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self):
        self.driver.get(self.URL)

    def wait_books(self):
        elements = self.wait.until(EC.visibility_of_all_elements_located(self.ELEMENTS))
        return elements

    def get_books(self, elements):
        for index, book in enumerate(elements, start=1):
            star_rating = book.find_element(By.XPATH, ".//*[contains(@class,'star-rating')]")
            class_name = star_rating.get_attribute("class")
            note = class_name.replace("star-rating", "").strip()
            title = book.find_element(By.XPATH, ".//a[@title]").text.strip()
            price = book.find_element(By.XPATH, ".//*[@class='product_price']/p").text.strip()
            
            self.BOOKS.append({
                "index": index,
                "rate":note,
                "title": title,
                "price":price,
            })
        return self.BOOKS