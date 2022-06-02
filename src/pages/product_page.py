from src.pages.base_page import BasePage
from src.locators import ProductPageLocators


class ProductPage(BasePage):

    def click_on_favorites_icon(self):
        click_status = self.browser.find_element(*ProductPageLocators.FAVORITE_ICON_IN_PRODUCT)\
            .get_attribute("data-tg-clicked")
        if '"label/label":"off"' in click_status:
            self.click_on_element(*ProductPageLocators.FAVORITE_ICON_IN_PRODUCT)
        elif '"label/label":"on"' in click_status:
            self.click_on_element(*ProductPageLocators.FAVORITE_ICON_IN_PRODUCT)
            self.click_on_element(*ProductPageLocators.FAVORITE_ICON_IN_PRODUCT)

    def get_name_of_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name
