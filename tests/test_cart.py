import pytest
import time
from pages.main_page import MainPage
from pages.cart_page import CartPage

@pytest.mark.regression
def test_add_tshirt(driver):
    main_page = MainPage(driver)
    cart_page = CartPage(driver)

    main_page.open_main_page()
    main_page.search("t-shirt")
    time.sleep(3)

    cart_page.open_first_product()
    time.sleep(3)

    cart_page.scroll_down_little()
    time.sleep(2)

    cart_page.choose_size_m()
    time.sleep(2)

    cart_page.add_to_bag()
    time.sleep(3)

    assert "bag" in driver.page_source.lower() or "view bag" in driver.page_source.lower()


@pytest.mark.regression
def test_open_jeans(driver):
    main_page = MainPage(driver)
    cart_page = CartPage(driver)

    main_page.open_main_page()
    main_page.search("jeans")
    time.sleep(3)

    cart_page.scroll_down_little()
    time.sleep(2)

    cart_page.open_first_product()
    time.sleep(3)
    cart_page.choose_jeans_size()
    time.sleep(2)

    cart_page.scroll_down_little()
    time.sleep(2)
    cart_page.scroll_to_top()
    time.sleep(2)

    cart_page.next_image()
    time.sleep(2)
    cart_page.next_image()
    time.sleep(2)

    cart_page.prev_image()
    time.sleep(2)
    cart_page.prev_image()
    time.sleep(2)

    cart_page.open_product_details()
    time.sleep(2)

    cart_page.scroll_after_details()
    time.sleep(2)

    assert cart_page.is_product_details_open()

    cart_page.open_product_details()
    time.sleep(2)

    cart_page.scroll_to_top()
    time.sleep(2)

    cart_page.save_to_favourites()
    time.sleep(3)

    assert "saved" in driver.page_source.lower() or "item saved" in driver.page_source.lower()