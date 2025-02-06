from selenium.webdriver.support.wait import WebDriverWait

from utils.browser import Browser
from utils.config_reader import ConfigReader


class BasePage:
    UNIQUE_ELEMENT_LOC = None
    CONFIG = ConfigReader()

    def __init__(self, driver):
        self.driver: Browser = driver
        self.page_name = None
        self.unique_element = None
        self.wait = WebDriverWait(self.driver.driver, self.CONFIG.read_driver_config('timeout'))

    def wait_for_opening(self):
        self.unique_element.wait_for_presence()
