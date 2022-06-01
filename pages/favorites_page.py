from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FavoritesPage(BasePage):

    def check_product_on_favorite_page(self, name_of_product):
        assert self.is_element_present(By.XPATH, f"//a[@data-qaid='product_name' "
                                                 f"and contains(., '{name_of_product}')]"), \
            "Product was not found on the favorite page"
