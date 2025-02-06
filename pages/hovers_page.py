from selenium.webdriver.common.by import By

from elements.text_element import LabelElement
from pages.base_page import BasePage
from utils.browser import Browser
from utils.page_utils import get_locator_by_index


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'HoversPage'
        self.unique_element = LabelElement(self.driver, self.UNIQUE_ELEMENT_LOC, self.page_name)

    def move_to_hover(self, username):
        self.driver.action.move_to_element(get_locator_by_index(self.driver, username, 'user_avatar')).perform()

    def check_name(self, username):
        return get_locator_by_index(self.driver, username, 'username')

    def get_user_number(self, username):
        return get_locator_by_index(self.driver, username, 'username').text[-1:]
