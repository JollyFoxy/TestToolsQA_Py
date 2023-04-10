from selenium.webdriver.chrome.webdriver import WebDriver


class Scrolling:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def scroll_to(self, x=0, y=0):
        self._driver.execute_script(f"window.scrollTo({x},{y})")
