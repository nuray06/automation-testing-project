from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    search_input = (By.NAME, "q")

    def search(self, text):
        element = self.find_element(self.search_input)
        element.clear()
        element.send_keys(text)
        element.submit()