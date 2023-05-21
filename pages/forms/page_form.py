import time

import allure
from selenium.webdriver.common.by import By

from pages.page_base import BasePage
from utils.elements.button import Button
from utils.elements.input import Input
from utils.elements.text_area import TextArea
from utils.tools.scroling import Scrolling


class PageForms(BasePage):

    @allure.step("Переход на страницу")
    def transition(self):
        self._all_transition("Forms", "Practice Form")

    @allure.step("Ввод имени")
    def input_first_name(self, name):
        first_name = Input("firstName", self._driver)
        first_name.val_input(name)

    @allure.step("Ввод фамилии")
    def input_last_name(self, last_name):
        name = Input("lastName", self._driver)
        name.val_input(last_name)

    @allure.step("Ввод почты")
    def input_user_email(self, email):
        user_email = Input("userEmail", self._driver)
        user_email.val_input(email)

    @allure.step("Выбор гендора")
    def input_gender(self, gender):
        if gender == "Male":
            self._driver.find_element(By.XPATH, f"//label[.='{gender}']").click()
        elif gender == "Female":
            self._driver.find_element(By.XPATH, f"//label[.='{gender}']").click()
        else:
            self._driver.find_element(By.XPATH, "//label[.='Other']").click()

    @allure.step("Ввод телефона")
    def input_phone(self, phone):
        user_phone = Input("userNumber", self._driver)
        user_phone.val_input(phone)

    @allure.step("Ввод даты рождения")
    # Костыль момент т.к. на этом моменте ежели отчистьть всё поле сайт ляжет...
    # Знаю так делать не стоит, но продолжать надо...
    def date_of_birth(self, date):
        date_of_birth = Input("dateOfBirthInput", self._driver)
        for i in range(10):
            date_of_birth.press_back_space_input()
            if i == 9:
                date_of_birth.val_input(date)
                for j in range(10):
                    date_of_birth.press_arrow_left_input()
                date_of_birth.press_back_space_input()
        date_of_birth.press_enter_input()

    @allure.step("Выбор хобби")
    def input_hobbies(self, arg="", arg1="", arg2=""):
        if arg != "":
            self._driver.find_element(By.XPATH, f"//label[.='{arg}']").click()
        if arg1 != "":
            self._driver.find_element(By.XPATH, f"//label[.='{arg1}']").click()
        if arg2 != "":
            self._driver.find_element(By.XPATH, f"//label[.='{arg2}']").click()

    @allure.step("Загрузка аватара ")
    def avatar(self, file_path: str = "/Users/pavel.mizirev/PycharmProjects/TestToolsQA_Py/img/foxy.png"):
        avatar_input = Input("uploadPicture", self._driver)
        avatar_input.val_input(file_path)

    @allure.step("Ввод адреса")
    def current_address_input(self, address):
        current_address = TextArea("currentAddress", self._driver)
        current_address.val_text_area(address)

    def scroll(self):
        widgets = self._driver.find_element(By.XPATH, "//div[.='Widgets']")
        widgets.click()
        time.sleep(0.05)
        Scrolling(self._driver).scroll_to(y=1000)

    @allure.step("Нажатие на кнопку")
    def click_submit(self):
        self.scroll()
        button_submit = Button(id="submit", driver=self._driver)
        button_submit.click_button()

    @allure.step("Закрыте окна")
    def click_close(self):
        button_close = Button(id="closeLargeModal", driver=self._driver)
        button_close.click_button()
