from .base_page import BasePage


class LandingPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        BasePage.__init__(self, driver, "http://www.automationpractice.com/")
