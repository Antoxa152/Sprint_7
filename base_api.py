import requests

from data import CREATE_COURIER_URL, LOGIN_COURIER_URL, CREATE_ORDER_URL


def create_courier(payload):
    return requests.post(CREATE_COURIER_URL, data=payload)


def login_courier(payload):
    return requests.post(LOGIN_COURIER_URL, data=payload)


def delete_courier(courier_id):
    return requests.delete(f'{CREATE_COURIER_URL}/{courier_id}')


def create_order(body):
    return requests.post(CREATE_ORDER_URL, json=body)


def get_orders_list():
    return requests.get(CREATE_ORDER_URL)
