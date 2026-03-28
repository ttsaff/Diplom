import sys
import os
import pytest
from selenium import webdriver

sys.path.append(os.path.abspath("."))
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
