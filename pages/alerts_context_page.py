from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from elements.text_element import TextElement
from pages.base_page import BasePage
from tests.conftest import Browser
from utils.logger import Logger


class AlertsContextPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    SELECTED_AREA = (By.ID, "hot-spot")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'AlertsContextClickPage'
        self.unique_element = TextElement(self.driver, self.UNIQUE_ELEMENT_LOC)
        self.actions = ActionChains(self.driver.driver)
        self.logger = Logger().getLogger()

    def context_click(self):
        self.logger.info(f'context click on {self.page_name}')
        target = self.wait.until(EC.element_to_be_clickable(self.SELECTED_AREA))
        self.actions.context_click(target).perform()
