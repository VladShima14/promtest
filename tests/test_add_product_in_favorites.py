import allure
import pytest

from src.links import Links
from src.user_data import UserData


@pytest.mark.parametrize('link', Links.PRODUCT_LINKS)
@allure.story("Test for add product in favorite list from product page")
def test_success_add_product_in_favorites(app, link):
    product = app.product_page
    with allure.step(f'Open product page with link: {link}'):
        product.open(link)
    with allure.step(f'Sing in with user data: {UserData.EMAIL}, {UserData.PASSWORD}'):
        product.login_use_email(email=UserData.EMAIL, password=UserData.PASSWORD)
    with allure.step('Get product name'):
        name_of_product = product.get_name_of_product()
    with allure.step('Click on favorite icon'):
        product.click_on_favorites_icon()
    favorites_page = app.favorites_page
    with allure.step('Open favorites page'):
        favorites_page.open(Links.FAVORITES_PRODUCT_PAGE)
    favorites_page.check_product_on_favorite_page(name_of_product=name_of_product)
