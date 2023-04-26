import time

from selenium.webdriver import ActionChains

from pages.page_base import BasePage
from utils.elements.div import Div
from utils.elements.p import P
from utils.tools.scroling import Scrolling


class PageDroppable(BasePage):
    def step_1_transition(self):
        self._first_element_transition("Interactions")
        Scrolling(self._driver).scroll_to(y=600)
        self._second_element_transition("Droppable")
    def step_2_drag_and_drop(self):
        draggable = Div("//div[@id='draggable']", self._driver)
        droppable = Div("//div[@id='droppable']", self._driver)
        ActionChains(self._driver).drag_and_drop(draggable, droppable).perform()
        time.sleep(5)
        message = P("//div[.='Dropped!']", self._driver)
        assert message.get_text() == "Dropped!"

