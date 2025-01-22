from selenium.common import NoAlertPresentException


def check_to_close_alerts(driver):
    try:
        assert driver.switch_to_alert()
        raise AssertionError("Alert was not close")
    except NoAlertPresentException:
        pass
