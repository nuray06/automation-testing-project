from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SortPage(BasePage):
    sort_button = (By.CSS_SELECTOR, '[data-testid="sort-button"]')
    whats_new_option = (By.ID, "plp_web_sort_whats_new")

    def open_sort(self):
        self.click(self.sort_button)

    def choose_whats_new(self):
        self.click(self.whats_new_option)

    def new_selected(self):
        element = self.driver.find_element(*self.whats_new_option)
        return element.is_selected()