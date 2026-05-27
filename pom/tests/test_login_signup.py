from pom.pages.home_page import HomePage
from pom.pages.login_page import LoginPage

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