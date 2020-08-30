from component import UiComponent
from ui_element import UiElement
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SummaryPage(BasePage):

    dress_name_label = UiElement(By.CLASS_NAME, 'product-name')
    attributes_label = UiElement(By.XPATH, "//td[@class='cart_description']/small/a")
    product_availibility = UiElement(By.XPATH, "//td[@class='cart_avail']/span")
    product_unit_price = UiElement(By.XPATH, "//td[@class='cart_unit']/span/span")
    product_quantity = UiElement(By.CLASS_NAME, "cart_quantity_input")
    product_total_price = UiElement(By.XPATH, "//td[@class='cart_total']/span")
    cart_info_price = UiElement(By.ID, "ajax_block_products_total")
    cart_info_shipping_price = UiElement(By.ID, "total_shipping")
    cart_info_total_price_without_tax = UiElement(By.ID, "total_price_without_tax")
    cart_info_tax = UiElement(By.ID, "total_tax")
    cart_info_total_price = UiElement(By.ID, "total_price")
    proceed_to_checkout_button = UiElement(By.CLASS_NAME, "standard-checkout")

    def __init__(self, driver):
        BasePage.__init__(self, driver, "http://automationpractice.com/index.php?controller=order")

    def proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()