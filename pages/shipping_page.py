from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from ui_element import UiElement


class ShippingPage(BasePage):

    my_carrier_delivery_option = UiElement(By.XPATH, "//td[contains(., 'My carrier') and contains(. , 'Delivery next day!')]")
    price = UiElement(By.XPATH, "//div[@class='delivery_option_price']")
    agree_to_terms_checkbox = UiElement(By.XPATH, "//label[@for='cgv']")
    proceed_to_checkout_button = UiElement(By.NAME, "processCarrier")

    def __init__(self, driver):
        BasePage.__init__(self, driver, "http://automationpractice.com/index.php?controller=order&step=2&multi-shipping=")

    def delivery_option_exists(self):
        return self.my_carrier_delivery_option.exists()

    def delivery_price_exists(self):
        return self.price.exists()

    def agree_to_terms(self):
        if not self.agree_to_terms_checkbox.is_checked():
            self.agree_to_terms_checkbox.click()

    def proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()
