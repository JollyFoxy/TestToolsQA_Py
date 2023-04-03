import allure
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self.__base_url = "https://demoqa.com/"

    def _go_to_site(self):
        return self._driver.get(self.__base_url)

    def _all_transition(self, first_element, second_element):
        elements_menu = self._driver.find_element(By.XPATH, f"//h5[.='{first_element}']")
        elements_menu.click()

        text_box_menu = self._driver.find_element(By.XPATH, f"//span[.='{second_element}']")
        text_box_menu.click()

    def _first_element_transition(self, element):
        elements_menu = self._driver.find_element(By.XPATH, f"//h5[.='{element}']")
        elements_menu.click()

    def second_element_transition(self, element):
        elements_menu = self._driver.find_element(By.XPATH, f"//span[.='{element}']")
        elements_menu.click()
