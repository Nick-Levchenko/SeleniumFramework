from pages.dynamic_content_page import DynamicContentPage
from utils.config_reader import ConfigReader

config = ConfigReader()


class TestDynamicContent:
    TEST_CASE_NAME = "DynamicContent"

    def test_dynamic_content(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        dynamic_content_page = DynamicContentPage(driver_chrome)
        total_links = dynamic_content_page.get_images_links()
        assert total_links == 2, f'result_links - {total_links}, expected 2'
