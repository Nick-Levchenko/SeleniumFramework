import faker

from pages.alerts_page import AlertsPage
from utils.config_reader import ConfigReader

fake = faker.Faker()
config = ConfigReader()


class TestAlerts:
    TEST_CASE_NAME = "Alerts"
    ALERT_TEXT = "I am a JS Alert"
    ALERT_RESULT_TEXT = "You successfully clicked an alert"
    CONFIRM_TEXT = "I am a JS Confirm"
    CONFIRM_RESULT_TEXT = "You clicked: Ok"
    PROMPT_TEXT = "I am a JS prompt"
    PROMPT_RESULT_TEXT = "You entered: "
    ALERT_BUTTON_SCRIPT = "document.getElementsByTagName('button')[0].click()"
    CONFIRM_BUTTON_SCRIPT = "document.getElementsByTagName('button')[1].click()"
    PROMPT_BUTTON_SCRIPT = "document.getElementsByTagName('button')[2].click()"

    def test_alert(self, driver_chrome):
        alerts_page = AlertsPage(driver_chrome)
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        alerts_page.wait_for_opening()
        alerts_page.click_alert_button()
        alert_text = driver_chrome.get_alert_text()
        assert alert_text == self.ALERT_TEXT, f'actual - {alert_text}, expected - {self.ALERT_TEXT}'
        driver_chrome.alert.accept()
        driver_chrome.check_to_close_alerts()
        result_section_text = alerts_page.result_section.get_text()
        assert result_section_text == self.ALERT_RESULT_TEXT, f'result_section_text actual - {result_section_text}, expected - {self.ALERT_RESULT_TEXT}'
        alerts_page.click_confirm_button()
        confirm_text = driver_chrome.get_alert_text()
        assert confirm_text == self.CONFIRM_TEXT, f'actual - {confirm_text}, expected - {self.CONFIRM_TEXT}'
        driver_chrome.alert.accept()
        driver_chrome.check_to_close_alerts()
        result_section_text = alerts_page.result_section.get_text()
        assert result_section_text == self.CONFIRM_RESULT_TEXT, f'result_section_text actual - {result_section_text}, expected - {self.CONFIRM_RESULT_TEXT}'
        alerts_page.click_prompt_button()
        prompt_text = driver_chrome.get_alert_text()
        assert prompt_text == self.PROMPT_TEXT, f'actual - {prompt_text}, expected - {self.PROMPT_TEXT}'
        fake_text = fake.text(15)
        driver_chrome.alert.send_keys(fake_text)
        driver_chrome.alert.accept()
        driver_chrome.check_to_close_alerts()
        result_section_text = alerts_page.result_section.get_text()
        assert result_section_text == f"{self.PROMPT_RESULT_TEXT}{fake_text}", f'result_section_text - {result_section_text}, expected - {self.PROMPT_RESULT_TEXT}{fake_text}'

    def test_alerts_js(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        alerts_page = AlertsPage(driver_chrome)
        alerts_page.wait_for_opening()
        driver_chrome.driver.execute_script(self.ALERT_BUTTON_SCRIPT)
        alert_text = driver_chrome.get_alert_text()
        assert alert_text == self.ALERT_TEXT, f'actual - {alert_text}, expected - {self.ALERT_TEXT}'
        driver_chrome.alert.accept()
        driver_chrome.check_to_close_alerts()
        result_section_text = alerts_page.result_section.get_text()
        assert result_section_text == self.ALERT_RESULT_TEXT, f'result_section_text actual - {result_section_text}, expected - {self.ALERT_RESULT_TEXT}'
        driver_chrome.driver.execute_script(self.CONFIRM_BUTTON_SCRIPT)
        confirm_text = driver_chrome.get_alert_text()
        assert confirm_text == self.CONFIRM_TEXT, f'actual - {confirm_text}, expected - {self.CONFIRM_TEXT}'
        driver_chrome.alert.accept()
        driver_chrome.check_to_close_alerts()
        result_section_text = alerts_page.result_section.get_text()
        assert result_section_text == self.CONFIRM_RESULT_TEXT, f'result_section_text actual - {result_section_text}, expected - {self.CONFIRM_RESULT_TEXT}'
        driver_chrome.driver.execute_script(self.PROMPT_BUTTON_SCRIPT)
        prompt_text = driver_chrome.get_alert_text()
        assert prompt_text == self.PROMPT_TEXT, f'actual - {prompt_text}, expected - {self.PROMPT_TEXT}'
        fake_text = fake.text(10)
        driver_chrome.alert.send_keys(fake_text)
        driver_chrome.alert.accept()
        result_section_text = alerts_page.result_section.get_text()
        assert result_section_text == f"{self.PROMPT_RESULT_TEXT}{fake_text}", f'result_section_text - {result_section_text}, expected - {self.PROMPT_RESULT_TEXT}{fake_text}'
