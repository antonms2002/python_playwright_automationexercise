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
        self.product_overlay_list = (page.locator("div.features_items > div.col-sm-4 .product-overlay").
                                     describe('HOME PAGE - Product overlay'))
        self.product_overlay_add_to_cart_list = (page.locator("div.features_items > div.col-sm-4 .product-overlay .add-to-cart").
                                                 describe('HOME PAGE - Add to cart button in product overlay'))
        self.modal_success = page.locator('#cartModal').describe('HOME PAGE - Success modal')
        self.modal_success_add_to_cart_text = (page.locator('#cartModal .modal-body > p:nth-child(1)').
                                               describe('HOME PAGE > SUCCESS MODAL - Text in modal'))
        self.modal_success_add_to_cart_view_cart_link = (page.locator('#cartModal .modal-body > p:nth-child(2)').
                                                         describe('HOME PAGE > SUCCESS MODAL - View cart link'))
        self.modal_success_add_to_cart_continue_button = (page.locator('#cartModal .close-modal').
                                                          describe('HOME PAGE > SUCCESS MODAL - Continue shopping button'))

    def check_catalogue_title(self):
        self.log.info("Checking catalogue tittle")
        assert self.get_text(self.catalogue_title) == 'Features Items'

    def go_to_first_product_page(self) -> None:
        self.click(self.view_product_link_list.first)

    def get_product_title(self, item_number: int = 0) -> str:
        return self.get_text(self.product_names_list.nth(item_number))

    def get_product_price(self, item_number: int = 0) -> str:
        return self.get_text(self.product_price_list.nth(item_number))

    def check_product_is_displayed(self, item_number: int = 0):
        expect(self.product_cards_list.nth(item_number)).to_be_visible()
        expect(self.product_names_list.nth(item_number)).to_be_visible()
        expect(self.product_price_list.nth(item_number)).to_be_visible()

    def get_products_number(self) -> int:
        return len(self.product_cards_list.all())

    def add_product_to_cart(self, item_number: int = 0):
        self.product_cards_list.nth(item_number).hover()
        self.click(self.product_overlay_add_to_cart_list.nth(item_number))

    def check_success_message_is_displayed(self):
        expect(self.modal_success_add_to_cart_text).to_have_text('Your product has been added to cart.')
        expect(self.modal_success_add_to_cart_continue_button).to_be_visible()
        expect(self.modal_success_add_to_cart_continue_button).to_be_visible()

    def click_continue_shopping_in_success_modal(self):
        self.click(self.modal_success_add_to_cart_continue_button)

    def check_success_modal_disappeared(self):
        expect(self.modal_success).not_to_be_visible()

    def go_to_cart_through_success_modal(self):
        self.click(self.modal_success_add_to_cart_view_cart_link)