from playwright.sync_api import Page
from pom.pages.home_page import HomePage
from pom.pages.product_page import ProductPage

def test_catalogue_title(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.check_catalogue_title()
    home_page.check_first_product_is_displayed()

def test_product_title_price_same_in_details(page: Page):
    home_page = HomePage(page)
    home_page.navigate()
    product_title_home_page = home_page.get_first_product_title()
    product_price_home_page = home_page.get_frist_product_price()
    home_page.go_to_first_product_page()
    # handling add in iframe
    # home_page.close_iframe_ad()
    product_page = ProductPage(page)
    product_title_product_page = product_page.get_product_title()
    product_price_product_price = product_page.get_product_price()
    assert product_title_home_page == product_title_product_page, 'Product titles is different'
    assert product_price_home_page == product_price_product_price, 'Product prices if different'
