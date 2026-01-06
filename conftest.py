import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options= Options()
options.add_argument("--start-maximized")

@pytest.fixture
def driver():
    driver= webdriver.Chrome(options=options)
    yield driver
    driver.quit()

