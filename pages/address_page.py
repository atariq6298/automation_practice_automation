from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from ui_element import UiElement


class AddressPage(BasePage):

    message_field = UiElement(By.NAME, "message")
    proceed_to_checkout_button = UiElement(By.NAME, "processAddress")

    def __init__(self, driver):
        BasePage.__init__(self, driver, "http://www.automationpractice.com/index.php?controller=authentication&back=my-account")

    def write_message(self, message):
        self.message_field.set_text(message)

    def proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()