import pytest
import helpers
import urls

from method_api import user_api
from selenium import webdriver
from pages.main_page import MainPage
from pages.account_page import AccountPage
from pages.pass_recover_page import PassRecoverPage
from pages.list_orders_page import ListOrdersPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.get(urls.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture
def list_orders_page(driver):
    return ListOrdersPage(driver)


@pytest.fixture
def pass_recover_page(driver):
    return PassRecoverPage(driver)


@pytest.fixture
def user_data():
    user_data = helpers.generate_user_data()
    user_api.create_user(user_data)
    yield user_data
    user_api.delete_user(user_data)
