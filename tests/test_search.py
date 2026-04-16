import pytest
import time
from pages.main_page import MainPage
from pages.search_page import SearchPage

@pytest.mark.smoke
@pytest.mark.parametrize("item", [
    "shoes",
    "dress",
    "jacket",
    "t-shirt",
    "jeans"
])
def test_search_products(driver, item):
    main_page = MainPage(driver)
    search_page = SearchPage(driver)

    main_page.open_main_page()
    search_page.search(item)
    time.sleep(3)

    main_page.scroll_down()
    time.sleep(2)

    assert "shoes" in driver.current_url.lower(), f"Search did not work for {item}"
    print("Search succeeded")