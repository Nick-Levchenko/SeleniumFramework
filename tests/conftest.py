import pytest

from utils.browser import Browser


@pytest.fixture
def driver_chrome():
    browser = Browser()
    browser.driver.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def basic_auth_driver():
    browser = Browser()
    browser.driver.maximize_window()
    yield browser
    browser.quit()
