from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from elements.text_element import LabelElement
from pages.base_page import BasePage
from utils.browser import Browser
from utils.page_utils import get_count_elements


class InfinityScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    PARAGRAPH_LOC = (By.XPATH, "//*[@class='jscroll-added']")
    FOOTER = (By.ID, "page-footer")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'InfinityScrollPage'
        self.unique_element = LabelElement(self.driver, self.UNIQUE_ELEMENT_LOC, self.page_name)
        self.paragraph = LabelElement(self.driver, self.PARAGRAPH_LOC, self.page_name)
        self.action = ActionChains(self.driver.driver)

    def get_count_paragraph(self):
        return get_count_elements(self.driver, 'div', 'class', 'jscroll-added')
