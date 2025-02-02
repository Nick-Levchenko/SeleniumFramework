from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from conftest import Browser
from elements.text_element import TextElement
from pages.base_page import BasePage


class AlertsContextPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, "hot-spot")
    SELECTED_AREA = (By.ID, "hot-spot")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'AlertsContextClickPage'
        self.unique_element = TextElement(self.driver, self.UNIQUE_ELEMENT_LOC)
        self.actions = ActionChains(self.driver.driver)

    def context_click(self):
        target = self.wait.until(EC.element_to_be_clickable(self.SELECTED_AREA))
        self.actions.context_click(target).perform()
