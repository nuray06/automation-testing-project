from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):
    url = "https://www.asos.com/"

    search_input = (By.NAME, "q")
    women_category = (By.ID, "women-floor")
    men_category = (By.ID, "men-floor")
    latest_drops = (By.XPATH, "//img[contains(@src,'latest-drops')]")
    load_more_button = (By.CSS_SELECTOR, "a[data-auto-id='loadMoreProducts']")

    def open_main_page(self):
        self.open(self.url)

    def search(self, text):
        element = self.find_element(self.search_input)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    def go_to_women(self):
        self.click(self.women_category)

    def go_to_men(self):
        self.click(self.men_category)

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 800);")

    def click_latest_drops(self):
        element = self.find_element(self.latest_drops)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_load_more(self):
        element = self.find_element(self.load_more_button)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")