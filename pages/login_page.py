from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_HOLDER), \
            "ENTER-EMAIl holder is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_HOLDER), \
            "ENTER-PASSWORD holder is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_ENTER_BUTTON), \
            "ENTER button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL_HOLDER), \
            "REG-EMAIL holder is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_HOLDER), \
            "REG-PASSWORD holder is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_APPROVE_HOLDER), \
            "REG-PASSWORD-APPROVE holder is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_REGISTRATION_BUTTON), \
            "REG-BUTTON is not presented"
