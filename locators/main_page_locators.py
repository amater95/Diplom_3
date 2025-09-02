from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка [Личный кабинет]
    ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    # Кнопка [Конструктор]
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Кнопка [Лента заказов]
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    # Заголовок "Соберите бургер"
    MAKE_BURGER_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    # Ингредиент "Флюоресцентная булка R2-D3"
    INGREDIENT_ELEM = (By.XPATH, ".//a[@href='/ingredient/{}']")
    # Счетчик ингредиентов
    INGREDIENT_ELEM_COUNTER = (By.XPATH, ".//a[@href='/ingredient/{}']/div[contains(@class, 'counter_counter')]/p")
    # Заголовок окна с деталями об ингредиенте
    DETAILS_INGREDIENT_TITLE = (By.XPATH, './/h2[text()="Детали ингредиента"]')
    # Кнопка [x] в окне с деталями об ингредиенте
    DETAILS_INGREDIENT_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    # Корзина
    ORDER_BASKET = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    # Кнопка [Оформить заказ]
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    # Заголовок идентификатора заказа
    ORDER_WINDOW_TITLE= (By.XPATH, ".//div[contains(@class, 'Modal_modal__contentBox')]/p")
    # Номер заказа
    ORDER_NUMBER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')
    # Кнопка [x] в окне с номером заказа
    FINISH_ORDER_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
