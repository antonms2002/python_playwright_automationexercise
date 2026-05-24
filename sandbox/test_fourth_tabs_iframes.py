from playwright.sync_api import Page, expect, BrowserContext
from time import sleep

def test_switch_to_new_tab(page: Page, context: BrowserContext):
    page.goto('https://octobrowser.net/')
    with context.expect_page() as new_tab_event:
        page.locator('a[href^="https://blog."]').first.click()
        new_tab = new_tab_event.value
    expect(new_tab.get_by_role("button", name="Search Icon")).to_be_visible()

def test_switch_to_iframe(page: Page):
    page.goto('https://www.qa-practice.com/elements/iframe/iframe_page')
    frame = page.frame_locator('iframe')
    expect(frame.locator("h1.fw-light")).to_have_text("Album example")
