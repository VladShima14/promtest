import pytest
from selenium import webdriver

from pages.app import Application


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def app(browser):
    return Application(browser)
