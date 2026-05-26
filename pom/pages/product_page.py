from playwright.sync_api import Page
from .base_page import BasePage

class ProductPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.product_title = page.locator("div.product-information > h2").describe('PRODUCT PAGE - Product title')
        self.product_price = page.locator("div.product-information > span > span").describe('PRODUCT PAGE - Product price')

    def get_product_title(self) -> str:
        return self.get_text(self.product_title)

    def get_product_price(self) -> str:
        return self.get_text(self.product_price)