import allure

from pages.base_page import BasePage
from locators.pass_recover_page_locators import PassRecoverPageLocators


class PassRecoverPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Получение заголовка страницы')
    def get_title_text(self):
        return self.get_element_text(PassRecoverPageLocators.PASS_RECOVER_TITLE)


    @allure.step('Ожидание отображения страницы восстановления пароля')
    def wait_page_visible(self):
        self.find_element(PassRecoverPageLocators.PASS_RECOVER_TITLE)


    @allure.step('Восстановление пароля')
    def fill_email_form(self, email):
        self.write_text_to_element(PassRecoverPageLocators.EMAIL_FIELD, email)
        self.click_to_element(PassRecoverPageLocators.PASS_RECOVER_BUTTON)


    @allure.step('Поиск поля ввода нового пароля')
    def find_new_password_field(self):
        return self.find_element(PassRecoverPageLocators.NEW_PASSWORD_FIELD)


    @allure.step('Нажатие на [показать/скрыть пароль]')
    def click_open_hide_password_button(self):
         self.click_to_element(PassRecoverPageLocators.BUTTON_PASSWORD_SHOW)


    @allure.step('Получаем атрибуты поля и проверяем, активно ли оно')
    def is_password_field_active(self):
        return 'input_status_active' in self.get_attribute(PassRecoverPageLocators.NEW_PASSWORD_DIV, 'class')
