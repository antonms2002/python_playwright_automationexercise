from playwright.sync_api import expect
from .base_page import BasePage

class HomePage(BasePage):
    # === Selectors for BasePage methods ===
    CATALOGUE_TITLE = 'div.features_items > h2'

    def __init__(self, page):
        super().__init__(page)
        # === Locators ===
        self.view_product_link_list = page.locator('a[href^="/product_details/"]')
        self.product_cards_list = page.locator("div.features_items > div.col-sm-4")
        self.product_names_list = page.locator('div.productinfo > p')
        self.product_price_list = page.locator('div.productinfo > h2')

    def check_catalogue_title(self):
        self.log.info("Checking catalogue tittle")
        assert self.get_text(self.CATALOGUE_TITLE) == 'Features Items'

    def go_to_first_product_page(self) -> None:
        self.view_product_link_list.first.click()

    def get_first_product_title(self) -> str:
        return self.product_names_list.first.text_content()

    def get_frist_product_price(self) -> str:
        return self.product_price_list.first.text_content()

    def check_first_product_is_displayed(self):
        expect(self.product_cards_list.first).to_be_visible()
        expect(self.product_names_list.first).to_be_visible()
        expect(self.product_price_list.first).to_be_visible()

    def get_products_number(self) -> int:
        return len(self.product_cards_list.all())

