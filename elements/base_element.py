from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import Browser
from utils.config_reader import ConfigReader
from utils.logger import Logger


class BaseElement:
    def __init__(self, driver, locator):
        self.driver: Browser = driver
        self.config: ConfigReader = ConfigReader()
        self.wait: WebDriverWait = WebDriverWait(self.driver.driver, self.config.read_driver_config('timeout'))
        self.locator: tuple[str, str] = locator
        self.logger = Logger().getLogger()

    def click(self):
        self.logger.info(f"{__name__} use click")
        self.wait.until(EC.element_to_be_clickable(self.locator)).click()

    def get_text(self):
        self.logger.info(f"{__name__} use get_text")
        text = self.wait.until(EC.visibility_of_element_located(self.locator)).text
        self.logger.info(f"{__name__} get_text received the text '{text}'")
        return text

    def get_attribute(self, attribute_name):
        self.logger.info(f"{__name__} use get_attribute get attribute {attribute_name}")
        return self.wait.until(EC.presence_of_element_located(self.locator)).get_attribute(attribute_name)

    def is_enabled(self):
        self.logger.info(f"{__name__} use is_enabled")
        return self.wait.until(EC.presence_of_element_located(self.locator)).is_enabled()

    def is_displayed(self):
        self.logger.info(f"{__name__} use is_displayed")
        return self.wait.until(EC.visibility_of_element_located(self.locator))

    def wait_for_presence(self):
        self.logger.info(f"{__name__} use wait_for_presence")
        self.wait.until(EC.presence_of_element_located(self.locator))
