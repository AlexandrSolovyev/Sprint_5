from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
from locators import StellarburgersLocators
from generator_email import random_email


class TestRegistration:
    def test_registration_and_login_new_user(self, driver):
        wait = WebDriverWait(driver, 5)
        driver.get(settings.URL + '/register')
        # Находим поле "Имя", вводим данные
        name = driver.find_element(*StellarburgersLocators.REGISTRATION_INPUT_NAME)
        name.send_keys("Test registration name")

        # Находим поле "Email" и заполняем его данными из рандомайзера generator_email
        email = driver.find_element(*StellarburgersLocators.REGISTRATION_INPUT_EMAIL)
        email.send_keys(random_email)
        value_email = driver.find_element(*StellarburgersLocators.REGISTRATION_INPUT_EMAIL).get_attribute('value')

        # Находим поле "Пароль" и заполняем его
        password = driver.find_element(*StellarburgersLocators.REGISTRATION_INPUT_PASSWORD)
        password.send_keys("123QWEasd")

        # Находим кнопку "Зарегистрироваться" и кликаем по ней
        button = driver.find_element(*StellarburgersLocators.REGISTRATION_BUTTON)
        button.click()
        wait.until(expected_conditions.visibility_of_element_located(*StellarburgersLocators.BUTTON_FOR_LOGIN))

        driver.find_element(*StellarburgersLocators.REGISTRATION_INPUT_EMAIL).send_keys(value_email)
        driver.find_element(*StellarburgersLocators.REGISTRATION_INPUT_PASSWORD).send_keys("123QWEasd")
        driver.find_element(*StellarburgersLocators.BUTTON_FOR_LOGIN).click()
        wait.until(expected_conditions.visibility_of_element_located(StellarburgersLocators.BUTTON_CHECKOUT))
        driver.find_element(*StellarburgersLocators.BUTTON_PROFILE).click()
        wait.until(expected_conditions.visibility_of_element_located(StellarburgersLocators.BUTTON_EXIT))

        current_url_after_login = driver.current_url

        assert '/account/profile' in current_url_after_login, ('Не удалось зарегестироваться и войти недавно '
                                                               'зарегестрированному пользователю')

    def test_password_validation_negative(self, driver):
        driver.get(settings.URL + '/register')

        name = driver.find_element(*StellarburgersLocators.REGISTRATION_INPUT_NAME)
        name.send_keys("Test registration name")
        email = driver.find_element(*StellarburgersLocators.REGISTRATION_INPUT_EMAIL)
        email.send_keys(random_email)
        password = driver.find_element(*StellarburgersLocators.REGISTRATION_INPUT_PASSWORD)
        password.send_keys("123QW")

        button = driver.find_element(*StellarburgersLocators.REGISTRATION_BUTTON)
        button.click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            StellarburgersLocators.ERROR_VALIDATION_PASSWORD))

        current_url_before_login = driver.current_url

        assert 'login' not in current_url_before_login, 'Удачная регистрация с паролем < 6 символов'
