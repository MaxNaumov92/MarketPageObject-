from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        # Инициализируем PageObject, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        # Открываем страницу
        page.open()
        # Выполняем метод страницы — переходим на страницу логина
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


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
    basket_page.basket_has_no_products_check()
    # Ожидаем, что есть текст о том, что корзина пуста
    basket_page.basket_has_empty_basket_text_check()
