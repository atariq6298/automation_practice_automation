from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from ui_element import UiElement


class LoginPage(BasePage):

    email_field = UiElement(By.ID, "email")
    password_field = UiElement(By.ID, "passwd")
    sign_in_button = UiElement(By.ID, "SubmitLogin")

    def __init__(self, driver):
        BasePage.__init__(self, driver, "http://www.automationpractice.com/index.php?controller=authentication&back=my-account")

    def input_email(self, email):
        self.email_field.set_text(email)

    def input_password(self, password):
        self.password_field.set_text((password))

    def press_sin_in_button(self):
        self.sign_in_button.click()


    def login_to_website(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.press_sin_in_button()