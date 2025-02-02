from selenium import webdriver

from utils.browser import Browser


class BrowserFactory:

    @staticmethod
    def get_driver():
        return webdriver.Chrome()

    @staticmethod
    def get_browser():
        return Browser()
