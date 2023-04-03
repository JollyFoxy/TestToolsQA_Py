import allure

from elements.button import Button
from elements.input import Input
from pages.page_base import BasePage


class PageWebTables(BasePage):
    @allure.step("Пеоеход на страницу")
    def step_1(self):
        self._go_to_site()
        self._all_transition("Elements", "Web Tables")

    @allure.step("")
    def step_2(self):
        add_btn = Button("//button[@id='addNewRecordButton']", self._driver)
        add_btn.click_button()

    @allure.step("")
    def step_3(self, name):
        first_name = Input("//input[@id='firstName']", self._driver)
        first_name.val_input(name)

    @allure.step("")
    def step_4(self, last_name):
        last_name_input = Input("//input[@id='lastName']", self._driver)
        last_name_input.val_input(last_name)

    @allure.step("")
    def step_5(self, email):
        email_input = Input("//input[@id='userEmail']", self._driver)
        email_input.val_input(email)

    @allure.step("")
    def step_6(self, age):
        age_input = Input("//input[@id='age']", self._driver)
        age_input.val_input(age)

    @allure.step("")
    def step_7(self, salary):
        salary_input = Input("//input[@id='salary']", self._driver)
        salary_input.val_input(salary)

    @allure.step("")
    def step_8(self, department):
        department_input = Input("//input[@id='department']", self._driver)
        department_input.val_input(department)

    @allure.step("нажатие на кнопку")
    def step_9(self):
        button_submit = Button(xpath="//button[@id='submit']", driver=self._driver)
        print(button_submit.is_visible())
        button_submit.click_button()
