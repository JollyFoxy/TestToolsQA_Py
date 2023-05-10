import allure
from selenium.webdriver.common.by import By

from pages.page_base import BasePage
from utils.elements.button import Button
from utils.tools.scroling import Scrolling
from utils.tools.waiting import Waiting
from selenium.webdriver.support.color import Color


class PageTimeButton(BasePage):

    @allure.step("Переход на страницу")
    def transition(self):
        self._first_element_transition("Elements")
        Scrolling(self._driver).scroll_to(y=300)
        self._second_element_transition("Dynamic Properties")

    @allure.step("Ожидание скрытой кнопки")
    def timeout_button(self):
        timeout_button = Button(id="visibleAfter", driver=self._driver)
        timeout_button.click_button()
        self._driver.refresh()

    @allure.step("Ожидание работы кнопки")
    def enable_button(self):
        no_clickable_button = Button(id="enableAfter", driver=self._driver)
        Waiting(self._driver).wait_to_element_clickable(no_clickable_button.get_element())
        self._driver.refresh()

    @allure.step("Ожидание изменения цвета")
    def color_change_button(self):
        color_change_button = Color.from_string(self._driver.find_element(By.ID, "colorChange")
                                                    .value_of_css_property('color'))
        assert color_change_button.rgba == "rgba(220, 53, 69, 1)"
        self._driver.refresh()
