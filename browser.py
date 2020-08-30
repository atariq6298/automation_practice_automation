from selenium import webdriver
import os


class Browser:
    driver = None

    @staticmethod
    def get_chrome_browser():
        if Browser.driver:
            return Browser.driver
        else:
            Browser.driver = webdriver.Chrome(os.path.dirname(os.path.abspath(__file__)) + "\\drivers\\chromedriver.exe")
            return Browser.driver
