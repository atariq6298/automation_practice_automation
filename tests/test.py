import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
import json
from pages.payment_page import PaymentPage
from pages.shipping_page import ShippingPage
from pages.address_page import AddressPage
from browser import Browser
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from components.cart_component import CartComponent
from pages.summary_page import SummaryPage
import pathlib

class TestClass(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = Browser.get_chrome_browser()
        self.driver.get("http://www.automationpractice.com")
        with open(pathlib.Path(__file__).parent.absolute().joinpath("..\\data\\product_data.json")) as f:
            self.product_data = json.loads(f.read())



    def test_e2e(self):

        self.login()
        self.search_black_products()
        self.add_to_cart()
        self.verify_cart_component()
        self.verify_summary_page()
        self.add_comment_in_address_page()
        self.verify_shipping_and_agree_to_terms()
        self.verify_payment_page()
        self.pay_by_bank_wire()

    def login(self):
        landing_page = LandingPage(self.driver)
        landing_page.click_sign_in_link()
        login_page = LoginPage(self.driver)
        login_page.login_to_website("atariq.sharafi@gmail.com", "Haider-6298")

    def search_black_products(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.search("Black")
        search_page = SearchPage(self.driver)
        product_components = search_page.get_product_components_with_color("black")
        product_components[1].click_product_link()

    def add_to_cart(self):
        product_page = ProductPage(self.driver)
        product_page.set_quantity(self.product_data["quantity"])
        product_page.select_size(self.product_data["size"])
        product_page.pick_black_color(self.product_data["color"])
        self.product_data["price"] = product_page.product_price_label.get_text()
        product_page.click_add_to_cart()

    def verify_cart_component(self):
        cart_component = CartComponent()
        assert cart_component.get_child_element_text(cart_component.attributes_label).lower() == f"{self.product_data['color']}, {self.product_data['size']}".lower()
        assert cart_component.get_child_element_text(cart_component.product_info_quantity) == self.product_data['quantity']
        assert cart_component.get_child_element_text(cart_component.product_info_total_product_price) == "$" + "{:.2f}".format(float(str(self.product_data["price"]).replace("$", "")) * int(self.product_data['quantity']))
        assert cart_component.get_child_element_text(cart_component.cart_info_shipping_price) == "$2.00"
        assert cart_component.get_child_element_text(cart_component.cart_info_price) == "$" + "{:.2f}".format(float(str(self.product_data["price"]).replace("$", "")) * int(self.product_data['quantity']))
        assert cart_component.get_child_element_text(cart_component.cart_info_total_price) == "$" + "{:.2f}".format(float(str(self.product_data["price"]).replace("$", "")) * int(self.product_data['quantity']) + 2)
        cart_component.proceed_to_checkout()


    def verify_summary_page(self):
        summary_page = SummaryPage(self.driver)
        assert summary_page.attributes_label.get_attribute("textContent").lower() == f"color : {self.product_data['color']}, size : {self.product_data['size']}".lower()
        assert summary_page.product_quantity.get_attribute("value") == self.product_data['quantity']
        assert summary_page.product_total_price.get_attribute("textContent").strip() == "$" + "{:.2f}".format(float(str(self.product_data["price"]).replace("$", "")) * int(self.product_data['quantity']))
        assert summary_page.product_unit_price.get_attribute("textContent") == self.product_data["price"]
        assert summary_page.cart_info_shipping_price.get_attribute("textContent") == "$2.00"
        assert summary_page.product_total_price.get_attribute("textContent").strip() == "$" + "{:.2f}".format(float(str(self.product_data["price"]).replace("$", "")) * int(self.product_data['quantity']))
        assert summary_page.cart_info_total_price_without_tax.get_attribute("textContent") == "$" + "{:.2f}".format(float(str(self.product_data["price"]).replace("$", "")) * int(self.product_data['quantity']) + 2)
        assert summary_page.cart_info_tax.get_attribute("textContent") == "$0.00"
        assert summary_page.cart_info_total_price.get_attribute("textContent") == "$" + "{:.2f}".format(float(str(self.product_data["price"]).replace("$", "")) * int(self.product_data['quantity']) + 2)
        summary_page.proceed_to_checkout()

    def add_comment_in_address_page(self):
        address_page = AddressPage(self.driver)
        address_page.write_message("Handle Carefully")
        address_page.proceed_to_checkout()

    def verify_shipping_and_agree_to_terms(self):
        shipping_page = ShippingPage(self.driver)
        assert shipping_page.delivery_option_exists()
        assert shipping_page.delivery_price_exists()
        shipping_page.agree_to_terms()
        shipping_page.proceed_to_checkout()

    def verify_payment_page(self):
        payment_page = PaymentPage(self.driver)
        assert payment_page.attributes_label.get_attribute("textContent").lower() == f"color : {self.product_data['color']}, size : {self.product_data['size']}".lower()
        assert payment_page.product_quantity.get_attribute("textContent").strip() == self.product_data['quantity']
        assert payment_page.product_total_price.get_attribute("textContent").strip() == "$" + "{:.2f}".format(float(str(self.product_data["price"]).replace("$", "")) * int(self.product_data['quantity']))
        assert payment_page.product_unit_price.get_attribute("textContent") == self.product_data["price"]
        assert payment_page.cart_info_shipping_price.get_attribute("textContent") == "$2.00"
        assert payment_page.product_total_price.get_attribute("textContent").strip() == "$" + "{:.2f}".format(float(str(self.product_data["price"]).replace("$", "")) * int(self.product_data['quantity']))
        assert payment_page.cart_info_total_price.get_attribute("textContent") == "$" + "{:.2f}".format(float(str(self.product_data["price"]).replace("$", "")) * int(self.product_data['quantity']) + 2)
        self.product_data["total_price"] = payment_page.cart_info_total_price.get_attribute("textContent")

    def pay_by_bank_wire(self):
        payment_page = PaymentPage(self.driver)
        payment_page.pay_by_bank_wire()
        payment_page.verify_order_summary(self.product_data["total_price"])
        payment_page.confirm_order()
        payment_page.verify_order_confirmation(self.product_data["total_price"])

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
