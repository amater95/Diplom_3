import allure
import data

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from seletools.actions import drag_and_drop
#seletools помогла решить проблему с ошибками при перетаскивании элемента в Firefox


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Поиск элемента')
    def find_element(self, locator):
        WebDriverWait(self.driver, data.WAITING_TIME, poll_frequency=0.2).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    @allure.step('Ожидание отображения элемента')
    def wait_element_visible(self, locator):
        WebDriverWait(self.driver, data.WAITING_TIME).until(expected_conditions.visibility_of_element_located(locator))
        return self.find_element(locator)


    @allure.step('Нажатие на элемент')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, data.WAITING_TIME).until(expected_conditions.element_to_be_clickable(locator))
        button = self.find_element(locator)
        try:
            self.find_element(locator).click()
        except:
            self.driver.execute_script("arguments[0].click();", button)
    #еще одна фишка которая помогла решить проблему с ошибками в Firefox 


    @allure.step('Ввод текста')
    def write_text_to_element(self, locator, text):
        self.find_element(locator).send_keys(text)


    @allure.step('Получение текста')
    def get_element_text(self, locator):
        return self.find_element(locator).text


    @allure.step('Перемещение элемента с помощью drag and drop')
    def move_element(self, locator_element1, locator_element2):
        element_from = self.wait_element_visible(locator_element1)
        element_to = self.wait_element_visible(locator_element2)
        drag_and_drop(self.driver, element_from, element_to)


    @allure.step('Проверка неотображения элемента')
    def check_invisibility(self, locator) -> object:
        return WebDriverWait(self.driver, data.WAITING_TIME).until(expected_conditions.invisibility_of_element(locator))
    

    @allure.step('Получение атрибута элемента')
    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)


    @staticmethod
    def format_locator(locator, value):
        return locator[0], locator[1].format(value)
    

    def wait_correct_order_number(self, locator):
        def _order_number_changed(driver):
            try:
                text = driver.find_element(*locator).text.strip()
                return text != "9999" and text != ""
            except NoSuchElementException:
                return False
        WebDriverWait(self.driver, data.WAITING_TIME, poll_frequency=0.2).until(_order_number_changed)
        return self.driver.find_element(*locator).text.strip()
    