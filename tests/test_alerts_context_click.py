from pages.alerts_context_page import AlertsContextPage
from utils.config_reader import ConfigReader

config = ConfigReader()


class TestAlertsContextClick:
    TEST_CASE_NAME = "AlertsContextClick"
    ALERT_TEXT = "You selected a context menu"

    def test_alerts_context_click(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        context_page = AlertsContextPage(driver_chrome)
        context_page.wait_for_opening()
        context_page.click_on_area()
        alert_text = driver_chrome.get_alert_text()
        assert alert_text == self.ALERT_TEXT, f'actual - {alert_text}, expected - {self.ALERT_TEXT}'
        driver_chrome.alert.accept()
        driver_chrome.check_to_close_alerts()
