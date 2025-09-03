import allure

from pages.base_page import BasePage
from locators.list_orders_page_locators import ListOrdersPageLocators


class ListOrdersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Получение заголовка страницы')
    def get_title_text(self):
        return self.get_element_text(ListOrdersPageLocators.LIST_ORDERS_TITLE)


    @allure.step('Ожидание загрузки страницы')
    def wait_list_orders(self):
        return self.find_element(ListOrdersPageLocators.LIST_ORDERS_TITLE)


    @allure.step('Нажатие на карточку первого заказа')
    def click_on_first_order(self):
        return self.click_to_element(ListOrdersPageLocators.FIRST_ORDER_CARD)


    @allure.step('Ожидание отображения окна заказа')
    def wait_details_window(self):
        return self.find_element(ListOrdersPageLocators.ORDER_DETAILS_WINDOW)


    @allure.step('Получение числа заказов за сегодня')
    def get_today_counter(self):
        return int(self.get_element_text(ListOrdersPageLocators.ORDER_COUNTER_TODAY))


    @allure.step('Получение числа заказов за всё время')
    def get_all_time_counter(self):
        return int(self.get_element_text(ListOrdersPageLocators.ORDER_COUNTER_ALL_TIME))


    @allure.step('Поиск заказа по id')
    def find_order_by_id(self, order_id):
        locator = self.format_locator(ListOrdersPageLocators.ORDER_ID_ELEMENT, order_id)
        return self.get_element_text(locator)


    @allure.step('Поиск заказа по id в списке "В работе"')
    def find_order_id_in_work_list(self, order_id):
        locator = self.format_locator(ListOrdersPageLocators.ORDER_ID_IN_WORK, order_id)
        return self.find_element(locator).text
    