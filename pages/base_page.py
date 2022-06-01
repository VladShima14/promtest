from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators import LoginFormLocators


class BasePage:
    def __init__(self, browser, timeout=30):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, url):
        self.browser.get(url)

    def click_on_element(self, how, what, timeout=5):
        WebDriverWait(self.browser, timeout) \
            .until(EC.element_to_be_clickable((how, what))) \
            .click()

    def fill_field(self, how, where, input_text, timeout=5):
        element = WebDriverWait(self.browser, timeout) \
            .until(EC.visibility_of_element_located((how, where)))
        element.clear()
        element.send_keys(input_text)

    def is_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout)\
                .until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return True

    def login_use_email(self, email, password):
        self.click_on_element(*LoginFormLocators.SIGN_IN_BUTTON)
        self.click_on_element(*LoginFormLocators.SIGN_IN_WITH_EMAIL_BUTTON)
        self.fill_field(*LoginFormLocators.EMAIL_INPUT_FIELD, email)
        self.click_on_element(*LoginFormLocators.SUBMIT_SIGN_IN_WITH_EMAIL_BUTTON)
        self.fill_field(*LoginFormLocators.PASSWORD_INPUT_FIELD, password)
        self.click_on_element(*LoginFormLocators.SUBMIT_SIGN_IN_AFTER_PASSWORD_INPUT)
