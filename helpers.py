import string
import random

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
