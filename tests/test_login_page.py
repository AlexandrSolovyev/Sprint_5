from locators import StellarburgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings


class TestLogin:

    def test_login_main_paige(self, driver):
        driver.get(settings.URL)
        driver.find_element(*StellarburgersLocators.BUTTON_LOGIN_MAIN_PAGE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.BUTTON_FOR_LOGIN))

        driver.find_element(*StellarburgersLocators.EMAIL_FOR_LOGIN).send_keys(settings.user_creds_login)
        driver.find_element(*StellarburgersLocators.PASSWORD_FOR_LOGIN).send_keys(settings.user_creds_password)
        driver.find_element(*StellarburgersLocators.BUTTON_FOR_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.BUTTON_CHECKOUT))

        driver.find_element(*StellarburgersLocators.BUTTON_PROFILE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.BUTTON_EXIT))
        current_profile_url = driver.current_url

        assert '/account/profile' in current_profile_url, 'Не удалось авторизоваться'

    def test_login_profile(self, driver):
        driver.get(settings.URL)
        driver.find_element(*StellarburgersLocators.BUTTON_PROFILE).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.BUTTON_FOR_LOGIN))

        driver.find_element(*StellarburgersLocators.EMAIL_FOR_LOGIN).send_keys(settings.user_creds_login)
        driver.find_element(*StellarburgersLocators.PASSWORD_FOR_LOGIN).send_keys(settings.user_creds_password)
        driver.find_element(*StellarburgersLocators.BUTTON_FOR_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.BUTTON_CHECKOUT))
        current_login_url = driver.current_url

        assert 'login' not in current_login_url, 'Не удалось авторизоваться'

    def test_login_registration(self, driver):
        driver.get(settings.URL + '/registration')
        driver.find_element(*StellarburgersLocators.BUTTON_LOGIN_IN_REG).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.EMAIL_FOR_LOGIN))

        driver.find_element(*StellarburgersLocators.EMAIL_FOR_LOGIN).send_keys(settings.user_creds_login)
        driver.find_element(*StellarburgersLocators.PASSWORD_FOR_LOGIN).send_keys(settings.user_creds_password)
        driver.find_element(*StellarburgersLocators.BUTTON_FOR_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.BUTTON_CHECKOUT))
        current_login_url = driver.current_url

        assert 'login' not in current_login_url, 'Не удалось авторизоваться'

    def test_login_recovery_password(self, driver):
        driver.get(settings.URL + '/forgot-password')
        driver.find_element(*StellarburgersLocators.BUTTON_LOGIN_FOR_RECOVERY).click()

        driver.find_element(*StellarburgersLocators.EMAIL_FOR_LOGIN).send_keys(settings.user_creds_login)
        driver.find_element(*StellarburgersLocators.PASSWORD_FOR_LOGIN).send_keys(settings.user_creds_password)
        driver.find_element(*StellarburgersLocators.BUTTON_FOR_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.BUTTON_CHECKOUT))
        current_login_url = driver.current_url

        assert 'login' not in current_login_url, 'Не удалось авторизоваться'

    def test_login_reset_password(self, driver):
        driver.get(settings.URL + '/forgot-password')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.EMAIL_FOR_RECOVERY))

        driver.find_element(*StellarburgersLocators.EMAIL_FOR_RECOVERY).send_keys(settings.user_creds_login)
        driver.find_element(*StellarburgersLocators.BUTTON_FOR_RECOVERY).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.PASSWORD_FOR_RESET))

        driver.find_element(*StellarburgersLocators.BUTTON_LOGIN_FOR_RECOVERY).click()

        driver.find_element(*StellarburgersLocators.EMAIL_FOR_LOGIN).send_keys(settings.user_creds_login)
        driver.find_element(*StellarburgersLocators.PASSWORD_FOR_LOGIN).send_keys(settings.user_creds_password)
        driver.find_element(*StellarburgersLocators.BUTTON_FOR_LOGIN).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.BUTTON_CHECKOUT))
        current_login_url = driver.current_url

        assert 'login' not in current_login_url, 'Неверные логин, или пароль'
