from ui_element import UiElement
from selenium.webdriver.common.by import By

class BasePage:

    sign_in_link = UiElement(By.XPATH, "//a[@title = 'Log in to your customer account']")
    search_bar = UiElement(By.ID, "search_query_top")
    search_button = UiElement(By.NAME, "submit_search")

    def __init__(self, driver, expected_url):
        self.driver = driver
        self.expected_url = expected_url

    def click_sign_in_link(self):
        self.sign_in_link.click()

    def search(self, search_text):
        self.search_bar.set_text(search_text)
        self.search_button.click()