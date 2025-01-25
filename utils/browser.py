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

    def close(self):
        self.logger.info(f"{self.name} close")
        self.driver.close()

    def switch_to_alert(self):
        self.logger.info(f"{self.name} switch to alert")
        return self.driver.switch_to.alert

    def current_url(self):
        self.logger.info(f"{self.name} current url")
        return self.driver.current_url

    def switch_to_window(self, window_number):
        self.logger.info(f"{self.name} switch to window {window_number}")
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def switch_to_frame(self, frame):
        self.logger.info(f"{self.name} switch to frame {frame}")
        self.driver.switch_to.frame(frame)

    def switch_to_previous_frame(self):
        self.logger.info(f"{self.name} switch to previous frame")
        self.driver.switch_to.parent_frame()
