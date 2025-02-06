from selenium.webdriver.common.by import By

from conftest import Browser
from elements.button_element import ButtonElement
from elements.text_element import LabelElement
from pages.base_page import BasePage


class AlertsContextPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, "hot-spot")
    SELECTED_AREA = (By.ID, "hot-spot")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'AlertsContextClickPage'
        self.unique_element = LabelElement(self.driver, self.UNIQUE_ELEMENT_LOC, self.page_name)
        self.area = ButtonElement(self.driver, self.SELECTED_AREA, self.page_name)
