from selenium.webdriver.common.by import By

from conftest import Browser
from elements.button_element import ButtonElement
from elements.text_element import LabelElement
from pages.base_page import BasePage


class AlertsPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@onclick='jsAlert()']")
    ALERT_BUTTON = (By.XPATH, "//*[@onclick='jsAlert()']")
    CONFIRM_BUTTON = (By.XPATH, "//*[@onclick='jsConfirm()']")
    PROMPT_BUTTON = (By.XPATH, "//*[@onclick='jsPrompt()']")
    RESULT_SECTION = (By.ID, "result")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'AlertsPage'
        self.unique_element = LabelElement(self.driver, self.UNIQUE_ELEMENT_LOC, self.page_name)
        self.alert_button = ButtonElement(self.driver, self.ALERT_BUTTON, self.page_name)
        self.confirm_button = ButtonElement(self.driver, self.CONFIRM_BUTTON, self.page_name)
        self.prompt_button = ButtonElement(self.driver, self.PROMPT_BUTTON, self.page_name)
        self.result_section = LabelElement(self.driver, self.RESULT_SECTION, self.page_name)

    def click_alert_button(self):
        self.alert_button.click()

    def click_confirm_button(self):
        self.confirm_button.click()

    def click_prompt_button(self):
        self.prompt_button.click()
