from pages.frames_page import FramesPage
from utils.config_reader import ConfigReader

config = ConfigReader()


class TestFrames:
    TEST_CASE_NAME = "Frames"
    NESTED_PARENT_FRAME = "frame1"
    NESTED_CHILD_FRAME = 0
    NESTED_PARENT_FRAME_TEXT = "Parent frame"
    NESTED_CHILD_FRAME_TEXT = "Child Iframe"
    UPPER_FRAME = "frame1"
    LOWER_FRAME = "frame2"

    def test_frames(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))

        frames_page = FramesPage(driver_chrome)
        frames_page.click_alerts_frame_windows()
        frames_page.click_nested_frames()
        driver_chrome.switch_to_frame(self.NESTED_PARENT_FRAME, frames_page.PARENT_FRAME_LOC)
        frames_text = frames_page.nested_frames_text.get_text()
        assert frames_text == self.NESTED_PARENT_FRAME_TEXT, f'parent text - {frames_text}, expected {self.NESTED_PARENT_FRAME_TEXT}'
        driver_chrome.switch_to_frame(self.NESTED_CHILD_FRAME, frames_page.CHILD_FRAME_LOC)
        frames_text = frames_page.nested_frames_text.get_text()
        assert frames_page.nested_frames_text.get_text() == self.NESTED_CHILD_FRAME_TEXT, f'child text - {frames_text}, expected {self.NESTED_CHILD_FRAME_TEXT}'
        driver_chrome.switch_to_previous_frame()
        driver_chrome.switch_to_previous_frame()
        frames_page.click_frames()
        driver_chrome.switch_to_frame(self.UPPER_FRAME, frames_page.UPPER_FRAME_LOC)
        upper_frame_text = frames_page.frames_text.get_text()
        driver_chrome.switch_to_previous_frame()
        driver_chrome.switch_to_frame(self.LOWER_FRAME, frames_page.LOWER_FRAME_LOC)
        lower_frame_text = frames_page.frames_text.get_text()
        assert upper_frame_text == lower_frame_text, f'upper_frame_text - {upper_frame_text} != lower - {lower_frame_text}'
