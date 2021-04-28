from .pages.product_page import ProductPage


def test_add_to_card_check(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.add_to_card_check()
