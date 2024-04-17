from selenium.webdriver.common.by import By


class StellarburgersLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_TO_ACCOUNT = (By.XPATH,
                        "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                        "button_button_size_large__G21Vg']")

    # Кнопка "Зарегистрироваться" для новых клиентов
    REGISTRATION_BUTTON_NEW = (By.CSS_SELECTOR, 'a.Auth_link__1fOlj[href="/register"]')

    # Поле "Имя" на странице регистрации
    REGISTRATION_INPUT_NAME = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")

    # Поле "Email" на странице регистрации
    REGISTRATION_INPUT_EMAIL = (By.XPATH,
                                "//fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default'and "
                                "contains (@name, 'name')]")

    # Поле "Пароль" на странице регистрации
    REGISTRATION_INPUT_PASSWORD = (
        By.XPATH, "//input[@class='text input__textfield text_type_main-default'and contains (@type,'password')]")

    # Кнопка "зарегистрироваться" на странице регистрации
    REGISTRATION_BUTTON = (By.XPATH,
                           "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                           "button_button_size_medium__3zxIa']")

    # Кнопка "Войти"
    BUTTON_FOR_LOGIN = By.XPATH, './/button[text() = "Войти"]'

    # Кнопка Оформить заказ
    BUTTON_CHECKOUT = By.XPATH, './/button[text() = "Оформить заказ"]'

    # кнопка Личный кабинет
    BUTTON_PROFILE = By.XPATH, './/a[@href = "/account"]'

    # кнопка Выйти на странице профиля
    BUTTON_EXIT = By.XPATH, ".//button[text() = 'Выход']"

    # тултип при некорректных данных введенного пароля на странице регистрации
    ERROR_VALIDATION_PASSWORD = By.XPATH, './/p[text() = "Некорректный пароль"]'

    # кнопка Войти в аккаунт на главной странице
    BUTTON_LOGIN_MAIN_PAGE = By.XPATH, './/button[text() = "Войти в аккаунт"]'

    # поле ввода email на странице авторизации
    EMAIL_FOR_LOGIN = By.XPATH, './/input[@name = "name"]'

    # поле ввода пароля на странице авторизации
    PASSWORD_FOR_LOGIN = By.XPATH, './/input[@name  = "Пароль"]'

    # кнопка Войти на странице регистрации
    BUTTON_LOGIN_IN_REG = By.XPATH, './/a[@href="/login"]'

    # кнопка Войти на 1-й странице восстановления пароля
    BUTTON_LOGIN_FOR_RECOVERY = By.XPATH, './/a[text() = "Войти"]'

    # поле ввода для email на 1-й странице восстановления пароля
    EMAIL_FOR_RECOVERY = By.XPATH, './/input[@name = "name"]'

    # кнопка восстановить на 1-й странице восстановления пароля
    BUTTON_FOR_RECOVERY = By.XPATH, './/button[ text() = "Восстановить"]'

    # поле ввода пароля на странице восстановления пароля
    PASSWORD_FOR_RESET = By.XPATH, './/input[@type = "password"]'

    # кнопка Начинки
    FILINGS_BUTTON = By.XPATH, './/span[text() = "Начинки"]'

    # наименование раздела Начинки
    FILINGS_CONTENT = By.XPATH, './/h2[text() = "Начинки"]'

    # кнопка Соусы
    SAUCES_BUTTON = By.XPATH, './/span[text() = "Соусы"]'

    # наименование раздела Соусы
    SAUCES_CONTENT = By.XPATH, './/h2[text() = "Соусы"]'

    # кнопка Булки
    BUNS_BUTTON = By.XPATH, './/span[text() = "Булки"]'

    # наименование раздела Булки
    BUNS_CONTENT = By.XPATH, './/h2[text() = "Булки"]'

    # кнопка конструктор
    BUTTON_CONSTRUCTOR = By.XPATH, './/p[text() = "Конструктор"]'

    # кнопка Выйти на странице профиля
    BUTTON_EXIT = By.XPATH, ".//button[text() = 'Выход']"
