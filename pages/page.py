import allure
from selenium.webdriver.common.by import By
from pages.page_base import BasePage
from elements.button import Button


class StepsTest1(BasePage):

    @allure.step("пеоеход на страницу")
    def step_transition(self):
        elements_menu = self.driver.find_element(By.XPATH, "//h5[.='Elements']")
        elements_menu.click()

        text_box_menu = self.driver.find_element(By.XPATH, "//span[.='Text Box']")
        text_box_menu.click()

    @allure.step("ввод имени")
    def step_input_name(self, name):
        input_full_name = self.driver.find_element(By.XPATH, "//input[@id='userName']")
        input_full_name.click()
        input_full_name.send_keys(name)

    @allure.step("нажатие на кнопку")
    def step_click_submit(self):
        button_submit = Button(xpath="//button[@id='submit']", driver=self.driver)
        print(button_submit.is_visible())
        button_submit.click_button()
