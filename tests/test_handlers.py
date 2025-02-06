from pages.handlers_page import HandlersPage
from utils.config_reader import ConfigReader

config = ConfigReader()


class TestHandlers:
    TEST_CASE_NAME = "Handlers"
    NEW_WINDOW_TEXT = "New Window"
    NEW_WINDOW_TITLE = "New Window"

    def test_handlers(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        handlers_page = HandlersPage(driver_chrome)
        handlers_page.wait_for_opening()
        handlers_page.click_new_window()
        driver_chrome.switch_to_window(1)
        title = driver_chrome.get_title()
        assert title == self.NEW_WINDOW_TITLE, f'title - {title}, expected - {self.NEW_WINDOW_TITLE}'
        window_text = handlers_page.window_text.get_text()
        assert window_text == self.NEW_WINDOW_TEXT, f'window text - {window_text}, expected - {self.NEW_WINDOW_TEXT}'
        driver_chrome.switch_to_window(0)
        handlers_page.wait_for_opening()
        handlers_page.click_new_window()
        driver_chrome.switch_to_window(2)
        title = driver_chrome.get_title()
        assert title == self.NEW_WINDOW_TITLE, f'title - {title}, expected - {self.NEW_WINDOW_TITLE}'
        window_text = handlers_page.window_text.get_text()
        assert window_text == self.NEW_WINDOW_TEXT, f'window text - {window_text}, expected - {self.NEW_WINDOW_TEXT}'
        driver_chrome.switch_to_window(0)
        handlers_page.wait_for_opening()
        driver_chrome.switch_to_window(1)
        driver_chrome.close()
        driver_chrome.switch_to_window(1)
        driver_chrome.close()
