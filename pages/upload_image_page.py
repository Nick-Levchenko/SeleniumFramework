from selenium.webdriver.common.by import By

from elements.button_element import ButtonElement
from elements.input_element import InputElement
from elements.text_element import LabelElement
from pages.base_page import BasePage
from utils.browser import Browser


class UploadImagePage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'file-submit')
    CHOOSE_FILE_LOC = (By.ID, 'file-upload')
    UPLOAD_BUTTON_LOC = (By.ID, 'file-submit')
    UPDATED_PAGE_UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[text()='File Uploaded!']")
    SUCCESS_UPLOAD_TEXT_LOC = (By.XPATH, "//*[@id='content']//h3")
    UPLOAD_FILE_TITLE_LOC = (By.ID, "uploaded-files")
    UPLOAD_AREA_LOC = (By.ID, "drag-drop-upload")
    FILENAME_IN_AREA_LOC = (By.XPATH, "(//*[@class='dz-filename'])[1]")
    CHECK_MARK_LOC = (By.XPATH, "(//*[text()='✔'])[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'UploadImage'
        self.unique_element = ButtonElement(self.driver, self.UNIQUE_ELEMENT_LOC, self.page_name)
        self.choose_file = InputElement(self.driver, self.CHOOSE_FILE_LOC, self.page_name)
        self.upload_button = ButtonElement(self.driver, self.UPLOAD_BUTTON_LOC, self.page_name)
        self.success_upload_text = LabelElement(self.driver, self.SUCCESS_UPLOAD_TEXT_LOC, self.page_name)
        self.upload_file_title = LabelElement(self.driver, self.UPLOAD_FILE_TITLE_LOC, self.page_name)
        self.upload_area = ButtonElement(self.driver, self.UPLOAD_AREA_LOC, self.page_name)
        self.file_name_in_area = LabelElement(self.driver, self.FILENAME_IN_AREA_LOC, self.page_name)
        self.check_mark = LabelElement(self.driver, self.CHECK_MARK_LOC, self.page_name)

    def upload_file(self):
        file = self.CONFIG.get_param_by_test_case(self.page_name, 'file')
        self.choose_file.send_keys(file)
        self.upload_button.click()
