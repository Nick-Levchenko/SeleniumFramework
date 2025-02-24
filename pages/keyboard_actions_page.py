import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from elements.input_element import InputElement
from elements.text_element import LabelElement
from pages.base_page import BasePage
from utils.browser import Browser


class KeyboardActionsPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//input")
    SLIDER = (By.XPATH, "//*[@id='content']//input")
    RANGE_VALUE = (By.ID, "range")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'KeyboardActions'
        self.unique_element = LabelElement(self.driver, self.UNIQUE_ELEMENT_LOC, self.page_name)
        self.range_value = LabelElement(self.driver, self.RANGE_VALUE, self.page_name)
        self.slider = InputElement(self.driver, self.SLIDER, self.page_name)

    def get_min_allowed_value(self):
        slider_min_value = self.slider.get_attribute('min')
        slider_step = self.slider.get_attribute('step')
        min_allowed_value = float(slider_min_value) + float(slider_step)
        return min_allowed_value

    def get_max_allowed_value(self):
        slider_max_value = self.slider.get_attribute('max')
        slider_step = self.slider.get_attribute('step')
        max_allowed_value = float(slider_max_value) + float(slider_step)
        return max_allowed_value

    def move_slider(self):
        slider_max_value = self.slider.get_attribute('max')
        slider_step = self.slider.get_attribute('step')
        max_step = int(float(slider_max_value) / float(slider_step))
        random_list = [i for i in range(max_step) if i != 0]
        random_choice = random.choice(random_list)
        for i in range(random_choice):
            self.slider.send_keys(Keys.ARROW_RIGHT)
        return random_choice / 2
