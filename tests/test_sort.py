import pytest
import time
from pages.main_page import MainPage
from pages.sort_page import SortPage

@pytest.mark.regression
def test_sort_dress(driver):
    main_page = MainPage(driver)
    sort_page = SortPage(driver)

    main_page.open_main_page()
    main_page.search("dress")
    time.sleep(3)

    sort_page.open_sort()
    sort_page.choose_whats_new()
    time.sleep(3)

    assert sort_page.new_selected(), "What's new sorting was not selected"