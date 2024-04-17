from locators import StellarburgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestJumpPage:

    def test_jump_pofile(self, driver, login_user):
        wait = WebDriverWait(driver, 5)
        wait.until(expected_conditions.visibility_of_element_located(StellarburgersLocators.BUTTON_PROFILE))
        driver.find_element(*StellarburgersLocators.BUTTON_PROFILE).click()

        wait.until(expected_conditions.visibility_of_element_located(StellarburgersLocators.BUTTON_EXIT))
        current_profile_url = driver.current_url

        assert '/account/profile' in current_profile_url, 'Не перейти на страницу профиля'

    def test_jump_constructor(self, driver, login_user):
        wait = WebDriverWait(driver, 5)
        wait.until(expected_conditions.visibility_of_element_located(StellarburgersLocators.BUTTON_CONSTRUCTOR))
        driver.find_element(*StellarburgersLocators.BUTTON_CONSTRUCTOR).click()

        wait.until(expected_conditions.visibility_of_element_located(StellarburgersLocators.BUTTON_CHECKOUT))
        current_main_paige_url = driver.current_url

        assert 'https://stellarburgers.nomoreparties.site/' in current_main_paige_url, ('Не перейти на страницу '
                                                                                        'конструктора')

    def test_logout(self, driver, login_user):
        wait = WebDriverWait(driver, 5)
        wait.until(expected_conditions.visibility_of_element_located(StellarburgersLocators.BUTTON_PROFILE))
        driver.find_element(*StellarburgersLocators.BUTTON_PROFILE).click()
        wait.until(expected_conditions.visibility_of_element_located(StellarburgersLocators.BUTTON_EXIT))
        driver.find_element(*StellarburgersLocators.BUTTON_EXIT).click()
        wait.until(expected_conditions.visibility_of_element_located(StellarburgersLocators.BUTTON_PROFILE))
        driver.find_element(*StellarburgersLocators.BUTTON_PROFILE).click()

        wait.until(expected_conditions.visibility_of_element_located(StellarburgersLocators.EMAIL_FOR_LOGIN))
        current_profile_url = driver.current_url

        assert '/account/profile' not in current_profile_url, 'Не удалось выйти'
