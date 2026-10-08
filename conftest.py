import allure
import pytest

from base_api import create_courier, login_courier, delete_courier
from helpers import generate_courier


@allure.step('Удаляем курьера по логину и паролю')
def delete_courier_by_credentials(payload):
    response = login_courier({'login': payload['login'], 'password': payload['password']})
    if response.status_code == 200:
        delete_courier(response.json()['id'])


@pytest.fixture()
def courier_payload_with_delete():
    payload = generate_courier()
    yield payload
    delete_courier_by_credentials(payload)


@pytest.fixture()
def registered_courier():
    payload = generate_courier()
    response = create_courier(payload)
    assert response.status_code == 201, f'Курьер не создался: {response.status_code}, {response.text}'
    yield payload
    delete_courier_by_credentials(payload)
