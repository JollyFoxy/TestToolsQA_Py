import allure

from pages.book_store.page_login import PageLogin
from pages.page_base import BasePage
from utils.elements.button import Button
from utils.elements.input import Input


class PageRegister(BasePage):

    @allure.step("Переход")
    def transition(self):
        PageLogin(self._driver).transition()

    @allure.step("Нажатие кнопки \"New User\"")
    def new_user(self):
        PageLogin(self._driver).new_user()

    @allure.step("Ввод в поле \"First Name\"")
    def input_first_name(self, name: str):
        first_name = Input("firstname", self._driver)
        first_name.val_input(name)

    @allure.step("Ввод в поле \"Last Name\"")
    def input_last_name(self, name: str):
        last_name = Input("lastname", self._driver)
        last_name.val_input(name)

    @allure.step("Ввод в поле \"User Name\"")
    def input_user_name(self, name: str):
        user_name = Input("userName", self._driver)
        user_name.val_input(name)

    @allure.step("Ввод в поле \"Password\"")
    def input_password(self, pas: str):
        password = Input("password", self._driver)
        password.val_input(pas)

    @allure.step("Нажатие на капчу")
    def captcha(self):
        self._captcha_click()

    @allure.step("Нажатие на кнопку \"Register\"")
    def register(self):
        register_btn = Button(id="register", driver=self._driver)
        register_btn.click_button()
