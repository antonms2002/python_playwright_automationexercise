from playwright.sync_api import Page, expect

class Navbar:

    def __init__(self, page: Page):
        # === Locators ===
        self.home = page.locator('ul > li > a[href="/"]')
        self.products = page.locator('ul > li > a[href="/products"]')
        self.cart = page.locator('ul > li > a[href="/view_cart"]')
        self.login = page.locator('ul > li > a[href="/login"]')
        self.logout = page.locator('ul > li > a[href="/logout"]')

    def go_to_home(self):
        self.home.click()

    def go_to_products(self):
        self.products.click()

    def go_to_cart(self):
        self.cart.click()

    def go_to_login(self):
        self.login.click()

    def logout_from_account(self):
        self.logout.click()

    def check_is_logout_link_displayed(self):
        expect(self.logout).to_be_visible()