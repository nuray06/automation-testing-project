from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class CartPage(BasePage):
    first_product = (By.CSS_SELECTOR, "a[href*='/prd/']")
    size_dropdown = (By.ID, "variantSelector")
    add_to_bag_button = (By.CSS_SELECTOR, '[data-testid="add-button"]')

    product_details_button = (By.XPATH, "//button[@aria-label='Product Details']")
    product_details_content = (By.ID, "productDescriptionDetails")

    save_to_favourites_button = (By.CSS_SELECTOR, '[data-testid="saveForLater"]')

    next_image_button = (By.CSS_SELECTOR, "button.arrow-button-right")
    prev_image_button = (By.CSS_SELECTOR, "button.arrow-button-left")

    def open_first_product(self):
        self.click(self.first_product)

    def choose_size_m(self):
        dropdown = self.find_element(self.size_dropdown)
        select = Select(dropdown)
        select.select_by_visible_text("M - EU 40-42")

    def choose_jeans_size(self):
        dropdown = self.find_element(self.size_dropdown)
        select = Select(dropdown)
        select.select_by_visible_text("W29 L30")

    def add_to_bag(self):
        self.click(self.add_to_bag_button)

    def scroll_down_little(self):
        self.driver.execute_script("window.scrollBy(0, 500);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 100);")

    def scroll_after_details(self):
        self.driver.execute_script("window.scrollBy(0, 400);")

    def open_product_details(self):
        self.click(self.product_details_button)

    def is_product_details_open(self):
        return self.is_element_visible(self.product_details_content)

    def save_to_favourites(self):
        button = self.find_element(self.save_to_favourites_button)
        self.driver.execute_script("arguments[0].click();", button)

    def next_image(self):
        button = self.find_element(self.next_image_button)
        self.driver.execute_script("arguments[0].click();", button)

    def prev_image(self):
        button = self.find_element(self.prev_image_button)
        self.driver.execute_script("arguments[0].click();", button)