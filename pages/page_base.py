import time

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _all_transition(self, first_element, second_element):
        menu_1 = self._driver.find_element(By.XPATH, f"//h5[.='{first_element}']")
        menu_1.click()

        menu_2 = self._driver.find_element(By.XPATH, f"//span[.='{second_element}']")
        menu_2.click()

    def _first_element_transition(self, element):
        menu = self._driver.find_element(By.XPATH, f"//h5[.='{element}']")
        menu.click()

    def _second_element_transition(self, element):
        menu = self._driver.find_element(By.XPATH, f"//span[.='{element}']")
        menu.click()

    def _captcha_click(self):
        self._driver.find_element(By.XPATH, "//iframe[starts-with(@name, 'a-') and "
                                            "starts-with(@src, 'https://www.google.com/recaptcha')]").click()

