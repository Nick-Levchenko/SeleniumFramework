from selenium.webdriver.common.by import By

from elements.button_element import ButtonElement
from elements.text_element import LabelElement
from pages.base_page import BasePage
from utils.browser import Browser


class FramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'sampleHeading')
    ALERTS_FRAME_WINDOWS = (By.XPATH, "//*[contains(@class, 'element-group')][3]")

    NESTED_FRAMES = (By.XPATH, "(//*[@id='item-3'])[2]")
    NESTED_FRAMES_TEXT = (By.XPATH, '//body')
    PARENT_FRAME_LOC = (By.ID, 'frame1')
    CHILD_FRAME_LOC = (By.XPATH, "//*[contains(@srcdoc, 'Child Iframe')]")

    FRAMES = (By.XPATH, "(//*[@id='item-2'])[2]")
    FRAMES_TEXT = (By.ID, 'sampleHeading')
    UPPER_FRAME_LOC = (By.ID, 'frame1')
    LOWER_FRAME_LOC = (By.ID, 'frame2Wrapper')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'Frames'
        self.alerts_frame_windows = ButtonElement(self.driver, self.ALERTS_FRAME_WINDOWS, self.page_name)
        self.unique_element = ButtonElement(self.driver, self.UNIQUE_ELEMENT_LOC, self.page_name)
        self.nested_frames = ButtonElement(self.driver, self.NESTED_FRAMES, self.page_name)
        self.frames = ButtonElement(self.driver, self.FRAMES, self.page_name)
        self.nested_frames_text = LabelElement(self.driver, self.NESTED_FRAMES_TEXT, self.page_name)
        self.frames_text = LabelElement(self.driver, self.FRAMES_TEXT, self.page_name)

    def click_alerts_frame_windows(self):
        self.alerts_frame_windows.click()

    def click_nested_frames(self):
        self.nested_frames.click()

    def click_frames(self):
        self.frames.click()
