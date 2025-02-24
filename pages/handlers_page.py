from selenium.webdriver.common.by import By

from elements.button_element import ButtonElement
from elements.text_element import LabelElement
from pages.base_page import BasePage
from utils.browser import Browser


class HandlersPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//*[@target='_blank']")
    NEW_WINDOW_TEXT = (By.CSS_SELECTOR, 'h3')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'HandlersPage'
        self.unique_element = ButtonElement(self.driver, self.UNIQUE_ELEMENT_LOC, self.page_name)
        self.button = ButtonElement(self.driver, self.UNIQUE_ELEMENT_LOC, self.page_name)
        self.window_text = LabelElement(self.driver, self.NEW_WINDOW_TEXT, self.page_name)

    def click_new_window(self):
        self.button.click()
