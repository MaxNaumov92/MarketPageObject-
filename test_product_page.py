from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.locators import BasketPageLocators
import pytest

# Данные для проверки страниц акционных товаров
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


# Пометка страницы ?promo=offer7 недоработанной
@pytest.mark.parametrize('number', [*range(1, 7), pytest.param(7, marks=pytest.mark.xfail), *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, number):
    # Тест проверки страниц товаров по акции
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.add_to_card_check()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Тест на проверку видимости сообщения гостем  после добавления товара в корзину (негатив)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # Тест на проверку видимости  сообщения гостем без! добавления товара в корзину (негатив)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Тест на проверку исчезновения сообщения после добавления товара в корзину
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.test_message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    # Тест наличия ссылки на LoginPage на странице продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    # Тест возможности перехода на LoginPage со страницы продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине нет товаров
    basket_page.basket_has_no_products_check(*BasketPageLocators.CARD_CONTENT_NUMBER_OF_PRODUCTS), \
        "You have something in your basket!"
    # Ожидаем, что есть текст о том, что корзина пуста
    basket_page.basket_has_empty_basket_text_check(*BasketPageLocators.CARD_CONTENT_HOLDER), \
        "Your basket is not empty!"
