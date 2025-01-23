from selenium import webdriver
from selenium.webdriver.common.alert import Alert

from utils.logger import Logger


class Browser:

    def __init__(self):
        self.name = "Browser"
        self.driver = webdriver.Chrome()
        self.alert = Alert(self.driver)
        self.logger = Logger().getLogger()

    def get(self, url):
        self.logger.info(f"{self.name} get: {url}")
        self.driver.get(url)

    def quit(self):
        self.logger.info(f"{self.name} quit")
        self.driver.quit()

    def switch_to_alert(self):
        self.logger.info(f"{self.name} switch to alert")
        return self.driver.switch_to.alert

    def current_url(self):
        self.logger.info(f"{self.name} current url")
        return self.driver.current_url
