import pytest
from playwright.sync_api import Page
from pom.pages.home_page import HomePage
from pom.pages.product_page import ProductPage
from pom.pages.cart_page import CartPage
from playwright.sync_api import expect
from random import randint


def test_catalogue_title(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.check_catalogue_title()
    home_page.check_product_is_displayed()

def test_product_title_price_same_in_details(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    product_title_home_page = home_page.get_product_title()
    product_price_home_page = home_page.get_product_price()
    home_page.go_to_first_product_page()
    product_page = ProductPage(page)
    product_title_product_page = product_page.get_product_title()
    product_price_product_price = product_page.get_product_price()
    assert product_title_home_page == product_title_product_page, 'Product titles is different'
    assert product_price_home_page == product_price_product_price, 'Product prices if different'

def test_add_item_to_cart_and_continue_shopping(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.add_product_to_cart()
    home_page.check_success_message_is_displayed()
    home_page.click_continue_shopping_in_success_modal()
    home_page.check_success_modal_disappeared()
    expect(page).to_have_url(home_page.BASE_URL)

@pytest.mark.parametrize('number', [randint(1, 10), randint(1, 10), randint(1, 10)])
def test_add_item_to_cart_and_go_to_cart(page, number):
    home_page = HomePage(page)
    home_page.navigate()

    product_name_home_page = home_page.get_product_title(item_number=number)
    home_page.add_product_to_cart(item_number=number)
    home_page.go_to_cart_through_success_modal()

    cart_page = CartPage(page)
    product_name_cart_page = cart_page.get_product_name(item_number=number)

    cart_page.check_no_empty_cart_text()
    assert product_name_home_page == product_name_cart_page, 'Product name from Home Page != product name from cart'



