import pytest
import time
from pages.main_page import MainPage

@pytest.mark.smoke
def test_full_navigation_flow(driver):
    main_page = MainPage(driver)
    main_page.open_main_page()
    time.sleep(3)

    main_page.go_to_women()
    time.sleep(2)
    main_page.go_to_men()
    time.sleep(3)

    main_page.scroll_down()
    time.sleep(3)

    main_page.click_latest_drops()
    time.sleep(5)

    main_page.scroll_to_bottom()
    time.sleep(4)

    main_page.click_load_more()
    time.sleep(5)
    main_page.scroll_to_top()
    time.sleep(3)

    assert "asos" in driver.current_url.lower(), "Navigation flow failed"