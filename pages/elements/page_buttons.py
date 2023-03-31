from elements.button import Button
from elements.p import P
from pages.page_base import BasePage


class PageButtons(BasePage):
    def step_transition(self):
        self._go_to_site()
        self._all_transition("Elements", "Buttons")

    def step_dinamic_click_button(self):
        dinamic_button = Button("/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button", self.driver)
        dinamic_button.click_button()
        dinamic_massage = P("//p[@id='dynamicClickMessage']", self.driver)
        assert dinamic_massage.get_text() == "You have done a dynamic click"

    def step_right_click_button(self):
        right_click_button = Button("//button[@id='rightClickBtn']", self.driver)
        right_click_button.right_click_button()
        right_click_massage = P("//p[@id='rightClickMessage']", self.driver)
        assert right_click_massage.get_text() == "You have done a right click"

    def step_double_click_button(self):
        double_click_button = Button("//button[@id='doubleClickBtn']", self.driver)
        double_click_button.double_click_button()
        double_click_massage = Button("//p[@id='doubleClickMessage']", self.driver)
        assert double_click_massage.get_text() == "You have done a double click"
