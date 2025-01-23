from selenium import webdriver

from utils.browser import Browser


class BrowserFactory:

    def __init__(self):
        self.remote_driver = Browser()
        self.driver = webdriver.Chrome()


    def get_remote_driver(self):
        return self.remote_driver

    def get_driver(self):
        return self.driver