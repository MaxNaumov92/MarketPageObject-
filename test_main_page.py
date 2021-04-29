from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import BasketPageLocators
import pytest


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # Инициализируем PageObject, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                    # Открываем страницу
    page.go_to_login_page()       # Выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Гость открывает главную страницу
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    # Получаем методы страницы корзины
    basket_page = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине нет товаров
    basket_page.basket_has_no_products_check(*BasketPageLocators.CARD_CONTENT_NUMBER_OF_PRODUCTS), \
        "You have something in your basket!"
    # Ожидаем, что есть текст о том, что корзина пуста
    basket_page.basket_has_empty_basket_text_check(*BasketPageLocators.CARD_CONTENT_HOLDER), \
        "Your basket is not empty!"



