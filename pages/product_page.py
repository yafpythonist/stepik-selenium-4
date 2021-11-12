from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_add_to_basket_button()
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "No 'add to basket' button"

    def should_be_added_to_basket_notification(self):
        assert self.is_element_present(
            *ProductPageLocators.ADDED_SUCCESSFULLY_ALERT_PRODUCT_TITLE), "No 'added to basket' notification"

    def should_notify_product_added(self):
        self.should_be_added_to_basket_notification()
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text == self.browser.find_element(
            *ProductPageLocators.ADDED_SUCCESSFULLY_ALERT_PRODUCT_TITLE).text, "Product name mismatch"

    def should_be_basket_total_notification(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_TOTAL_ALERT_TOTAL_VALUE), "No 'basket total' notification"

    def should_notify_basket_total(self):
        self.should_be_basket_total_notification()
        assert self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL_ALERT_TOTAL_VALUE).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text, "Product price mismatch"

    def should_not_notify_product_added(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ADDED_SUCCESSFULLY_ALERT_PRODUCT_TITLE), "Notified of added product while souldn't"

    def should_remove_notification_product_added(self):
        assert self.is_disappeared(
            *ProductPageLocators.ADDED_SUCCESSFULLY_ALERT_PRODUCT_TITLE), "added product notification was not removed"
