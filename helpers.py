import random
import string

import requests

from base_api import create_courier


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_courier():
    return {
        'login': generate_random_string(10),
        'password': generate_random_string(10),
        'firstName': generate_random_string(10)
    }


def create_login_data(courier_payload):
    # для авторизации нужны только логин и пароль
    return {
        'login': courier_payload['login'],
        'password': courier_payload['password']
    }


def generate_order_body(color=None):
    from data import ORDER_BODY
    body = ORDER_BODY.copy()
    if color is not None:
        body['color'] = color
    return body


def register_new_courier_and_return_login_password():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {'login': login, 'password': password, 'firstName': first_name}
    response = create_courier(payload)

    if response.status_code == 201:
        return [login, password, first_name]
    return []
