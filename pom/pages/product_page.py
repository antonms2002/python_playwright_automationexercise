from playwright.sync_api import Page

class ProductPage:

    def __init__(self, page: Page):
        self.product_title = page.locator("div.product-information > h2")
        self.product_price = page.locator("div.product-information > span > span")

    def get_product_title(self) -> str:
        return self.product_title.text_content()

    def get_product_price(self) -> str:
        return self.product_price.text_content()