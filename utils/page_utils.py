import os
import time

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.browser import Browser
from utils.config_reader import ConfigReader

config = ConfigReader()


def get_locator_by_index(driver: Browser, index, locator):
    wait = WebDriverWait(driver.driver, config.read_driver_config('timeout'))
    user = {'username': (By.XPATH, f"(//*[@id='content']//h5)[{index}]"),
            'user_avatar': (By.XPATH, f"(//*[@alt='User Avatar'])[{index}]"),
            'user_link': (By.XPATH, f"(//*[@id='content']//a)[{index}]")}
    return wait.until(EC.visibility_of_element_located(user[locator]))


def give_format_url(url: str, login, password):
    auth_string = f'{login}:{password}@'
    strings = url.split('//')
    formatted_url = f'{strings[0]}//{auth_string}{strings[1]}'
    return formatted_url


def use_system_script(script_path):
    time.sleep(1)
    os.popen(script_path)
    time.sleep(1)


def img_parser(driver: Browser):
    soup = BeautifulSoup(driver.driver.page_source, 'lxml')
    while len(set(soup.select('img')[1:])) != 2:
        driver.driver.refresh()
        soup = BeautifulSoup(driver.driver.page_source, 'lxml')
    return len(set(soup.select('img')[1:]))


def get_count_elements(driver: Browser, tag, attribute_name, attribute_value):
    soup = BeautifulSoup(driver.driver.page_source, 'lxml')
    count = len(soup.find_all(tag, attrs={attribute_name: attribute_value}))
    return count
