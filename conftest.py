import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from api_steps.api_client import ApiClient


@pytest.fixture()
def get_driver():
    _options = webdriver.ChromeOptions()
    _options.add_argument("--headless")
    _options.add_argument("--no-sandbox")
    _options.add_argument("--disable-extensions")
    _options.add_argument("--start-maximized")
    _options.add_argument("--window-size=1920,1080")
    _options.add_argument("--disable-dev-shm-usage")
    _options.add_argument("--lang=ru")

    _options.page_load_strategy = "normal"

    prefs = {"download.default_directory": os.path.abspath("data")}
    _options.add_experimental_option("prefs", prefs)

    _driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=_options)

    _driver.implicitly_wait(6)
    _driver.get("https://demoqa.com/")

    yield _driver

    _driver.quit()


@pytest.fixture()
def api_requests():
    return ApiClient(base_path="https://reqres.in/api")
