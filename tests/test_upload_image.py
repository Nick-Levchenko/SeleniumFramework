from pages.upload_image_page import UploadImagePage
from utils.config_reader import ConfigReader
from utils.page_utils import upload_file_to_system_dialog

config = ConfigReader()


class TestUploadImage:
    TEST_CASE_NAME = "UploadImage"
    FILE_TITLE = "schema.jpg"
    SUCCESS_UPLOAD = "File Uploaded!"
    CHECK_MARK = "✔"
    SCRIPT_PATH = 'utils\send_path.exe'

    def test_upload_file(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        upload_image_page = UploadImagePage(driver_chrome)
        upload_image_page.wait_for_opening()
        upload_image_page.upload_file()
        success_upload_text = upload_image_page.get_success_upload_text()
        upload_file_title = upload_image_page.get_upload_file_title()
        assert success_upload_text == self.SUCCESS_UPLOAD, f'success_upload_text - {success_upload_text}, expected {self.SUCCESS_UPLOAD}'
        assert upload_file_title == self.FILE_TITLE, f'upload_file_title - {upload_file_title}, expected {self.FILE_TITLE}'

    def test_upload_file_dialog_window(self, driver_chrome):
        driver_chrome.get(config.get_url_by_test_case(self.TEST_CASE_NAME))
        upload_image_page = UploadImagePage(driver_chrome)
        upload_image_page.wait_for_opening()
        upload_image_page.click_upload_button()
        upload_file_to_system_dialog(self.SCRIPT_PATH)
        file_name_in_area = upload_image_page.get_file_name_in_area()
        check_mark = upload_image_page.get_check_mark()
        assert file_name_in_area == self.FILE_TITLE, f'file_name_in_area - {file_name_in_area}, expected {self.FILE_TITLE}'
        assert check_mark == self.CHECK_MARK, f'check_mark - {check_mark}, expected {self.CHECK_MARK}'
