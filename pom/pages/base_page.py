from playwright.sync_api import Page, Locator, Route, TimeoutError as TimeoutPw
from config import BASE_URL
import logging
from pom.pages.components.navbar import Navbar

class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.BASE_URL = BASE_URL
        self.log = logging.getLogger(__name__)
        self.navbar = Navbar(page)

    def navigate(self, path: str = '', block_ads: bool = True) -> None:
        if block_ads:
            self.block_ads()
        self.log.info('Navigating to: ' + self.BASE_URL + path)
        self.page.goto(f"{self.BASE_URL}{path}")

    def click(self, locator: Locator) -> None:
        self.log.info(f'Clicking: {locator.description}')
        locator.click()

    def fill(self, locator: Locator, text: str):
        self.log.info(f'Filling in field {locator.description}: {text}')
        locator.fill(text)

    def get_text(self, locator: Locator) -> str:
        self.log.info(f'Getting text from: {locator.description}')
        return locator.text_content()

    def get_page_url(self) -> str:
        return self.page.url

    def block_ads(self):
        self.log.info("Block ads enabled")
        def abort_ad_requests(request: Route):
            request.abort()
        self.page.route('**googleads**', abort_ad_requests)
        self.page.route('**googlesyndication**', abort_ad_requests)

    def close_iframe_ad(self) -> None:
        try:
            self.log.info("Trying to find and close add ...")
            self.page.frame_locator("iframe#aswift_2").locator("#dismiss-button").click(timeout=3000)
            self.log.info("Add closed")
        except TimeoutPw:
            self.log.info("Add is not found")