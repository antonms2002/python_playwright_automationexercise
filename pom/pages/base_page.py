from playwright.sync_api import Page
from config import BASE_URL
import logging

class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.BASE_URL = BASE_URL
        self.log = logging.getLogger(__name__)

    def navigate(self, path: str = '') -> None:
        self.log.info('Navigating to: ' + self.BASE_URL + path)
        self.page.goto(f"{self.BASE_URL}{path}")

    def click(self, selector) -> None:
        self.log.info('Clicking: ' + selector)
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        self.log.info(f'Filling in field "{selector}": {text}')
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        self.log.info('Getting text from: ' + selector)
        return self.page.text_content(selector)

    def get_page_url(self) -> str:
        return self.page.url