from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import Browser
from utils.config_reader import ConfigReader
from utils.logger import Logger


class BaseElement:
    CONFIG = ConfigReader()
    LOGGER = Logger().getlogger()

    def __init__(self, driver, locator, title):
        self.driver: Browser = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver.driver, self.CONFIG.read_driver_config('timeout'))
        self.locator: tuple[str, str] = locator
        self.title: str = title

    def wait_for_presence(self):
        self.LOGGER.info(f"{self.title} use wait_for_presence")
        return self.wait.until(EC.presence_of_element_located(self.locator))

    def wait_for_clickable(self):
        self.LOGGER.info(f"{self.title} use wait_for_clickable")
        return self.wait.until(EC.element_to_be_clickable(self.locator))

    def wait_until_visible(self):
        self.LOGGER.info(f"{self.title} use wait_until_visible")
        return self.wait.until(EC.visibility_of_element_located(self.locator))

    def is_enabled(self):
        self.LOGGER.info(f"{self.title} use is_enabled")
        return self.wait.until(EC.presence_of_element_located(self.locator)).is_enabled()

    def is_displayed(self):
        self.LOGGER.info(f"{self.title} use is_displayed")
        try:
            self.wait.until(EC.presence_of_element_located(self.locator)).is_displayed()
        except TimeoutException:
            return False
        return True

    def click(self):
        self.LOGGER.info(f"{self.title} use click")
        self.wait.until(EC.element_to_be_clickable(self.locator)).click()

    def get_text(self):
        self.LOGGER.info(f"{self.title} use get_text")
        return self.wait_for_presence().text

    def get_attribute(self, attribute_name):
        self.LOGGER.info(f"{self.title} use get_attribute get attribute {attribute_name}")
        return self.wait_for_presence().get_attribute(attribute_name)
