from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from elements.button_element import ButtonElement
from elements.image_element import ImageElement
from pages.base_page import BasePage
from utils.browser import Browser


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'content')
    IMAGES = (By.XPATH, "//*[@id='content']//img")

    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = 'DynamicContent'
        self.driver: Browser = driver
        self.unique_element = ButtonElement(self.driver, self.UNIQUE_ELEMENT_LOC)
        self.images = ImageElement(self.driver, self.IMAGES)

    def get_images_links(self):
        images = self.wait.until(EC.presence_of_all_elements_located(self.IMAGES))
        links_list = []
        for image in images:
            links_list.append(image.get_attribute('src'))
        return links_list
