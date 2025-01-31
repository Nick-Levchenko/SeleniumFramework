from selenium.webdriver.support import expected_conditions as EC

from elements.base_element import BaseElement


class InputElement(BaseElement):

    def send_keys(self, keys):
        self.wait.until(EC.element_to_be_clickable(self.locator)).send_keys(keys)


