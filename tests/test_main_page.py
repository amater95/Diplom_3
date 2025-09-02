import data
import allure


@allure.suite('Проверка основного функционала')
class TestsMainPage:
    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Нажаем на ингредиент, проверяем, что появилось окно с деталями')
    def test_open_ingredient_details_window(self, main_page):
        main_page.click_on_ingredient(data.INGREDIENT_iD)
        assert main_page.get_ingredient_details_title() == data.INGREDIENT_DETAILS_TITLE


    @allure.title('Всплывающее окно закрывается кликом по крестику')
    @allure.description('Нажаем на ингредиент, проверяем, что появилось окно с деталями, нажимаем на крестик, проверяем, что окно закрылось')
    def test_close_ingredient_details_window(self, main_page):
        main_page.click_on_ingredient(data.INGREDIENT_iD)
        main_page.wait_ingredient_details_window()
        main_page.close_ingredient_details_window()
        assert main_page.wait_ingredient_details_window_is_closed()


    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @allure.description('Перетаскиваем ингредиент в конструктор, проверяем, что значение каунтера увеличилось')
    def test_increase_ingredient_counter(self, main_page):
        counter = main_page.get_ingredient_counter_value(data.INGREDIENT_iD)
        assert counter == 0
        main_page.add_ingredients_to_order(data.INGREDIENT_iD)
        counter = main_page.get_ingredient_counter_value(data.INGREDIENT_iD)
        assert counter == 2


    @allure.title('Залогиненный пользователь может оформить заказ')
    @allure.description('Нажимаем на ЛК -> авторизация -> добавляем ингредиенты -> нажимаем [Оформить заказ] -> проверяем, что появилось окно с номером заказа')
    def test_make_order(self, main_page, account_page, user_data):
        main_page.move_to_account()
        account_page.wait_login_form()
        account_page.autorisation(user_data['email'], user_data['password'])
        main_page.wait_page_visible()
        main_page.add_ingredients_to_order(data.INGREDIENT_iD)
        main_page.click_order_button()
        assert main_page.get_order_finish_id_title() == data.ORDER_FINISH_TITLE
