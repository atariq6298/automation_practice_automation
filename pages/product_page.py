from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from ui_element import UiElement


class ProductPage(BasePage):

    quantity_field = UiElement(By.ID, "quantity_wanted")
    size_dropdown = UiElement(By.ID, "group_1")
    black_color_piker_link = UiElement(By.NAME, "Black")
    add_to_cart_button = UiElement(By.NAME, "Submit")
    product_price_label = UiElement(By.ID, "our_price_display")
    def __init__(self, driver):
        BasePage.__init__(self, driver, "http://automationpractice.com/index.php?id_product=*&controller=product")

    def pick_black_color(self, color: str):
        if color.lower() == 'black':
            self.black_color_piker_link.click()

    def select_size(self,size):
        self.size_dropdown.select_dropdown_value_by_text("M")

    def set_quantity(self, value):
        self.quantity_field.set_text(str(value))

    def click_add_to_cart(self):
        self.add_to_cart_button.click()