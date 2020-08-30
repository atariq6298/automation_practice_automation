from pages.base_page import BasePage
from collection import ProductComponentCollection

class SearchPage(BasePage):

    product_collection = ProductComponentCollection()

    def __init__(self, driver):
        self.driver = driver
        BasePage.__init__(self, driver, "http://www.automationpractice.com/?controller=search*")

    def get_product_components_with_color(self, color: str):
        list = []
        for i in range(1, self.product_collection.get_length() + 1):
            product_component = self.product_collection.get_product_component_at_index(i)
            if product_component.color_available(color):
                list.append(product_component)
        return list