from selenium.webdriver.common.by import By


class PassRecoverPageLocators:
    # Заголовок "Восстановление пароля"
    PASS_RECOVER_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    # Поле [Email]
    EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')
    # Кнопка [Восстановить]
    PASS_RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    # Поле [Пароль]
    NEW_PASSWORD_FIELD = (By.XPATH, '//input[@name="Введите новый пароль"]')
    NEW_PASSWORD_DIV = (By.XPATH, '//div[input[@name="Введите новый пароль"]]')
    # Кнопка [Открытый глаз/Зачекрунтый глаз]
    BUTTON_PASSWORD_SHOW = (By.XPATH, "//div[@class='input__icon input__icon-action']")
