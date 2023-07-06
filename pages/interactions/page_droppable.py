from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.page_base import BasePage
from utils.tools.scroling import Scrolling


class PageDroppable(BasePage):
    def transition(self):
        self._first_element_transition("Interactions")
        Scrolling(self._driver).scroll_to(y=600)
        self._second_element_transition("Droppable")

    def drag_and_drop(self):
        draggable = self._driver.find_element(By.XPATH, "//div[@id='draggable']")
        droppable = self._driver.find_element(By.XPATH, "//div[@id='droppable']")
        draggable.click()
        ActionChains(self._driver).drag_and_drop(draggable, droppable).perform()
        assert droppable.text == "Dropped!"
