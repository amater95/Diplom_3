import data
import allure


@allure.suite('Восстановление пароля')
class TestPassRecoverPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке [Восстановить пароль]')
    @allure.description('Нажимаем [ЛК] -> нажимаем на [Восстановить пароль]')
    def test_go_to_pass_recover(self, main_page, account_page, pass_recover_page):
        main_page.move_to_account()
        account_page.wait_login_form()
        account_page.click_to_pass_recover()
        assert pass_recover_page.get_title_text() == data.PASS_RECOVER_TITLE


    @allure.title('Ввод почты и клик по кнопке [Восстановить]')
    @allure.description('Нажимаем [ЛК] -> нажимаем на [Восстановить пароль] -> вводим почту -> нажимаем [Восстановить]')
    def test_fill_email_form(self, main_page, account_page, pass_recover_page, user_data):
        main_page.move_to_account()
        account_page.wait_login_form()
        account_page.click_to_pass_recover()
        pass_recover_page.wait_page_visible()
        pass_recover_page.fill_email_form(user_data['email'])
        assert pass_recover_page.find_new_password_field().is_displayed()


    @allure.title('Клик по кнопке [показать/скрыть пароль] делает поле активным — подсвечивает его')
    @allure.description('Нажимаем [ЛК] -> нажимаем на [Восстановить пароль] -> вводим почту -> нажимаем [Восстановить] -> нажимаем [Показать пароль]')
    def test_new_password_field_become_active(self, main_page, account_page, pass_recover_page, user_data):
        main_page.move_to_account()
        account_page.wait_login_form()
        account_page.click_to_pass_recover()
        pass_recover_page.wait_page_visible()
        pass_recover_page.fill_email_form(user_data['email'])
        assert pass_recover_page.find_new_password_field().is_displayed()
        assert pass_recover_page.is_password_field_active() is False
        pass_recover_page.click_open_hide_password_button()
        assert pass_recover_page.is_password_field_active() is True
