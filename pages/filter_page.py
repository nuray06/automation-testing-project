from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FilterPage(BasePage):
    filter_button = (By.CSS_SELECTOR, '[data-testid="filter-button-desktop"]')
    gender_filter = (By.CSS_SELECTOR, 'button[data-auto-id="floor"]')
    men_option = (By.XPATH, "//div[contains(text(),'Men')]")
    products = (By.CSS_SELECTOR, "a[href*='/prd/']")

    def open_filters(self):
        self.click(self.filter_button)

    def open_gender_filter(self):
        self.click(self.gender_filter)

    def select_men(self):
        self.click(self.men_option)

    def get_products(self):
        return self.driver.find_elements(*self.products)