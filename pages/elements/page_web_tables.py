import allure

from utils.elements.button import Button
from utils.elements.input import Input
from pages.page_base import BasePage


class PageWebTables(BasePage):
    @allure.step("Пеоеход на страницу")
    def step_1_transition(self):
        self._all_transition("Elements", "Web Tables")

    @allure.step("Нажатие кнопки \"ADD\"")
    def step_2_press_button_add(self):
        add_btn = Button("//button[@id='addNewRecordButton']", self._driver)
        add_btn.click_button()

    @allure.step("Ввод имени")
    def step_3_input_name(self, name):
        first_name = Input("//input[@id='firstName']", self._driver)
        first_name.val_input(name)

    @allure.step("Ввод фамили")
    def step_4_input_last_name(self, last_name):
        last_name_input = Input("//input[@id='lastName']", self._driver)
        last_name_input.val_input(last_name)

    @allure.step("Ввод почты")
    def step_5_input_email(self, email):
        email_input = Input("//input[@id='userEmail']", self._driver)
        email_input.val_input(email)

    @allure.step("Ввод возраста")
    def step_6_input_age(self, age):
        age_input = Input("//input[@id='age']", self._driver)
        age_input.val_input(age)

    @allure.step("Ввод зарплаты")
    def step_7_input_salary(self, salary):
        salary_input = Input("//input[@id='salary']", self._driver)
        salary_input.val_input(salary)

    @allure.step("Ввод  депортамента")
    def step_8_input_department(self, department):
        department_input = Input("//input[@id='department']", self._driver)
        department_input.val_input(department)

    @allure.step("Нажатие на кнопку\"submit\"")
    def step_9_press_button_submit(self):
        button_submit = Button(xpath="//button[@id='submit']", driver=self._driver)
        print(button_submit.is_visible())
        button_submit.click_button()
