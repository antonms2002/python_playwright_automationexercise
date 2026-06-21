from playwright.sync_api import BrowserContext, Browser, Page, Cookie
import pytest
import logging
from faker import Faker
from pom.pages.login_page import LoginPage

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# context fixture depends on browser_context_args and receives it as a parameter
@pytest.fixture()
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }
    # Python 3.5+: dictionary unpacking - creates new dict preserving original
    # Python 3.9+ alternative: browser_context_args | {"viewport": {"width": 1920, "height": 1080}}

@pytest.fixture()
def fake():
    fake = Faker()
    return fake

@pytest.fixture(scope="session")
def auth_cookies(browser: Browser):
    """auth_cookies fixture returns cookies of authenticated user. Login performs once in session"""
    context: BrowserContext = browser.new_context()
    page: Page = context.new_page()
    login_page = LoginPage(page)
    login_page.navigate(path=login_page.path)
    login_page.login(login=login_page.default_login, password=login_page.default_password)
    login_page.navbar.check_is_logout_link_displayed()
    cookies = context.cookies()
    page.close()
    context.close()
    return cookies

# @pytest.fixture(scope='session')
# def context_auth(browser: Browser):
#     context = browser.new_context()
#     page = context.new_page()
#
#     login_page = LoginPage(page)
#     login_page.navigate(path=login_page.path)
#     login_page.login(login=login_page.default_login, password=login_page.default_password)
#     login_page.navbar.check_is_logout_link_displayed()
#     page.close()
#
#     yield context
#     context.close()
#
# @pytest.fixture()
# def page_auth(context_auth: BrowserContext):
#     page = context_auth.new_page()
#     yield page
#     page.close()

# @pytest.fixture()
# def page(context):
#     page: Page = context.new_page()
#     page.set_viewport_size({
#             "width": 1920,
#             "height": 1080,
#         })