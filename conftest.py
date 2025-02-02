import pytest
from selenium.webdriver.chrome.options import Options

from utils.browser import Browser
from utils.browser_factory import BrowserFactory


@pytest.fixture
def driver_chrome():
    options = Options()
    browser = BrowserFactory.get_browser()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def basic_auth_driver():
    browser = BrowserFactory.get_browser()
    browser.maximize_window()
    yield browser
    browser.quit()
