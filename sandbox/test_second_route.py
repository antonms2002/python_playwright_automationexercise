from time import sleep

from playwright.sync_api import Page, Route, expect
from datetime import timedelta, date
import re
from faker import Faker
from random import randint

fake = Faker()

def test_create_booking(page: Page):
    start_date = date.today() + timedelta(days=randint(1000, 2000))
    booking_dates = f"?checkin={start_date}&checkout={start_date + timedelta(days=3)}"
    page.goto(f"https://automationintesting.online/reservation/2{booking_dates}")
    page.locator("#doReservation").click()

    page.get_by_placeholder("Firstname").fill(fake.first_name())
    page.get_by_placeholder("Lastname").fill(fake.last_name())
    page.get_by_placeholder("Email").fill(fake.email())
    page.get_by_placeholder("Phone").fill(fake.phone_number())
    page.get_by_role("button", name="Reserve Now").click()

    expect(page.locator("h2.card-title")).to_have_text("Booking Confirmed")

def test_route_change_request_body(page: Page):
    start_date = date.today() + timedelta(days=randint(100, 500))
    booking_dates = f"?checkin={start_date}&checkout={start_date+timedelta(days=3)}"
    def change_booking_request(route: Route):
        response = route.fetch()
        response_body = response.json()
        if response.status != 201:
            raise AssertionError(f"Response status expected: 201, actual {response.status}")

        print(response.status, response_body)
        route.fulfill(response=response, json={"error":"Failed to create booking"} ,status=400)

    page.route(re.compile("/api/booking$"), change_booking_request)
    page.goto(f"https://automationintesting.online/reservation/2{booking_dates}")
    page.locator("#doReservation").click()

    page.get_by_placeholder("Firstname").fill(fake.first_name())
    page.get_by_placeholder("Lastname").fill(fake.last_name())
    page.get_by_placeholder("Email").fill(fake.email())
    page.get_by_placeholder("Phone").fill(fake.phone_number())
    page.get_by_role("button", name="Reserve Now").click()

    expect(page.get_by_text("This page couldn’t load")).to_be_visible()