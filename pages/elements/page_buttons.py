import allure

from utils.elements.button import Button
from utils.elements.p import P
from pages.page_base import BasePage


class PageButtons(BasePage):

    @allure.step("Переход на страницу")
    def step_1_transition(self):
        self._all_transition("Elements", "Buttons")

    @allure.step("Один клик")
    def step_2_dinamic_click_button(self):
        dinamic_button = Button("/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button", self._driver)
        dinamic_button.click_button()
        dinamic_massage = P("//p[@id='dynamicClickMessage']", self._driver)
        assert dinamic_massage.get_text() == "You have done a dynamic click"

    @allure.step("Правый клик")
    def step_3_right_click_button(self):
        right_click_button = Button("//button[@id='rightClickBtn']", self._driver)
        right_click_button.right_click_button()
        right_click_massage = P("//p[@id='rightClickMessage']", self._driver)
        assert right_click_massage.get_text() == "You have done a right click"

    @allure.step("Двойной клик")
    def step_4_double_click_button(self):
        double_click_button = Button("//button[@id='doubleClickBtn']", self._driver)
        double_click_button.double_click_button()
        double_click_massage = Button("//p[@id='doubleClickMessage']", self._driver)
        assert double_click_massage.get_text() == "You have done a double click"
