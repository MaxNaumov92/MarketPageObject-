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
        assert self.browser.element_is_enabled(*LoginPageLocators.LOGIN_EMAIL_HOLDER), \
            "ENTER-EMAIl holder is not enabled"
        assert self.browser.element_is_enabled(*LoginPageLocators.LOGIN_PASSWORD_HOLDER), \
            "ENTER-PASSWORD holder is not enabled"
        assert self.browser.element_is_clickable(*LoginPageLocators.LOGIN_ENTER_BUTTON), \
            "ENTER button is not clickable"

    def should_be_register_form(self):
        assert self.browser.element_is_enabled(*LoginPageLocators.REG_EMAIL_HOLDER), \
            "REG-EMAIL holder is not presented"
        assert self.browser.element_is_enabled(*LoginPageLocators.REG_PASSWORD_HOLDER), \
            "REG-PASSWORD holder is not presented"
        assert self.browser.element_is_enabled(*LoginPageLocators.REG_PASSWORD_APPROVE_HOLDER), \
            "REG-PASSWORD-APPROVE holder is not presented"
        assert self.browser.element_is_clickable(*LoginPageLocators.REG_REGISTRATION_BUTTON), \
            "REG-BUTTON is not clickable"
