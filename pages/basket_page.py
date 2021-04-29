from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage


class BasketPage(BasePage):
    def basket_has_no_products_check(self, how, what, timeout):
        # Проверка пустой корзины (timeout)
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def basket_has_empty_basket_text_check(self, how, what):
        # Проверка наличия текста о пустой корзине
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
