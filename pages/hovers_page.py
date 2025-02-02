from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from elements.text_element import TextElement
from pages.base_page import BasePage
from utils.browser import Browser
from utils.config_reader import ConfigReader


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    USER_1_IMG = (By.XPATH, "(//*[@alt='User Avatar'])[1]")
    USER_2_IMG = (By.XPATH, "(//*[@alt='User Avatar'])[2]")
    USER_3_IMG = (By.XPATH, "(//*[@alt='User Avatar'])[3]")
    USER_1_NAME = (By.XPATH, "(//*[@id='content']//h5)[1]")
    USER_2_NAME = (By.XPATH, "(//*[@id='content']//h5)[2]")
    USER_3_NAME = (By.XPATH, "(//*[@id='content']//h5)[3]")
    USER_1_LINK = (By.XPATH, "(//*[@id='content']//a)[1]")
    USER_2_LINK = (By.XPATH, "(//*[@id='content']//a)[2]")
    USER_3_LINK = (By.XPATH, "(//*[@id='content']//a)[3]")

    USERS = {'user_1': {'username': USER_1_NAME, 'user_avatar': USER_1_IMG, 'user_link': USER_1_LINK},
             'user_2': {'username': USER_2_NAME, 'user_avatar': USER_2_IMG, 'user_link': USER_2_LINK},
             'user_3': {'username': USER_3_NAME, 'user_avatar': USER_3_IMG, 'user_link': USER_3_LINK}, }

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'HoversPage'
        self.unique_element = TextElement(self.driver, self.UNIQUE_ELEMENT_LOC)
        self.action = ActionChains(self.driver.driver)
        self.config = ConfigReader()

    def get_user_param(self, user_name, user_element):
        user = self.USERS[user_name]
        return self.wait.until(EC.visibility_of_element_located(user[user_element]))

    def move_to_hover(self, username):
        self.action.move_to_element(self.get_user_param(username, 'user_avatar')).perform()

    def check_name(self, username):
        return self.get_user_param(username, 'username')

    def view_profile(self, username):
        self.action.click(self.get_user_param(username, 'user_link')).perform()

    def get_current_url(self):
        return self.driver.current_url()

    def get_user_number(self, username):
        return self.get_user_param(username, 'username').text[-1:]
