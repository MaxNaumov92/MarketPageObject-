from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        assert "?promo=newYear" in self.browser.current_url

    def add_to_card(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BUTTON).click()

    def add_to_card_check(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ADD_TO_CARD_MESSAGE)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_name_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADD_TO_CARD_MESSAGE)
        assert product_name == product_name_message, "Wrong product added to card"
        assert product_price == product_price_message, "Wrong price of product added to card"






        #self.solve_quiz_and_get_code()