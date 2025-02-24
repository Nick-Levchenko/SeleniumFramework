from selenium.webdriver.common.by import By

from conftest import Browser
from elements.text_element import LabelElement
from pages.base_page import BasePage


class BasicAuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//p")
    SUCCESS_AUTH_TEXT = (By.XPATH, "//*[@id='content']//p")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'BasicAuthomationPage'
        self.unique_element = LabelElement(self.driver, self.UNIQUE_ELEMENT_LOC, self.page_name)
        self.success_element = LabelElement(self.driver, self.SUCCESS_AUTH_TEXT, self.page_name)
