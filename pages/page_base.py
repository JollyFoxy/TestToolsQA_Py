from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://demoqa.com/"

    def go_to_site(self):
        return self.driver.get(self.base_url)
