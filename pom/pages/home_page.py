from playwright.sync_api import expect
from .base_page import BasePage

class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        # === Locators ===
        self.catalogue_title = page.locator('div.features_items > h2').describe('HOME PAGE - Catalogue tittle')
        self.view_product_link_list = page.locator('a[href^="/product_details/"]').describe('HOME PAGE - View product link')
        self.product_cards_list = page.locator("div.features_items > div.col-sm-4").describe('HOME PAGE - Product card')
        self.product_names_list = page.locator('div.productinfo > p').describe('HOME PAGE - Product name')
        self.product_price_list = page.locator('div.productinfo > h2').describe('HOME PAGE - Product price')

    def check_catalogue_title(self):
        self.log.info("Checking catalogue tittle")
        assert self.get_text(self.catalogue_title) == 'Features Items'

    def go_to_first_product_page(self) -> None:
        self.click(self.view_product_link_list.first)

    def get_first_product_title(self) -> str:
        return self.get_text(self.product_names_list.first)

    def get_frist_product_price(self) -> str:
        return self.get_text(self.product_price_list.first)

    def check_first_product_is_displayed(self):
        expect(self.product_cards_list.first).to_be_visible()
        expect(self.product_names_list.first).to_be_visible()
        expect(self.product_price_list.first).to_be_visible()

    def get_products_number(self) -> int:
        return len(self.product_cards_list.all())

