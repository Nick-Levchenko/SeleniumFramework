import faker

from pages.alerts_context_page import AlertsContextPage
from pages.alerts_page import AlertsPage
from pages.basic_auth_page import BasicAuthPage
from pages.dynamic_content_page import DynamicContentPage
from pages.frames_page import FramesPage
from pages.handlers_page import HandlersPage
from pages.hovers_page import HoversPage
from pages.infinity_scroll_page import InfinityScrollPage
from pages.keyboard_actions_page import KeyboardActionsPage
from pages.upload_image_page import UploadImagePage
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

    def test_alerts_js(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        alerts_page = AlertsPage(driver_chrome)
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
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        context_page = AlertsContextPage(driver_chrome)
        context_page.wait_for_opening()
        context_page.context_click()
        assert context_page.get_alert_text() == config.get_param_by_test_case(self.TEST_CASE_NAME, 'alert_text')
        driver_chrome.alert.accept()
        check_to_close_alerts(driver_chrome)


class TestKeyboardActions:
    TEST_CASE_NAME = "KeyboardActions"

    def test_keyboard_actions(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        slider_page = KeyboardActionsPage(driver_chrome)
        slider_page.wait_for_opening()
        slider_page.move_slider()
        assert 0 < slider_page.get_result() < 5


class TestHovers:
    TEST_CASE_NAME = "Hovers"

    def test_hovers(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        hovers_page = HoversPage(driver_chrome)
        for user in config.get_param_by_test_case(self.TEST_CASE_NAME, 'users'):
            hovers_page.wait_for_opening()
            hovers_page.move_to_hover(user)
            assert hovers_page.check_name(user).is_displayed()
            user_number = hovers_page.get_user_number(user)
            hovers_page.view_profile(user)
            assert hovers_page.get_current_url().endswith(user_number)
            driver_chrome.driver.back()
            assert hovers_page.unique_element.get_text() == config.get_param_by_test_case(self.TEST_CASE_NAME,
                                                                                          'unique_element_text')


class TestHandlers:
    TEST_CASE_NAME = "Handlers"

    def test_handlers(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        handlers_page = HandlersPage(driver_chrome)
        handlers_page.wait_for_opening()
        handlers_page.click_new_window()
        handlers_page.switch_to_window(1)
        assert driver_chrome.driver.title == config.get_param_by_test_case(self.TEST_CASE_NAME, 'new_window_title')
        assert handlers_page.window_text.get_text() == config.get_param_by_test_case(self.TEST_CASE_NAME,
                                                                                     'new_window_text')
        handlers_page.switch_to_window(0)
        handlers_page.wait_for_opening()
        handlers_page.click_new_window()
        handlers_page.switch_to_window(2)
        assert driver_chrome.driver.title == config.get_param_by_test_case(self.TEST_CASE_NAME, 'new_window_title')
        assert handlers_page.window_text.get_text() == config.get_param_by_test_case(self.TEST_CASE_NAME,
                                                                                     'new_window_text')
        handlers_page.switch_to_window(0)
        handlers_page.wait_for_opening()
        handlers_page.switch_to_window(1)
        driver_chrome.close()
        handlers_page.switch_to_window(1)
        driver_chrome.close()


class TestFrames:
    TEST_CASE_NAME = "Frames"

    def test_frames(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))

        frames_page = FramesPage(driver_chrome)
        frames_page.click_alerts_frame_windows()
        frames_page.click_nested_frames()
        frames_page.switch_to_frame(config.get_param_by_test_case(self.TEST_CASE_NAME, 'nested_parent_frame'))
        assert frames_page.nested_frames_text.get_text() == config.get_param_by_test_case(self.TEST_CASE_NAME,
                                                                                          'nested_parent_frame_text')
        frames_page.switch_to_frame(config.get_param_by_test_case(self.TEST_CASE_NAME, 'nested_child_frame'))
        assert frames_page.nested_frames_text.get_text() == config.get_param_by_test_case(self.TEST_CASE_NAME,
                                                                                          'nested_child_frame_text')
        frames_page.switch_to_parent()
        frames_page.switch_to_parent()
        frames_page.click_frames()
        frames_page.switch_to_frame(config.get_param_by_test_case(self.TEST_CASE_NAME, 'upper_frame'))
        upper_frame_text = frames_page.frames_text.get_text()
        frames_page.switch_to_parent()
        frames_page.switch_to_frame(config.get_param_by_test_case(self.TEST_CASE_NAME, 'lower_frame'))
        lower_frame_text = frames_page.frames_text.get_text()
        assert upper_frame_text == lower_frame_text


class TestDynamicContent:
    TEST_CASE_NAME = "DynamicContent"

    def test_dynamic_content(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        dynamic_content_page = DynamicContentPage(driver_chrome)
        dynamic_content_page.get_two_identical_avatars()
        assert dynamic_content_page.compare_avatars() == 2


class TestInfinityScroll:
    TEST_CASE_NAME = "InfinityScroll"

    def test_infinity_scroll(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        infinity_scroll_page = InfinityScrollPage(driver_chrome)
        infinity_scroll_page.wait_for_opening()
        infinity_scroll_page.scroll_by_age(34)
        assert infinity_scroll_page.get_count_paragraph() == 34


class TestUploadImage:
    TEST_CASE_NAME = "UploadImage"

    def test_upload_file(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        upload_image_page = UploadImagePage(driver_chrome)
        upload_image_page.wait_for_opening()
        upload_image_page.upload_file()
        assert upload_image_page.success_upload_text.get_text() == config.get_param_by_test_case(self.TEST_CASE_NAME,
                                                                                                 'success_upload')
        assert upload_image_page.upload_file_title.get_text() == config.get_param_by_test_case(self.TEST_CASE_NAME,
                                                                                               'file_title')

    def test_upload_file_dialog_window(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        upload_image_page = UploadImagePage(driver_chrome)
        upload_image_page.wait_for_opening()
        upload_image_page.upload_file_dialog_window()

        assert upload_image_page.file_name_in_area.get_text() == config.get_param_by_test_case(self.TEST_CASE_NAME,
                                                                                               'file_title')
        mark = upload_image_page.check_mark.get_text()
        assert mark == "✔"
