from time import sleep

from playwright.sync_api import Page, Dialog


def test_handle_dialogs_page_on(page: Page):
    def dialog_handler(dialog: Dialog):
        print(dialog.message)
        dialog.accept()
    page.on("dialog", dialog_handler)
    page.goto('https://www.demoblaze.com/')
    page.locator("#tbodyid [src$='.jpg']").first.click()
    page.get_by_role("link", name="Add to cart").click()
    sleep(3)
    page.locator('#cartur').click()

# page.once works like .on, but it handles only 1 event
# created lambda-handler
def test_handle_dialogs_page_once(page: Page):
    page.once("dialog", lambda dialog: dialog.accept())
    page.goto('https://www.demoblaze.com/')
    page.locator("#tbodyid [src$='.jpg']").first.click()
    page.get_by_role("link", name="Add to cart").click()
    sleep(3)  # just waiting alert
    page.locator('#cartur').click()

# with page.expect_event - capturing event after some actions.
def test_dandle_dialogs_page_expect_event(page: Page):
    page.goto('https://www.demoblaze.com/')
    page.locator("#tbodyid [src$='.jpg']").first.click()
    with page.expect_event("dialog", timeout=5000) as dialog:
        page.get_by_role("link", name="Add to cart").click()
    dialog.value.accept()
    page.locator('#cartur').click()

