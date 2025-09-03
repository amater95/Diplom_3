import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Нажатие на [Лента заказов] в хедере')
    def move_to_list_orders(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)


    @allure.step('Нажатие на [Конструктор] в хедере')
    def move_to_constructor(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)


    @allure.step('Нажатие на [Личный кабинетъ] в хедере')
    def move_to_account(self):
        self.click_to_element(MainPageLocators.ACCOUNT_BUTTON)


    @allure.step('Получение заголовок страницы')
    def get_title_text(self):
        return self.get_element_text(MainPageLocators.MAKE_BURGER_TITLE)


    @allure.step('Ожидание отображения главной страницы')
    def wait_page_visible(self):
        self.find_element(MainPageLocators.MAKE_BURGER_TITLE)


    @allure.step('Нажатие на ингредиент')
    def click_on_ingredient(self, ingredient_id):
        locator = self.format_locator(MainPageLocators.INGREDIENT_ELEM, ingredient_id)
        self.click_to_element(locator)


    @allure.step('Получение заголовка деталей ингредиента')
    def get_ingredient_details_title(self):
        return self.get_element_text(MainPageLocators.DETAILS_INGREDIENT_TITLE)


    @allure.step('Ожидание отображения деталей ингредиента')
    def wait_ingredient_details_window(self):
        self.find_element(MainPageLocators.DETAILS_INGREDIENT_TITLE)


    @allure.step('Нажатие на [x] в окне деталей ингредиента')
    def close_ingredient_details_window(self):
        self.click_to_element(MainPageLocators.DETAILS_INGREDIENT_CLOSE_BUTTON)


    @allure.step('Ожидание закрытия деталей ингредиента ')
    def wait_ingredient_details_window_is_closed(self):
        return self.check_invisibility(MainPageLocators.DETAILS_INGREDIENT_TITLE)


    @allure.step('Получение значения счетчика ингредиента')
    def get_ingredient_counter_value(self, ingredient_id):
        counter_locator = self.format_locator(MainPageLocators.INGREDIENT_ELEM_COUNTER, ingredient_id)
        return int(self.get_element_text(counter_locator))


    @allure.step('Добавление ингредиента')
    def add_ingredients_to_order(self, ingredient_id):
        ingredient_locator = self.format_locator(MainPageLocators.INGREDIENT_ELEM, ingredient_id)
        self.move_element(ingredient_locator, MainPageLocators.ORDER_BASKET)
    

    @allure.step('Нажатие на [Оформить заказ]')
    def click_order_button(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON)


    @allure.step('Получение заголовока окна завершения заказа')
    def get_order_finish_id_title(self):
        return self.get_element_text(MainPageLocators.ORDER_WINDOW_TITLE)


    @allure.step('Ожидание окна завершения заказа')
    def wait_order_finish(self):
        self.wait_correct_order_number(MainPageLocators.ORDER_NUMBER)


    @allure.step('Получение id заказа')
    def get_order_id(self):
        return self.wait_correct_order_number(MainPageLocators.ORDER_NUMBER)


    @allure.step('Закрытие окна завершения заказа')
    def close_order_window(self):
        self.click_to_element(MainPageLocators.FINISH_ORDER_CLOSE_BUTTON)
