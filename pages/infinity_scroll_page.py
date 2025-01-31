from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from elements.text_element import TextElement
from pages.base_page import BasePage
from utils.browser import Browser


class InfinityScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    PARAGRAPH_LOC = (By.XPATH, "//*[@class='jscroll-added']")
    FOOTER = (By.ID, "page-footer")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'InfinityScrollPage'
        self.unique_element = TextElement(self.driver, self.UNIQUE_ELEMENT_LOC)
        self.paragraph = TextElement(self.driver, self.PARAGRAPH_LOC)
        self.action = ActionChains(self.driver.driver)

    def get_count_paragraph(self):
        return self.paragraph.get_count_elements()

    def scroll_by_age(self, age: int):
        footer = self.wait.until(EC.presence_of_element_located(self.FOOTER))
        while self.get_count_paragraph() < age:
            self.action.move_to_element(footer).scroll_by_amount(1, 500).perform()
