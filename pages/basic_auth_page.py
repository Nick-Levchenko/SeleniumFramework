from selenium.webdriver.support.wait import WebDriverWait

from elements.text_element import TextElement
from pages.base_page import BasePage
from tests.conftest import Browser
from utils.config_reader import ConfigReader


class BasicAuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = ("xpath", "//*[@id='content']//h3")
    SUCCESS_AUTH_TEXT = ("xpath", "//*[@id='content']//p")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'BasicAuthomationPage'
        self.config = ConfigReader()
        self.wait = WebDriverWait(self.driver.driver,
                                  self.config.read_driver_config('timeout'))
        self.unique_element = TextElement(self.driver, self.UNIQUE_ELEMENT_LOC)
        self.success_element = TextElement(self.driver, self.SUCCESS_AUTH_TEXT)

    def give_format_url(self, url: str, login, password):
        self.logger.info(f'give_format_url take url = {url}')
        auth_string = f'{login}:{password}@'
        if url.startswith('https://'):
            index = 8
            final_url = url[:index] + auth_string + url[index:]
            return final_url
        elif url.startswith('http://'):
            index = 7
            final_url = url[:index] + auth_string + url[index:]
            return final_url
        formatted_url = auth_string + url

        return formatted_url, self.logger.info(f'give_format_url return formatted url = {formatted_url}')
