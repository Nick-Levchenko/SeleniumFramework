from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from elements.button_element import ButtonElement
from elements.image_element import ImageElement
from pages.base_page import BasePage
from utils.browser import Browser


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
        soup = BeautifulSoup(self.driver.driver.page_source, 'lxml')
        while len(set(soup.select('img')[1:])) != 2:
            self.driver.driver.refresh()
            soup = BeautifulSoup(self.driver.driver.page_source, 'lxml')
        return len(set(soup.select('img')[1:]))