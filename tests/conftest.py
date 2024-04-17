import pytest
import settings
from locators import StellarburgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


@pytest.fixture
def login_user(driver):
    driver.get(settings.URL + '/login')
    driver.find_element(*StellarburgersLocators.EMAIL_FOR_LOGIN).send_keys(settings.user_creds_login)
    driver.find_element(*StellarburgersLocators.PASSWORD_FOR_LOGIN).send_keys(settings.user_creds_password)
    driver.find_element(*StellarburgersLocators.BUTTON_FOR_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        StellarburgersLocators.BUTTON_CHECKOUT))


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver
    driver.quit()
