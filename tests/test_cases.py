import time

import faker

from pages.alerts_context_page import AlertsContextPage
from pages.alerts_page import AlertsPage
from pages.basic_auth_page import BasicAuthPage
from pages.keyboard_actions_page import KeyboardActionsPage
from utils.alert_utils import check_to_close_alerts
from utils.config_reader import ConfigReader

fake = faker.Faker()
config = ConfigReader()


class TestBasicAuthPage:
    TEST_CASE_NAME = "BasicAuthorization"

    def test_basic_auth(self, basic_auth_driver):
        login = config.get_param_by_test_case(self.TEST_CASE_NAME, 'login')
        password = config.get_param_by_test_case(self.TEST_CASE_NAME, 'password')
        auth_page = BasicAuthPage(basic_auth_driver)
        auth_url = auth_page.give_format_url(config.get_url_by_test_case(self.TEST_CASE_NAME), login, password)
        basic_auth_driver.get(auth_url)
        auth_page.unique_element.wait_for_presence()
        assert auth_page.success_element.get_text() == config.get_param_by_test_case(self.TEST_CASE_NAME,
                                                                                     'check_phrase')
        time.sleep(3)


class TestAlerts:
    TEST_CASE_NAME = "Alerts"

    def test_alert(self, driver_chrome):
        alerts_page = AlertsPage(driver_chrome)
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        alerts_page.wait_for_opening()
        alerts_page.click_alert_button()
        assert alerts_page.get_alert_text() == config.get_param_by_test_case(self.TEST_CASE_NAME, 'alert_text')
        driver_chrome.alert.accept()
        check_to_close_alerts(driver_chrome)
        assert alerts_page.result_section.get_text() == config.get_param_by_test_case(self.TEST_CASE_NAME,
                                                                                      'alert_result_text')
        alerts_page.click_confirm_button()
        assert alerts_page.get_alert_text() == config.get_param_by_test_case(self.TEST_CASE_NAME, 'confirm_text')
        driver_chrome.alert.accept()
        check_to_close_alerts(driver_chrome)
        assert alerts_page.result_section.get_text() == config.get_param_by_test_case(self.TEST_CASE_NAME,
                                                                                      'confirm_result_text')
        alerts_page.click_prompt_button()
        assert alerts_page.get_alert_text() == config.get_param_by_test_case(self.TEST_CASE_NAME, 'prompt_text')
        fake_text = fake.text(15)
        driver_chrome.alert.send_keys(fake_text)
        driver_chrome.alert.accept()
        check_to_close_alerts(driver_chrome)
        assert alerts_page.result_section.get_text() == f"{config.get_param_by_test_case(self.TEST_CASE_NAME, 'prompt_result_text')}{fake_text}"


class TestAlertsJS:
    TEST_CASE_NAME = "AlertsJS"

    def test_alerts_js(self, driver_chrome):
        alerts_page = AlertsPage(driver_chrome)
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        alerts_page.wait_for_opening()
        driver_chrome.driver.execute_script(config.get_param_by_test_case(self.TEST_CASE_NAME, 'alert_button_script'))
        assert alerts_page.get_alert_text() == config.get_param_by_test_case(self.TEST_CASE_NAME, 'alert_text')
        driver_chrome.alert.accept()
        check_to_close_alerts(driver_chrome)
        assert alerts_page.result_section.get_text() == config.get_param_by_test_case(self.TEST_CASE_NAME,
                                                                                      'alert_result_text')
        driver_chrome.driver.execute_script(config.get_param_by_test_case(self.TEST_CASE_NAME, 'confirm_button_script'))
        assert alerts_page.get_alert_text() == config.get_param_by_test_case(self.TEST_CASE_NAME, 'confirm_text')
        driver_chrome.alert.accept()
        check_to_close_alerts(driver_chrome)
        assert alerts_page.result_section.get_text() == config.get_param_by_test_case(self.TEST_CASE_NAME,
                                                                                      'confirm_result_text')
        driver_chrome.driver.execute_script(config.get_param_by_test_case(self.TEST_CASE_NAME, 'prompt_button_script'))
        assert alerts_page.get_alert_text() == config.get_param_by_test_case(self.TEST_CASE_NAME, 'prompt_text')
        fake_text = fake.text(10)
        driver_chrome.alert.send_keys(fake_text)
        driver_chrome.alert.accept()
        check_to_close_alerts(driver_chrome)
        assert alerts_page.result_section.get_text() == f"{config.get_param_by_test_case(self.TEST_CASE_NAME, 'prompt_result_text')}{fake_text}"


class TestAlertsContextClick:
    TEST_CASE_NAME = "AlertsContextClick"

    def test_alerts_context_click(self, driver_chrome):
        context_page = AlertsContextPage(driver_chrome)
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        context_page.wait_for_opening()
        context_page.context_click()
        assert context_page.get_alert_text() == config.get_param_by_test_case(self.TEST_CASE_NAME, 'alert_text')
        driver_chrome.alert.accept()
        check_to_close_alerts(driver_chrome)


class TestKeyboardActions:
    TEST_CASE_NAME = "KeyboardActions"

    def test_keyboard_actions(self, driver_chrome):
        slider_page = KeyboardActionsPage(driver_chrome)
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        slider_page.wait_for_opening()
        slider_page.move_slider()
        assert 0 < slider_page.get_result() < 5