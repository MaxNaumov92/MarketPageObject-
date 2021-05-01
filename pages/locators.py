from selenium.webdriver.common.by import By


class BasePageLocators():
    # Локатор для перехода по ссылке Войти или зарегистрироваться
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_PAGE_LINK = (By.CSS_SELECTOR, "span.btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

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
    # Локатор кнопки "Добавить в корзину"
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    # Локатор элемента с названием продукта
    PRODUCT_NAME = (By.CSS_SELECTOR, ".breadcrumb .active")
    # Локатор элемента с ценой продукта
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    # Локатор элемента названия продукта из сообщения о добавлении в корзину
    PRODUCT_NAME_ADD_TO_CARD_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner strong")
    # Локатор элемента цены продукта из сообщения о добавлении в корзину
    PRODUCT_PRICE_ADD_TO_CARD_MESSAGE = (By.CSS_SELECTOR, "#messages  .alert.alert-safe.alert-noicon.alert-info strong")
    # Локатор сообщения о добавлении продукта в корзину
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in")


class BasketPageLocators():
    CARD_CONTENT_HOLDER = (By.CSS_SELECTOR, "#content_inner > p")
    CARD_CONTENT_NUMBER_OF_PRODUCTS = (By.CSS_SELECTOR, "#id_form-0-quantity")

