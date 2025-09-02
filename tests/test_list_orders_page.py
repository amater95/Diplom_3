import data
import allure


@allure.suite('Раздел «Лента заказов»')
class TestsListOrdersPage:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('Нажимаем на ЛК -> авторизация -> оформление заказа -> переход в ленту заказов -> клик на первый заказ в списке')
    def test_open_order_info(self, main_page, account_page, list_orders_page, user_data):
        main_page.move_to_account()
        account_page.wait_login_form()
        account_page.autorisation(user_data['email'], user_data['password'])
        main_page.wait_page_visible()
        main_page.add_ingredients_to_order(data.INGREDIENT_iD)
        main_page.click_order_button()
        main_page.get_order_id()
        main_page.close_order_window()
        main_page.move_to_list_orders()
        list_orders_page.wait_list_orders()
        list_orders_page.click_on_first_order()
        assert list_orders_page.wait_details_window().is_displayed()


    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Нажимаем на ЛК -> авторизация -> оформление заказа -> переход в ленту заказов -> проверка, что заказ из истории заказов отображается в ленте заказов')
    def test_orders_from_history_exist_in_list(self, main_page, account_page, list_orders_page, user_data):
        main_page.move_to_account()
        account_page.wait_login_form()
        account_page.autorisation(user_data['email'], user_data['password'])
        main_page.wait_page_visible()
        main_page.add_ingredients_to_order(data.INGREDIENT_iD)
        main_page.click_order_button()
        main_page.wait_order_finish()
        main_page.close_order_window()
        main_page.move_to_account()
        account_page.wait_page_ready()
        account_page.go_to_orders_history()
        history_order_id = account_page.get_order_id()
        main_page.move_to_list_orders()
        list_orders_page.wait_list_orders()
        assert list_orders_page.find_order_by_id(history_order_id) is not None


    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('Нажимаем на ЛК -> авторизация -> оформление заказа -> проверяем, что значение счётчика за все время увеличилось')
    def test_increase_all_time_order_counter(self, main_page, account_page, list_orders_page, user_data):
        main_page.move_to_account()
        account_page.wait_login_form()
        account_page.autorisation(user_data['email'], user_data['password'])
        main_page.wait_page_visible()
        main_page.move_to_list_orders()
        list_orders_page.wait_list_orders()
        value_before_order = list_orders_page.get_all_time_counter()
        main_page.move_to_constructor()
        main_page.wait_page_visible()
        main_page.add_ingredients_to_order(data.INGREDIENT_iD)
        main_page.click_order_button()
        main_page.wait_order_finish()
        main_page.close_order_window()
        main_page.move_to_list_orders()
        list_orders_page.wait_list_orders()
        value_after_order = list_orders_page.get_all_time_counter()
        assert value_after_order > value_before_order


    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('Нажимаем на ЛК -> авторизация -> оформление заказа -> проверяем, что значение счётчика за день увеличилось')
    def test_increase_today_time_order_counter(self, main_page, account_page, list_orders_page, user_data):
        main_page.move_to_account()
        account_page.wait_login_form()
        account_page.autorisation(user_data['email'], user_data['password'])
        main_page.wait_page_visible()
        main_page.move_to_list_orders()
        list_orders_page.wait_list_orders()
        value_before_order = list_orders_page.get_today_counter()
        main_page.move_to_constructor()
        main_page.wait_page_visible()
        main_page.add_ingredients_to_order(data.INGREDIENT_iD)
        main_page.click_order_button()
        main_page.wait_order_finish()
        main_page.close_order_window()
        main_page.move_to_list_orders()
        list_orders_page.wait_list_orders()
        value_after_order = list_orders_page.get_today_counter()
        assert value_after_order > value_before_order
    

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    @allure.description('Нажимаем на ЛК -> авторизация -> оформление заказа -> нажимаем на [Лента заказов] -> проверяем список "В работе"')
    def test_order_is_in_work_list(self, main_page, account_page, list_orders_page, user_data):
        main_page.move_to_account()
        account_page.wait_login_form()
        account_page.autorisation(user_data['email'], user_data['password'])
        main_page.wait_page_visible()
        main_page.add_ingredients_to_order(data.INGREDIENT_iD)
        main_page.click_order_button()
        order_id = main_page.get_order_id()
        main_page.wait_order_finish()
        main_page.close_order_window()
        main_page.move_to_list_orders()
        list_orders_page.wait_list_orders()
        id_text = list_orders_page.find_order_id_in_work_list(order_id)
        assert order_id in id_text
