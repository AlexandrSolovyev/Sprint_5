import settings
from locators import StellarburgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSection:

    def test_fillings(self, driver):
        driver.get(settings.URL)

        driver.find_element(*StellarburgersLocators.FILINGS_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.FILINGS_CONTENT))

        name_fillings = driver.find_element(*StellarburgersLocators.FILINGS_CONTENT)

        assert 'Начинки' in name_fillings.text, 'Не удалось перейти в раздел "Начинки"'

    def test_sauces(self, driver):
        driver.get(settings.URL)

        driver.find_element(*StellarburgersLocators.SAUCES_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.SAUCES_CONTENT))

        name_sauces = driver.find_element(*StellarburgersLocators.SAUCES_CONTENT)

        assert 'Соусы' in name_sauces.text, 'Не удалось перейти в раздел "Соусы"'

    def test_buns(self, driver):
        driver.get(settings.URL)

        driver.find_element(*StellarburgersLocators.FILINGS_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.FILINGS_CONTENT))

        driver.find_element(*StellarburgersLocators.BUNS_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            StellarburgersLocators.BUNS_CONTENT))

        name_buns = driver.find_element(*StellarburgersLocators.BUNS_CONTENT)

        assert 'Булки' in name_buns.text, 'Не удалось перейти в раздел "Булки"'
