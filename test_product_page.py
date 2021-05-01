import pytest
import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


# Данные для проверки страниц акционных товаров
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]



@pytest.mark.need_review
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

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # Тест возможности перехода на LoginPage со страницы продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()
    # Получаем методы страницы корзины
    basket_page = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине нет товаров
    basket_page.basket_has_no_products_check()
    # Ожидаем, что есть текст о том, что корзина пуста
    basket_page.basket_has_empty_basket_text_check()

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    # Тесты для зарегистрированного пользователя
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        foo = email.split('.')
        password = foo[0]
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(email=email, password=password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Тест на проверку видимости  сообщения гостем без! добавления товара в корзину (негатив)
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        # Тест проверки страницы товара по акции
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        page.add_to_card()
        page.solve_quiz_and_get_code()
        page.add_to_card_check()
