from selenium.webdriver.common.by import By

from elements.button_element import ButtonElement
from elements.text_element import TextElement
from pages.base_page import BasePage
from utils.browser import Browser


class FramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'sampleHeading')
    ALERTS_FRAME_WINDOWS = (By.XPATH, "//*[contains(@class, 'element-group')][3]")

    NESTED_FRAMES = (By.XPATH, "(//*[@id='item-3'])[2]")
    NESTED_FRAMES_TEXT = (By.XPATH, '//body')

    FRAMES = (By.XPATH, "(//*[@id='item-2'])[2]")
    FRAMES_TEXT = (By.ID, 'sampleHeading')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'Frames'
        self.alerts_frame_windows = ButtonElement(self.driver, self.ALERTS_FRAME_WINDOWS)
        self.unique_element = ButtonElement(self.driver, self.UNIQUE_ELEMENT_LOC)
        self.nested_frames = ButtonElement(self.driver, self.NESTED_FRAMES)
        self.frames = ButtonElement(self.driver, self.FRAMES)
        self.nested_frames_text = TextElement(self.driver, self.NESTED_FRAMES_TEXT)
        self.frames_text = TextElement(self.driver, self.FRAMES_TEXT)

    def click_alerts_frame_windows(self):
        self.alerts_frame_windows.click()

    def click_nested_frames(self):
        self.nested_frames.click()

    def click_frames(self):
        self.frames.click()

    def switch_to_frame(self, frame):
        self.driver.switch_to_frame(frame)

    def switch_to_parent(self):
        self.driver.switch_to_previous_frame()
