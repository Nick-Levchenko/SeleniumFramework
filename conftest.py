import pytest
from selenium.webdriver.chrome.options import Options

from utils.browser import Browser
from utils.config_reader import ConfigReader

config = ConfigReader()


@pytest.fixture
def driver_chrome():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('no-sandbox')
    browser = Browser(options=options)
    yield browser
    browser.quit()
