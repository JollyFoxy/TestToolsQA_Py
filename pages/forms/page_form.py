import allure
from selenium.webdriver.common.by import By

from pages.page_base import BasePage
from utils.elements.button import Button
from utils.elements.input import Input
from utils.elements.text_area import TextArea
from utils.tools.scroling import Scrolling


class PageForms(BasePage):

    @allure.step("")
    def step_1_transition(self):
        self._all_transition("Forms", "Practice Form")

    @allure.step("")
    def step_2_input_first_name(self, name):
        first_name = Input("//input[@id='firstName']", self._driver)
        first_name.val_input(name)

    @allure.step("")
    def step_3_input_last_name(self, last_name):
        name = Input("//input[@id='lastName']", self._driver)
        name.val_input(last_name)

    @allure.step("")
    def step_4_input_user_email(self, email):
        user_email = Input("//input[@id='userEmail']", self._driver)
        user_email.val_input(email)

    @allure.step("")
    def step_5_input_gender(self, gender):
        if gender == "Male":
            self._driver.find_element(By.XPATH, f"//label[.='{gender}']").click()
        elif gender == "Female":
            self._driver.find_element(By.XPATH, f"//label[.='{gender}']").click()
        else:
            self._driver.find_element(By.XPATH, "//label[.='Other']").click()

    @allure.step("")
    def step_6_input_phone(self, phone):
        user_phone = Input("//input[@id='userNumber']", self._driver)
        user_phone.val_input(phone)

    @allure.step("")
    # Костыль момент т.к. на этом моменте ежели отчистьть всё поле сайт ляжет...
    # Знаю так делать не стоит, но продолжать надо...
    def step_7_date_of_birth(self, date):
        date_of_birth = Input("//input[@id='dateOfBirthInput']", self._driver)
        for i in range(10):
            date_of_birth.press_back_space_input()
            if i == 9:
                date_of_birth.val_input(date)
                for j in range(10):
                    date_of_birth.press_arrow_left_input()
                date_of_birth.press_back_space_input()
        date_of_birth.press_enter_input()

    @allure.step("")
    def step_8_input_hobbies(self, arg="", arg1="", arg2=""):
        if arg != "":
            self._driver.find_element(By.XPATH, f"//label[.='{arg}']").click()
        if arg1 != "":
            self._driver.find_element(By.XPATH, f"//label[.='{arg1}']").click()
        if arg2 != "":
            self._driver.find_element(By.XPATH, f"//label[.='{arg2}']").click()

    @allure.step("")
    def step_9_avatar(self):
        pass

    @allure.step("")
    def step_10_current_address_input(self, address):
        current_address = TextArea("//textarea[@id='currentAddress']", self._driver)
        current_address.val_text_area(address)

    @allure.step("нажатие на кнопку")
    def step_11_click_submit(self):
        self._driver.find_element(By.XPATH, "//div[.='Widgets']").click()
        Scrolling(self._driver).scroll_to(y=500)
        button_submit = Button(xpath="//button[@id='submit']", driver=self._driver)
        print(button_submit.is_visible())
        button_submit.click_button()

    @allure.step("")
    def step_12_click_close(self):
        button_close = Button("//button[@id='closeLargeModal']", self._driver)
        button_close.click_button()