from selenium.webdriver.common.by import By

from elements.button_element import ButtonElement
from elements.image_element import ImageElement
from pages.base_page import BasePage
from utils.browser import Browser
from utils.page_utils import img_parser


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//img")
    IMAGES = (By.XPATH, "//*[@id='content']//img")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = 'DynamicContent'
        self.driver: Browser = driver
        self.unique_element = ButtonElement(self.driver, self.UNIQUE_ELEMENT_LOC, self.page_name)
        self.images = ImageElement(self.driver, self.IMAGES, self.page_name)

    def get_images_links(self):
        return img_parser(self.driver)
