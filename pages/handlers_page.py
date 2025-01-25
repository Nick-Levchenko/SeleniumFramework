from selenium.webdriver.common.by import By

from elements.button_element import ButtonElement
from elements.text_element import TextElement
from pages.base_page import BasePage
from utils.browser import Browser


class HandlersPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//*[@target='_blank']")
    NEW_WINDOW_TEXT = (By.CSS_SELECTOR, 'h3')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'HandlersPage'
        self.unique_element = ButtonElement(self.driver, self.UNIQUE_ELEMENT_LOC)
        self.button = ButtonElement(self.driver, self.UNIQUE_ELEMENT_LOC)
        self.window_text = TextElement(self.driver, self.NEW_WINDOW_TEXT)

    def click_new_window(self):
        self.logger.info(f'Click new window button')
        self.button.click()

    def switch_to_window(self, window_number):
        self.logger.info(f'Switch window number {window_number}')
        self.driver.switch_to_window(window_number)

    def get_all_windows(self):
        self.logger.info(f'Get all windows')
        return self.driver.driver.window_handles
