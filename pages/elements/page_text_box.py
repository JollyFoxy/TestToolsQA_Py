import allure

from utils.elements.button import Button
from utils.elements.input import Input
from utils.elements.text_area import TextArea
from pages.page_base import BasePage


class PageTextBox(BasePage):

    @allure.step("Пеоеход на страницу")
    def transition(self):
        self._all_transition("Elements", "Text Box")

    @allure.step("Ввод имени")
    def input_name(self, name):
        input_full_name = Input("userName", self._driver)
        input_full_name.val_input(name)

    @allure.step("Ввод email")
    def input_email(self, email):
        input_email = Input("userEmail", self._driver)
        input_email.val_input(email)

    @allure.step("Ввод адреса")
    def input_current_address(self, address):
        textarea_current_address = TextArea("currentAddress", self._driver)
        textarea_current_address.val_text_area(address)

    @allure.step("Ввод постоянго адреса")
    def input_permanent_address(self, address):
        textarea_permanent_address = TextArea("permanentAddress", self._driver)
        textarea_permanent_address.val_text_area(address)

    @allure.step("нажатие на кнопку")
    def click_submit(self):
        button_submit = Button(id="submit", driver=self._driver)
        print(button_submit.is_visible())
        button_submit.click_button()
