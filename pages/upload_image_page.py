import os
import time

from selenium.webdriver.common.by import By

from elements.button_element import ButtonElement
from elements.input_element import InputElement
from elements.text_element import TextElement
from pages.base_page import BasePage
from utils.browser import Browser


class UploadImagePage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, 'file-submit')
    CHOOSE_FILE_LOC = (By.ID, 'file-upload')
    UPLOAD_BUTTON_LOC = (By.ID, 'file-submit')
    UPDATED_PAGE_UNIQUE_ELEMENT_LOC = (By.ID, 'uploaded-files')
    SUCCESS_UPLOAD_TEXT_LOC = (By.XPATH, "//*[@id='content']//h3")
    UPLOAD_FILE_TITLE_LOC = (By.ID, "uploaded-files")
    UPLOAD_AREA_LOC = (By.ID, "drag-drop-upload")
    FILENAME_IN_AREA_LOC = (By.XPATH, "(//*[@class='dz-filename'])[1]")
    CHECK_MARK_LOC = (By.XPATH, "(//*[text()='✔'])[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: Browser = driver
        self.page_name = 'UploadImage'
        self.unique_element = ButtonElement(self.driver, self.UNIQUE_ELEMENT_LOC)
        self.choose_file = InputElement(self.driver, self.CHOOSE_FILE_LOC)
        self.upload_button = ButtonElement(self.driver, self.UPLOAD_BUTTON_LOC)
        self.success_upload_text = TextElement(self.driver, self.SUCCESS_UPLOAD_TEXT_LOC)
        self.upload_file_title = TextElement(self.driver, self.UPLOAD_FILE_TITLE_LOC)
        self.upload_area = ButtonElement(self.driver, self.UPLOAD_AREA_LOC)
        self.file_name_in_area = TextElement(self.driver, self.FILENAME_IN_AREA_LOC)
        self.check_mark = TextElement(self.driver, self.CHECK_MARK_LOC)

    def upload_file(self):
        file = self.config.get_param_by_test_case(self.page_name, 'file')
        self.choose_file.send_keys(file)
        self.upload_button.click()

    def upload_file_dialog_window(self):
        self.upload_area.click()
        time.sleep(1)
        os.popen(r'D:\PycharmProjects\SeleniumFramework\utils\send_path.exe')
        '''в этом месте тоже не получается сделать ожидание кроме как time.sleep.
        асинхронность как я понял селениуму не доступна. Как быть в таких ситуациях?'''
