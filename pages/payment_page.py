import re
from ui_element import UiElement
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import pathlib
class PaymentPage(BasePage):

    dress_name_label = UiElement(By.CLASS_NAME, 'product-name')
    attributes_label = UiElement(By.XPATH, "//td[@class='cart_description']/small/a")
    product_availibility = UiElement(By.XPATH, "//td[@class='cart_avail']/span")
    product_unit_price = UiElement(By.XPATH, "//td[@class='cart_unit']/span/span")
    product_quantity = UiElement(By.XPATH, "//td[contains(@class,'cart_quantity')]/span")
    product_total_price = UiElement(By.XPATH, "//td[@class='cart_total']/span")
    cart_info_price = UiElement(By.ID, "ajax_block_products_total")
    cart_info_shipping_price = UiElement(By.ID, "total_shipping")
    cart_info_total_price_without_tax = UiElement(By.ID, "total_price_without_tax")
    cart_info_tax = UiElement(By.ID, "total_tax")
    cart_info_total_price = UiElement(By.ID, "total_price")
    proceed_to_checkout_button = UiElement(By.CLASS_NAME, "standard-checkout")
    bank_wire_link = UiElement(By.XPATH, "//*[@title='Pay by bank wire']")
    order_summary = UiElement(By.CLASS_NAME, "cheque-box")
    order_confirmation = UiElement(By.CLASS_NAME, "box")
    confirm_order_button = UiElement(By.XPATH, "//button[contains(., 'I confirm my order')]")

    def __init__(self, driver):
        BasePage.__init__(self, driver, "http://automationpractice.com/index.php?controller=order")

    def proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()

    def pay_by_bank_wire(self):
        self.bank_wire_link.click()

    def verify_order_summary(self, total_price):
        actual = self.order_summary.get_attribute("innerHTML")
        with open(pathlib.Path(__file__).parent.absolute().joinpath("..\\data\\order_summary.txt")) as f:
            expected = f.read()
            expected = expected.replace("{total_amount}", total_price)
            assert actual.strip() == expected.strip()

    def verify_order_confirmation(self, total_price):
        actual = self.order_confirmation.get_attribute("innerHTML")
        with open(pathlib.Path(__file__).parent.absolute().joinpath("..\\data\\order_confirmation.txt")) as f:
            expected = f.read()
            expected = expected.replace("{total_amount}", total_price)
            actual = re.sub("reference.*in", "reference in", actual)
            assert actual.strip() == expected.strip()

    def confirm_order(self):
        self.confirm_order_button.click()