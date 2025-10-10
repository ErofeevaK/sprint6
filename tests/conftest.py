import pytest
from selenium import webdriver
from urls import BASE_URL

# Фикстура веб-драйвера
@pytest.fixture(scope="function")
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1200,600')
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1200, 600)
    driver.get(BASE_URL)
    yield driver
    driver.quit()