from pom.pages.sign_up_form_page import SignUpForm
from pom.pages.login_page import LoginPage
from playwright.sync_api import Page
from faker import Faker

def sign_up_new_user_and_save_storage_state(page: Page, fake: Faker):
    login_page = LoginPage(page)

    login_page.navigate(path=login_page.path)
    login_page.sign_up_fill_form_and_go_to_create_account(name=fake.first_name(), email=fake.email())

    sign_up_form = SignUpForm(page)
    sign_up_form.sign_up(password=fake.password(), first_name=fake.first_name(), last_name=fake.last_name(),
                         address=fake.address(), state=fake.state(), city=fake.city(), zipcode=fake.zipcode(),
                         mobile_number=fake.phone_number())

    sign_up_form.check_account_created_tittle()
    page.context.storage_state(path="state.json")