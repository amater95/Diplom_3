import string
import random
import api

from faker import Faker


def generate_user_data(empty_field=None):
    faker=Faker()
    user_data = {
        "email": generate_random_string(10)+"@yandex.ru",
        "password": faker.password(),
        "name": faker.name()
    }
    if empty_field is not None:
        user_data[empty_field] = ""
    return user_data


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def create_user(user_data):
    response = api.create_user(user_data)
    response_payload = response.json()
    user_data['accessToken'] = response_payload['accessToken']


def delete_user(user_data):
    api.delete_user(user_data['accessToken'])
