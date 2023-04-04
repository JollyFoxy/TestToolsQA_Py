import allure

from elements.button import Button
from elements.input import Input
from elements.text_area import TextArea
from pages.page_base import BasePage


class PageTextBox(BasePage):

    @allure.step("Пеоеход на страницу")
    def step_transition(self):
        self._all_transition("Elements", "Text Box")

    @allure.step("Ввод имени")
    def step_input_name(self, name):
        input_full_name = Input(xpath="//input[@id='userName']", driver=self._driver)
        input_full_name.val_input(name)

    @allure.step("Ввод email")
    def step_input_email(self, email):
        input_email = Input(xpath="//input[@id='userEmail']", driver=self._driver)
        input_email.val_input(email)

    @allure.step("Ввод адреса")
    def step_input_current_address(self, address):
        textarea_current_address = TextArea(xpath="//textarea[@id='currentAddress']", driver=self._driver)
        textarea_current_address.val_input(address)

    @allure.step("Ввод постоянго адреса")
    def step_input_permanent_address(self, address):
        textarea_permanent_address = TextArea(xpath="//textarea[@id='permanentAddress']", driver=self._driver)
        textarea_permanent_address.val_input(address)

    @allure.step("нажатие на кнопку")
    def step_click_submit(self):
        button_submit = Button(xpath="//button[@id='submit']", driver=self._driver)
        print(button_submit.is_visible())
        button_submit.click_button()
