from elements.base_element import BaseElement


class InputElement(BaseElement):

    def send_keys(self, keys):
        self.wait_for_clickable().send_keys(keys)
