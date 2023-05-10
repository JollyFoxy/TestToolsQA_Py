import allure

from utils.elements.button import Button
from utils.elements.input import Input
from pages.page_base import BasePage


class PageWebTables(BasePage):
    @allure.step("Пеоеход на страницу")
    def transition(self):
        self._all_transition("Elements", "Web Tables")

    @allure.step("Нажатие кнопки \"ADD\"")
    def press_button_add(self):
        add_btn = Button(id="addNewRecordButton", driver=self._driver)
        add_btn.click_button()

    @allure.step("Ввод имени")
    def input_name(self, name):
        first_name = Input("firstName", self._driver)
        first_name.val_input(name)

    @allure.step("Ввод фамили")
    def input_last_name(self, last_name):
        last_name_input = Input("lastName", self._driver)
        last_name_input.val_input(last_name)

    @allure.step("Ввод почты")
    def input_email(self, email):
        email_input = Input("userEmail", self._driver)
        email_input.val_input(email)

    @allure.step("Ввод возраста")
    def input_age(self, age):
        age_input = Input("age", self._driver)
        age_input.val_input(age)

    @allure.step("Ввод зарплаты")
    def input_salary(self, salary):
        salary_input = Input("salary", self._driver)
        salary_input.val_input(salary)

    @allure.step("Ввод  депортамента")
    def input_department(self, department):
        department_input = Input("department", self._driver)
        department_input.val_input(department)

    @allure.step("Нажатие на кнопку\"submit\"")
    def press_button_submit(self):
        button_submit = Button(id="submit", driver=self._driver)
        print(button_submit.is_visible())
        button_submit.click_button()
