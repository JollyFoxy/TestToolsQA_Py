import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def config_option():
    _options = webdriver.ChromeOptions()
    _options.add_argument("--headless")
    _options.add_argument("--no-sandbox")
    _options.add_argument("--disable-extensions")
    _options.add_argument("--start-maximized")
    _options.add_argument("--window-size=1920,1080")
    _options.add_argument("--disable-dev-shm-usage")

    _options.page_load_strategy = "normal"

    prefs = {"download.default_directory": os.path.abspath("data")}
    _options.add_experimental_option("prefs", prefs)
    return _options


@pytest.fixture()
def get_driver(config_option):
    _driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=config_option)

    _driver.implicitly_wait(6)
    _driver.get("https://demoqa.com/")

    yield _driver

    _driver.quit()
