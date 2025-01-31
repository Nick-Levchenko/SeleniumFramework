from selenium.webdriver.common.by import By

from elements.button_element import ButtonElement
from elements.text_element import TextElement
from pages.base_page import BasePage
from conftest import Browser
from utils.logger import Logger


class AlertsPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    ALERT_BUTTON = (By.XPATH, "//*[@onclick='jsAlert()']")
    CONFIRM_BUTTON = (By.XPATH, "//*[@onclick='jsConfirm()']")
    PROMPT_BUTTON = (By.XPATH, "//*[@onclick='jsPrompt()']")
    RESULT_SECTION = (By.ID, "result")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'AlertsPage'
        self.unique_element = TextElement(self.driver, self.UNIQUE_ELEMENT_LOC)
        self.alert_button = ButtonElement(self.driver, self.ALERT_BUTTON)
        self.confirm_button = ButtonElement(self.driver, self.CONFIRM_BUTTON)
        self.prompt_button = ButtonElement(self.driver, self.PROMPT_BUTTON)
        self.result_section = TextElement(self.driver, self.RESULT_SECTION)

    def click_alert_button(self):
        self.alert_button.click()

    def click_confirm_button(self):
        self.confirm_button.click()

    def click_prompt_button(self):
        self.prompt_button.click()
