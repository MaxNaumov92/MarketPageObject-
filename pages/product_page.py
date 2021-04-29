from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        # Проверка наличия акции на товар
        assert "?promo=offer" in self.browser.current_url

    def add_to_card(self):
        # Добавление товара в корзину
        self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BUTTON).click()

    def add_to_card_check(self):
        # Проверка соответствия цены и названия у добавленного в корзину товара
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ADD_TO_CARD_MESSAGE)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADD_TO_CARD_MESSAGE)
        assert product_price.text == product_price_message.text, "Wrong price of product added to card"
        assert product_name.text == product_name_message.text, "Wrong product added to card"

    def should_not_be_success_message(self):
        # Проверка отсутсвтия сообшения о добавлении товара в корзину
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self):
        # Проверка исчезновения сообшения о добавлении товара в корзину
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
