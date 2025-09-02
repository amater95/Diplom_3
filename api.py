import requests
import allure
import urls


@allure.step('Создание пользователя')
def create_user(payload):
    return requests.post(urls.CREATE_USER, json=payload)


@allure.step('Удаление пользователя')
def delete_user(token):
    return requests.delete(urls.DELETE_USER, headers={"Authorization": token})
