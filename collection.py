from ui_element import UiElement
from selenium.webdriver.common.by import By
from components.product_component import ProductComponent
from collections import Collection

class ProductComponentCollection(UiElement):

    def __init__(self):
        UiElement.__init__(self, By.XPATH, "//ul[contains(@class, 'product_list')]/li")

    def get_length(self):
        return len(self.get_all_elements())

    def get_product_component_at_index(self, index):
        return ProductComponent(index)