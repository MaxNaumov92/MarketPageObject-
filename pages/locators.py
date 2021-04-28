from selenium.webdriver.common.by import By


class MainPageLocators():
    # Локатор для перехода по ссылке Войти или зарегистрироваться
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


class ProductPageLocators():
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRODUCT_NAME_ADD_TO_CARD_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner strong")
    PRODUCT_PRICE_ADD_TO_CARD_MESSAGE = (By.CSS_SELECTOR, "#messages  .alert.alert-safe.alert-noicon.alert-info strong")
