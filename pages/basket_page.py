from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Ожидаем, что есть текст о том что корзина пуста
    def basket_has_empty_basket_text_check(self):
        assert self.is_element_present(*BasketPageLocators.CARD_CONTENT_HOLDER), \
            "Message 'basket is empty' is not presented"

    # Ожидаем, что в корзине нет товаров
    def basket_has_no_products_check(self):
        assert self.is_not_element_present(*BasketPageLocators.CARD_CONTENT_NUMBER_OF_PRODUCTS), \
            "Your basket is not empty!"
