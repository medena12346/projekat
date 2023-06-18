import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

@pytest.fixture
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    project_driver = webdriver.Chrome(service=service)
    yield project_driver
    time.sleep(5)
    project_driver.quit()