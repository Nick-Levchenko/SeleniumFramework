from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from elements.text_element import LabelElement
from pages.base_page import BasePage
from utils.browser import Browser
from utils.config_reader import ConfigReader


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'HoversPage'
        self.unique_element = LabelElement(self.driver, self.UNIQUE_ELEMENT_LOC, self.page_name)
        self.config = ConfigReader()
        self.wait = WebDriverWait(self.driver.driver, 10)

    def _get_locator_by_index(self, index, locator):
        user = {'username': (By.XPATH, f"(//*[@id='content']//h5)[{index}]"),
                'user_avatar': (By.XPATH, f"(//*[@alt='User Avatar'])[{index}]"),
                'user_link': (By.XPATH, f"(//*[@id='content']//a)[{index}]")}
        return self.wait.until(EC.visibility_of_element_located(user[locator]))

    def move_to_hover(self, username):
        self.driver.action.move_to_element(self._get_locator_by_index(username, 'user_avatar')).perform()

    def check_name(self, username):
        return self._get_locator_by_index(username, 'username')

    def get_user_number(self, username):
        return self._get_locator_by_index(username, 'username').text[-1:]

    def get_current_url(self, username):
        return self._get_locator_by_index(int(username), 'user_link')
