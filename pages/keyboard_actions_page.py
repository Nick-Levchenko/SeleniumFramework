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
        self.slider_max_value = self.slider.get_attribute('max')
        self.slider_step = self.slider.get_attribute('step')

    def move_slider(self):
        max_step = int(float(self.slider_max_value) / float(self.slider_step))
        random_list = [i for i in range(max_step) if i != 0]
        random_choice = random.choice(random_list)
        for i in range(random_choice):
            self.slider.send_keys(Keys.ARROW_RIGHT)
        return random_choice / 2
    # а вот можно так делать? что помимо самого движения еще и возвращаем
    # значение на сколько сдвинули?
