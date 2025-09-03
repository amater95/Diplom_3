import allure

from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators



class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Получение заголовка формы авторизации')
    def get_login_form_text(self):
        return self.get_element_text(AccountPageLocators.LOGIN_FORM_TITLE)


    @allure.step('Ожидание отображения формы авторизации')
    def wait_login_form(self):
        self.find_element(AccountPageLocators.LOGIN_FORM_TITLE)


    @allure.step('Авторизация пользователя')
    def autorisation(self, email, password):
        self.write_text_to_element(AccountPageLocators.LOGIN_FORM_EMAIL_INPUT, email)
        self.write_text_to_element(AccountPageLocators.LOGIN_FORM_PASSWORD_INPUT, password)
        self.click_to_element(AccountPageLocators.LOGIN_BUTTON)


    @allure.step('Ожидание загрузки страницы')
    def wait_page_ready(self):
        self.find_element(AccountPageLocators.ORDER_HISTORY_BUTTON)


    @allure.step('Нажатие на [История заказов]')
    def go_to_orders_history(self):
        self.click_to_element(AccountPageLocators.ORDER_HISTORY_BUTTON)


    @allure.step('Получение активного раздела')
    def get_active_text(self):
        return self.get_element_text(AccountPageLocators.ACTIVE_ITEM)


    @allure.step('Ожидание перехода на "История заказов"')
    def wait_history_transition(self):
        return self.find_element(AccountPageLocators.ACTIVE_ITEM_HISTORY)


    @allure.step('Получение номера заказа')
    def get_order_id(self):
        text = self.get_element_text(AccountPageLocators.FIRST_ORDER_ID)
        return text


    @allure.step('Нажатие на [Выход]')
    def logout(self):
        self.click_to_element(AccountPageLocators.LOGOUT_BUTTON)


    @allure.step('Нажатие на [Восстановить пароль]')
    def click_to_pass_recover(self):
        self.click_to_element(AccountPageLocators.PASSWORD_RECOVERY_LINK)
