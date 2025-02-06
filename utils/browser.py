from selenium.common import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.browser_factory import BrowserFactory
from utils.logger import Logger


class Browser:

    def __init__(self, options):
        self.name = "Browser"
        self.driver = BrowserFactory.get_driver(options)
        self.alert = Alert(self.driver)
        self.logger = Logger().getlogger()
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def get(self, url):
        self.logger.info(f"{self.name} get: {url}")
        self.driver.get(url)

    def back(self):
        self.logger.info(f"{self.name} back: {self.driver.current_url}")
        self.driver.back()

    def quit(self):
        self.logger.info(f"{self.name} quit")
        self.driver.quit()

    def close(self):
        self.logger.info(f"{self.name} close")
        self.driver.close()

    def switch_to_alert(self):
        self.logger.info(f"{self.name} switch to alert")
        self.wait.until(EC.alert_is_present())
        return self.driver.switch_to.alert

    def check_to_close_alerts(self):
        try:
            return self.driver.switch_to.alert
        except NoAlertPresentException:
            pass

    def get_current_url(self):
        self.logger.info(f"{self.name} current url")
        return self.driver.current_url

    def switch_to_window(self, window_number):
        self.logger.info(f"{self.name} switch to window {window_number}")
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def switch_to_frame(self, frame, frame_locator):
        self.logger.info(f"{self.name} switch to frame {frame}")
        self.wait.until(EC.presence_of_element_located(frame_locator))
        self.driver.switch_to.frame(frame)

    def switch_to_previous_frame(self):
        self.logger.info(f"{self.name} switch to previous frame")
        self.driver.switch_to.parent_frame()

    def get_alert_text(self):
        self.logger.info(f"{self.name} get alert text")
        return self.alert.text

    def get_title(self):
        self.logger.info(f"{self.name} get title")
        return self.driver.title

    def scroll_down(self):
        self.logger.info(f"{self.name} scroll down")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
