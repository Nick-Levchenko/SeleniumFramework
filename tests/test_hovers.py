from pages.hovers_page import HoversPage
from utils.config_reader import ConfigReader

config = ConfigReader()


class TestHovers:
    TEST_CASE_NAME = "Hovers"
    UNIQUE_ELEMENT_TEXT = "Hovers"
    USERS = [
        "1",
        "2",
        "3"
    ]

    def test_hovers(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))

        for user in self.USERS:
            hovers_page = HoversPage(driver_chrome)
            hovers_page.wait_for_opening()
            hovers_page.move_to_hover(user)
            assert hovers_page.check_name(user).is_displayed(), f'username is not displayed - {user}'
            user_number = hovers_page.get_user_number(user)
            current_loc = hovers_page.get_current_url(int(user))
            driver_chrome.action.click(current_loc).perform()
            assert driver_chrome.get_current_url().endswith(
                user_number), f"current url doesn't match the user's number - {user_number}"
            driver_chrome.driver.back()
            assert hovers_page.unique_element.get_text() == self.UNIQUE_ELEMENT_TEXT, 'incorrect page'
