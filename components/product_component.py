from component import UiComponent
from ui_element import UiElement
from selenium.webdriver.common.by import By

class ProductComponent(UiComponent):
    BLACK_COLOR = 'background: rgb(241, 196, 15);'
    add_to_cart_button = UiElement(By.XPATH, "//span[text()='Add to cart']//parent::a")
    colors = UiElement(By.CLASS_NAME, "color_pick")
    in_stock_indication = UiElement(By.CLASS_NAME, "available-now")
    product_name_label = UiElement(By.CLASS_NAME, "product-name")
    product_price_label = UiElement(By.XPATH, "//span[@class = 'price product-price' and @itemprop = 'price']")
    product_link = UiElement(By.CLASS_NAME, "product_img_link")

    def __init__(self, index):
        locator = f"//ul[contains(@class, 'product_list')]/li[{str(index)}]"
        UiComponent.__init__(self, By.XPATH, locator)

    def is_in_stock(self):
        return self.child_element_exists(self.in_stock_indication)

    def color_available(self, color):
        colors = self.get_child_elements(self.colors)
        for a_color in colors:
            if color in str(a_color.get_attribute("href")):
                return True
        return False
    def click_product_link(self):
        self.get_child_element(self.product_link).click()
