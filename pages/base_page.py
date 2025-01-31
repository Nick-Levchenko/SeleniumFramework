from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.config_reader import ConfigReader
from utils.logger import Logger


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger.getlogger()
        self.page_name = None
        self.unique_element = None
        self.config = ConfigReader()
        self.wait = WebDriverWait(self.driver.driver, self.config.read_driver_config('timeout'))

    def wait_for_opening(self):
        self.unique_element.wait_for_presence()

    def get_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        return alert.text
