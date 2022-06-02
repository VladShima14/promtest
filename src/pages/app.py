from src.pages.base_page import BasePage
from src.pages.favorites_page import FavoritesPage
from src.pages.product_page import ProductPage


class Application(BasePage):

    @property
    def product_page(self):
        return ProductPage(self.browser)

    @property
    def favorites_page(self):
        return FavoritesPage(self.browser)
