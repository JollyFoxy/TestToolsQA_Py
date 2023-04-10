from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Waiting:
    def __init__(self, driver: WebDriver, wait_time=6):
        self._driver = driver
        self._wait_time = wait_time
        self.wait = WebDriverWait(self._driver, self._wait_time)

    def wait_to_element_clickable(self, element):
        self.wait.until(EC.element_to_be_clickable(element))

    def wait_all_of(self, *ec):
        self.wait.until(EC.any_of(ec))
