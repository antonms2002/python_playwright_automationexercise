from .base_page import BasePage
from config import EMAIL_LOGIN, PASSWORD_LOGIN
from playwright.sync_api import expect

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        # === Default credentials ===
        self.default_login = EMAIL_LOGIN
        self.default_password = PASSWORD_LOGIN

        # === Locators ===
        self.login_email_field = page.locator('[data-qa="login-email"]').describe('LOGIN PAGE - email field')
        self.login_password_field = page.locator('[data-qa="login-password"]').describe('LOGIN PAGE - password field')
        self.signup_name_field = page.locator('[data-qa="signup-name"]').describe('LOGIN PAGE - sign up name field')
        self.signup_email_field = page.locator('[data-qa="signup-email"]').describe('LOGIN PAGE - sign up email field')
        self.login_button = page.locator('[data-qa="login-button"]').describe('LOGIN PAGE - login button')
        self.signup_button = page.locator('[data-qa="signup-button"]').describe('LOGIN PAGE - signup button')

    def check_login_page_is_present(self):
        self.log.info('Check is email field visible')
        expect(self.login_email_field).to_be_visible()
        self.log.info('Check is password field visible')
        expect(self.login_password_field).to_be_visible()
        self.log.info('Check is sign up name field visible')
        expect(self.signup_name_field).to_be_visible()
        self.log.info('Check is sign up email field visible')
        expect(self.signup_email_field).to_be_visible()
        self.log.info('Check is login button visible')
        expect(self.login_button).to_be_visible()
        self.log.info('Check is signup button visible')
        expect(self.signup_button).to_be_visible()

    def login(self, login: str, password: str):
        self.fill(self.login_email_field, login)
        self.fill(self.login_password_field, password)
        self.click(self.login_button)


