from playwright.sync_api import Page
import pytest
import logging
from faker import Faker

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











# @pytest.fixture()
# def page(context):
#     page: Page = context.new_page()
#     page.set_viewport_size({
#             "width": 1920,
#             "height": 1080,
#         })