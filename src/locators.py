from selenium.webdriver.common.by import By


class LoginFormLocators:
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[data-qaid*='sign-in']")
    SIGN_IN_WITH_EMAIL_BUTTON = (By.CSS_SELECTOR, "div[data-qaid*='email_btn']")
    EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "input[data-qaid*='input_field']")
    SUBMIT_SIGN_IN_WITH_EMAIL_BUTTON = (By.CSS_SELECTOR, "button[data-qaid*='submit_btn']")
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "input[data-qaid*='password']")
    SUBMIT_SIGN_IN_AFTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "button[data-qaid*='submit_btn']")


class ProductPageLocators:
    FAVORITE_ICON_IN_PRODUCT = (By.CSS_SELECTOR, "span[data-qaid*='add_favorite']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1[data-qaid*='product_name']")


class FavoritePageLocators:
    pass
