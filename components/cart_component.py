from component import UiComponent
from ui_element import UiElement
from selenium.webdriver.common.by import By
import time
class CartComponent(UiComponent):

    dress_name_label = UiElement(By.ID, 'layer_cart_product_title')
    attributes_label = UiElement(By.ID, 'layer_cart_product_attributes')
    product_info_total_product_price = UiElement(By.ID, "layer_cart_product_price")
    product_info_quantity = UiElement(By.ID, "layer_cart_product_quantity")
    cart_info_price = UiElement(By.CLASS_NAME, "ajax_block_products_total")
    cart_info_shipping_price = UiElement(By.CLASS_NAME, "ajax_cart_shipping_cost")
    cart_info_total_price = UiElement(By.CLASS_NAME, "ajax_block_cart_total")
    proceed_to_checkout_button = UiElement(By.XPATH, ".//*[@title = 'Proceed to checkout']")

    def __init__(self,):
        UiComponent.__init__(self, By.ID, "layer_cart")
        self.wait_to_appear()
        self.wait_to_be_clickable()

    def proceed_to_checkout(self):
        self.proceed_to_checkout_button.click()

    def get_child_element_text(self, ui_element: UiElement):
        return self.get_child_element(ui_element).get_attribute("textContent")

