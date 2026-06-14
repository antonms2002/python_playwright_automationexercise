from typing import Literal

from playwright.sync_api import Page
from playwright.sync_api import expect
from .base_page import BasePage
from config import SIGN_UP_PATH

class SignUpForm(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        # -- Page --
        self.page = page
        # -- Page path
        self.path = SIGN_UP_PATH
        # -- Locators --
        self.name_field = page.locator('[data-qa="name"]')
        self.password_filed = page.locator('[data-qa="password"]')
        self.day_date_birth_select = page.locator('[data-qa="days"]')
        self.month_date_birth_select = page.locator('[data-qa="months"]')
        self.year_date_birth_select = page.locator('[data-qa="years"]')
        self.first_name_filed = page.locator('[data-qa="first_name"]')
        self.last_name_field = page.locator('[data-qa="last_name"]')
        self.company_field = page.locator('[data-qa="company"]')
        self.address_field = page.locator('[data-qa="address"]')
        self.country = page.locator('[data-qa="country"]')
        self.state_field = page.locator('[data-qa="state"]')
        self.city_field = page.locator('[data-qa="city"]')
        self.zipcode_filed = page.locator('[data-qa="zipcode"]')
        self.mobile_number_field = page.locator('[data-qa="mobile_number"]')
        self.create_account_button = page.locator('[data-qa="create-account"]')

    def sign_up(self,
                password: str, first_name: str, last_name: str, address: str,
                state: str, city: str, zipcode: str, mobile_number: str,
                country: Literal['Canada', 'India', 'United States'] = 'India',
                day_of_birth: str = '1', month: str = 'March', year: str = '1999',
                company: str = None):
        self.fill(self.password_filed, password)
        self.fill(self.first_name_filed, first_name)
        self.fill(self.last_name_field, last_name)
        self.fill(self.address_field, address)
        self.fill(self.state_field, state)
        self.fill(self.city_field, city)
        self.fill(self.zipcode_filed, zipcode)
        self.fill(self.mobile_number_field, mobile_number)
        self.country.select_option(country)
        self.day_date_birth_select.select_option(day_of_birth)
        self.month_date_birth_select.select_option(month)
        self.year_date_birth_select.select_option(year)
        if company:
            self.fill(self.company_field, company)
        with self.page.expect_request('**/signup**') as request:
            self.click(self.create_account_button)
        request_body = request.value.post_data
        print(type(request_body))
        self.log.info(request_body)
        #assert password in request_body




