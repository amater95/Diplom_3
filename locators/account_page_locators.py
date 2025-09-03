from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Заголовок "Вход"
    LOGIN_FORM_TITLE = (By.XPATH, "//h2[text()='Вход']")
    # Поле [Email]
    LOGIN_FORM_EMAIL_INPUT = (By.XPATH, '//input[@name="name"]')
    # Поле [Пароль]
    LOGIN_FORM_PASSWORD_INPUT = (By.XPATH, '//input[@name="Пароль"]')
    # Кнопка [Войти]
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Ссылка "Восстановить пароль"
    PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    # Кнопка [История заказов]
    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
    # Текущий активный раздел
    ACTIVE_ITEM = (By.XPATH, '//a[contains(@class, "Account_link_active")]')
    # Активный раздел "История заказов"
    ACTIVE_ITEM_HISTORY = (By.XPATH, '//a[contains(@class, "Account_link_active") and text()="История заказов"]')
    # Кнопка [Выход]
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
    # Номер первого заказа в истории
    FIRST_ORDER_ID = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]/li[1]/a/div/p[1]")
