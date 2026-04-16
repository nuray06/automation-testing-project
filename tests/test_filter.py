import pytest
import time
from pages.main_page import MainPage
from pages.filter_page import FilterPage

@pytest.mark.regression
def test_filter_shoes(driver):
    main_page = MainPage(driver)
    filter_page = FilterPage(driver)

    main_page.open_main_page()
    main_page.search("shoes")
    time.sleep(3)

    filter_page.open_filters()
    filter_page.open_gender_filter()
    filter_page.select_men()
    time.sleep(5)

    products = filter_page.get_products()
    assert len(products) > 0, "No products after applying gender filter"