import pytest
from playwright.sync_api import Page, expect
import re



# def test_onliner(page: Page):
#     page.goto('https://www.onliner.by/')
#     page.get_by_role("link", name="Электроника").click()
#     expect(page.get_by_text("Популярные разделы")).to_be_visible()

def test_catalogue(page: Page):
    page.goto('https://www.onliner.by/')
    page.get_by_role("link", name="Автобарахолка").first.click()
    #page.get_by_placeholder("от").first.type("100000")
    page.locator('.vehicle-interaction__state').first.click()
    #prices = page.locator(".vehicle-form__offers-part_price > .vehicle-form__description_primary ").all()
    page.locator('.vehicle-form__offers-item').first.click()
    expect(page.locator(".jest-all-cars")).to_have_text("Все автомобили")

    #assert int(prices[3].text_content()) > 10000
