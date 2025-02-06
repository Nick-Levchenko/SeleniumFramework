from pages.keyboard_actions_page import KeyboardActionsPage
from utils.config_reader import ConfigReader

config = ConfigReader()


class TestKeyboardActions:
    TEST_CASE_NAME = "KeyboardActions"

    def test_keyboard_actions(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        slider_page = KeyboardActionsPage(driver_chrome)
        slider_page.wait_for_opening()
        result_value = slider_page.move_slider()
        assert 0.5 <= result_value <= 4.5, f'result_value should be between 0.5 and 4.5, actual value is {result_value}'
