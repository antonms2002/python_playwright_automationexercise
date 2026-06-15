from faker import Faker
from pom.pages.home_page import HomePage
from pom.pages.login_page import LoginPage
from pom.pages.sign_up_form_page import SignUpForm

def test_login(page):
    home_page = HomePage(page)
    home_page.navigate()
    home_page.navbar.go_to_login()
    login_page = LoginPage(page)
    login_page.check_login_page_is_present()
    login_page.login(login=login_page.default_login, password=login_page.default_password)
    login_page.navbar.check_is_logout_link_displayed()

def test_login_invalid_creds(page, fake):
    login_page = LoginPage(page)
    login_page.navigate(path=login_page.path)
    login_page.login(login=fake.email(), password=fake.password())
    login_page.check_invalid_login_message()

def test_sign_up_valid(page, fake: Faker):
    # -- Generate email, password for check request body --
    email = fake.email()
    password = fake.password()
    # -- Test --
    login_page = LoginPage(page)
    login_page.navigate(path=login_page.path)
    login_page.sign_up_fill_form_and_go_to_create_account(name=fake.first_name(), email=email)

    sign_up_form = SignUpForm(page)
    request_body = sign_up_form.sign_up(password=password, first_name=fake.first_name(), last_name=fake.last_name(),
                         address=fake.address(), state=fake.state(), city=fake.city(), zipcode=fake.zipcode(),
                         mobile_number=fake.phone_number())
    assert request_body['password'] == password, (f'Entered password: {password},'
                                                       f' password in request body: {request_body['password']}')
    assert request_body['email_address'] == email, (f'Entered password: {email},'
                                                       f' password in request body: {request_body['email_address']}')
    sign_up_form.check_account_created_tittle()
    sign_up_form.click_continue_button()
    sign_up_form.navbar.check_is_logout_link_displayed()



