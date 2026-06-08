from playwright.sync_api import expect
from .base_page import BasePage

class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        # === Path ===
        self.path = 'view_cart'
        # === Locators ===
        self.cart_is_empty_text = page.locator('#empty_cart b').describe('CART PAGE: Empty cart text')
        self.cart_is_empty_go_to_products = page.locator(
            '#empty_cart_products a').describe('CART PAGE: Empty cart "Here" link ')
        self.product_name = page.locator('tbody a').describe('CART PAGE: Product name')

    def go_to_product_using_here_link_in_empty_cart(self):
        self.click(self.cart_is_empty_go_to_products)

    def get_empty_cart_text(self) -> str:
        return self.get_text(self.cart_is_empty_text)

    def check_empty_cart_text(self):
        expect(self.cart_is_empty_text).to_be_visible()
        expect(self.cart_is_empty_text).to_have_text('Cart is empty!')

    def check_no_empty_cart_text(self):
        expect(self.cart_is_empty_text).not_to_be_visible()

    def get_product_name(self, item_number: int = 0) -> str:
        return self.get_text(self.product_name.nth(item_number))
