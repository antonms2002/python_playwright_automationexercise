from pom.pages.cart_page import CartPage


def test_is_cart_empty_text_present(page):
    cart_page = CartPage(page)
    cart_page.navigate(path=cart_page.path)
    cart_page.check_empty_cart_text()

def test_is_cart_empty_text_present_auth_user(page_auth):
    cart_page = CartPage(page_auth)
    cart_page.navigate(path=cart_page.path, block_ads=False) # page_auth enable block_ads
    cart_page.check_empty_cart_text()