import time
from ui_element import UiElement
from browser import Browser
class UiComponent(UiElement):

    def __init__(self, by, locator):
        UiElement.__init__(self, by, locator)

    def get_child_element(self, ui_element: UiElement, wait=60):
        self.wait_for_child_element_to_appear(ui_element, wait)
        return self.get_element().find_element(ui_element.by, ui_element.locator)

    def get_child_elements(self, ui_element: UiElement, wait=60):
        self.wait_for_child_element_to_appear(ui_element, wait)
        return self.get_element().find_elements(ui_element.by, ui_element.locator)

    def wait_for_child_element_to_appear(self, ui_element: UiElement, seconds=60, ignore_error=False):
        start = time.time()
        while (time.time() - start) < seconds:
            if self.child_element_exists(ui_element):
                return self
        if not ignore_error:
            raise AssertionError("Locator: {} did not appear in {} seconds!".format(self.locator, seconds))
        else:
            return self

    def child_element_exists(self, ui_element: UiElement):
        if len(self.get_element().find_elements(ui_element.by, ui_element.locator)) > 0:
            return True
        else:
            return False