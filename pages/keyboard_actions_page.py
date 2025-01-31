from random import randrange

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from elements.text_element import TextElement
from pages.base_page import BasePage
from utils.browser import Browser
from utils.logger import Logger


class KeyboardActionsPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    SLIDER = (By.XPATH, "//*[@id='content']//input")
    RANGE_VALUE = (By.ID, "range")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'KeyboardActions'
        self.unique_element = TextElement(self.driver, self.UNIQUE_ELEMENT_LOC)
        self.range_value = TextElement(self.driver, self.RANGE_VALUE)
        self.action = ActionChains(self.driver.driver)
        self.random = randrange(-50, 50, 10)

    def move_slider(self):
        slider = self.wait.until(EC.element_to_be_clickable(self.SLIDER))
        self.action.click_and_hold(slider).move_by_offset(self.random, 0).release().perform()

    def get_result(self):
        result = float(self.range_value.get_text())
        return result
