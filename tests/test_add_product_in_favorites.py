import pytest

from src.links import Links
from src.user_data import UserData

# product_link_ru = "https://prom.ua/p712545800-pokrishka-schwalbe-marathon.html"
# product_link_ua = "https://prom.ua/ua/p712545800-pokrishka-schwalbe-marathon.html"


@pytest.mark.parametrize('link', Links.PRODUCT_LINKS)
def test_success_add_product_in_favorites(app, link):
    product = app.product_page
    product.open(link)
    product.login_use_email(email=UserData.EMAIL, password=UserData.PASSWORD)
    name_of_product = product.get_name_of_product()
    product.click_on_favorites_icon()
    favorites_page = app.favorites_page
    favorites_page.open(Links.FAVORITES_PRODUCT_PAGE)
    favorites_page.check_product_on_favorite_page(name_of_product=name_of_product)
