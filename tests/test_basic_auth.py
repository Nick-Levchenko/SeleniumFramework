from pages.basic_auth_page import BasicAuthPage
from utils.url_utils import give_format_url


class TestBasicAuthPage:
    TEST_CASE_NAME = "BasicAuthorization"
    URL = "http://the-internet.herokuapp.com/basic_auth"
    CHECK_PHRASE = "Congratulations! You must have the proper credentials."
    LOGIN = "admin"
    PASSWORD = "admin"

    def test_basic_auth(self, driver_chrome):
        auth_page = BasicAuthPage(driver_chrome)
        auth_url = give_format_url(self.URL, self.LOGIN, self.PASSWORD)
        driver_chrome.get(auth_url)
        auth_page.unique_element.wait_for_presence()
        result_text = auth_page.success_element.get_text()
        assert result_text == self.CHECK_PHRASE, f'actual - {result_text}, expected - {self.CHECK_PHRASE}'
