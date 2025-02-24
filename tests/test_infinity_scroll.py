from pages.infinity_scroll_page import InfinityScrollPage
from utils.config_reader import ConfigReader

config = ConfigReader()


class TestInfinityScroll:
    TEST_CASE_NAME = "InfinityScroll"
    AGE = 34

    def test_infinity_scroll(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        infinity_scroll_page = InfinityScrollPage(driver_chrome)
        infinity_scroll_page.wait_for_opening()
        while infinity_scroll_page.get_count_paragraph() < self.AGE:
            driver_chrome.scroll_down()
        total_paragraphs = infinity_scroll_page.get_count_paragraph()
        assert total_paragraphs == self.AGE, f'total_paragraphs - {total_paragraphs}, expected 34'
