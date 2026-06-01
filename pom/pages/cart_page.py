from playwright.sync_api import expect
from .base_page import BasePage

class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        # === Path ===
        self.path = 'view_cart'
        # === Locators ===
        self.cart_is_empty_text = page.locator('#empty_cart b').describe('CART PAGE: EMPTY CART TEXT')
        self.cart_is_empty_go_to_products = page.locator(
            '#empty_cart_products a').describe('CART PAGE: EMPTY CART "HERE" LINK TO PRODUCTS PAGE')

    def go_to_product_using_here_link_in_empty_cart(self):
        self.click(self.cart_is_empty_go_to_products)

    def get_empty_cart_text(self) -> str:
        return self.get_text(self.cart_is_empty_text)

    def check_empty_cart_text(self):
        expect(self.cart_is_empty_text).to_be_visible()
        expect(self.cart_is_empty_text).to_have_text('Cart is empty!')
