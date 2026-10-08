import allure
import pytest

from base_api import create_courier
from helpers import generate_courier
from data import DUPLICATE_LOGIN, MISSING_CREATE_FIELDS


class TestCreateCourier:
    @allure.title('Создание курьера')
    @allure.description('Проверка, что курьера можно создать и возвращается код 201 и {"ok": True}')
    def test_create_courier(self, courier_payload_with_delete):
        with allure.step('Проверка создания курьера через фикстуру'):
            payload = courier_payload_with_delete
        with allure.step('Проверка регистрации курьера с "ok": True в теле'):
            response = create_courier(payload)
            assert response.status_code == 201
            assert response.json() == {'ok': True}

    @allure.title('Создание двух одинаковых курьеров')
    @allure.description('Проверка, что нельзя создать курьера с логином, который уже есть')
    def test_create_duplicate_courier(self, registered_courier):
        with allure.step('Проверка регистрации курьера через фикстуру'):
            payload = registered_courier
        with allure.step('Проверка ошибки регистрации курьера с повторяющимся логином'):
            response = create_courier(payload)
            assert response.status_code == 409
            assert response.json()['message'] == DUPLICATE_LOGIN

    @allure.title('Создание курьера без обязательного поля')
    @allure.description('Проверка, что нельзя создать курьера без логина или пароля')
    @pytest.mark.parametrize('no_field', ['login', 'password'])
    def test_create_courier_without_required_field(self, no_field):
        with allure.step('Проверка генерации данных курьера'):
            payload = generate_courier()
        with allure.step(f'Проверка удаления обязательного поля: {no_field}'):
            payload.pop(no_field)
        with allure.step('Проверка ошибки регистрации курьера без логина или пароля'):
            response = create_courier(payload)
            assert response.status_code == 400
            assert response.json()['message'] == MISSING_CREATE_FIELDS
