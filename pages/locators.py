from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    # Локаторы для "Войти"
    LOGIN_EMAIL_HOLDER = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_HOLDER = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_ENTER_BUTTON = (By.CSS_SELECTOR, "[name=login_submit]")
    # Локаторы для "Зарегистрироваться"
    REG_EMAIL_HOLDER = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_HOLDER = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_APPROVE_HOLDER = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")
