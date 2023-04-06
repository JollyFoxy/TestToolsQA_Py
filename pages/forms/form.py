import allure
from selenium.webdriver.common.by import By

from pages.page_base import BasePage
from utils.elements.input import Input


class StepForms(BasePage):

    @allure.step("")
    def step_1_transition(self):
        self._all_transition("Forms", "Practice Form")

    @allure.step("")
    def step_2_input_first_name(self, name):
        first_name = Input("//input[@id='firstName']", self._driver)
        first_name.val_input(name)

    @allure.step("")
    def step_3_input_last_name(self, last_name):
        last_name = Input("//input[@id='lastName']", self._driver)
        last_name.val_input(last_name)

    @allure.step("")
    def step_4_input_user_email(self, email):
        user_email = Input("//input[@id='userEmail']", self._driver)
        user_email.val_input(email)

    @allure.step("")
    def step_5_input_gender(self, gender):
        self._driver.find_element(By.LINK_TEXT, gender).click()

    @allure.step("")
    def step_6_input_phone(self, phone):
        user_phone = Input("//input[@id='userNumber']", self._driver)
        user_phone.val_input(phone)

    @allure.step("")
    def step_7_date_of_birth(self, date):
        date_of_birth = Input("//input[@id='dateOfBirthInput']", self._driver)
        
