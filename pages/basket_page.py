from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.is_not_element_present(*BasketPageLocators.NONEMPTY_BASKET_HEADER)
        pass

    def should_be_basket_is_empty_text(self):
        self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT)
        pass