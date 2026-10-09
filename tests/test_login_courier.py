import allure
import pytest

from base_api import create_courier, login_courier
from helpers import generate_courier, create_login_data
from data import MISSING_LOGIN_FIELDS, WRONG_CREDENTIALS


class TestLoginCourier:
    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверка, что курьер может авторизоваться и запрос возвращает id')
    def test_login_courier_success(self, registered_courier):
        with allure.step('Проверка регистрации курьера через фикстуру'):
            payload = registered_courier
        with allure.step('Проверка авторизации курьера с "id" в теле'):
            response = login_courier(create_login_data(payload))
            assert response.status_code == 200
            assert 'id' in response.json()

    @allure.title('Авторизация без обязательного поля')
    @allure.description('Проверка, что система вернёт ошибку, если не указать логин или пароль')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_login_courier_missing_field(self, missing_field, registered_courier):
        with allure.step(f'Проверка удаления обязательного поля: {missing_field}'):
            courier_data = create_login_data(registered_courier)
            courier_data.pop(missing_field)
        with allure.step('Проверка ошибки авторизации без обязательного поля'):
            response = login_courier(courier_data)
            assert response.status_code == 400
            assert response.json()['message'] == MISSING_LOGIN_FIELDS

    @allure.title('Авторизация с неверным логином')
    @allure.description('Проверка, что система вернёт ошибку при неправильном логине')
    def test_login_courier_wrong_login(self, registered_courier):
        with allure.step('Проверка подмены логина на несуществующий'):
            courier_data = create_login_data(registered_courier)
            courier_data['login'] += '_x'
        with allure.step('Проверка ошибки авторизации с неверным логином'):
            response = login_courier(courier_data)
            assert response.status_code == 404
            assert response.json()['message'] == WRONG_CREDENTIALS

    @allure.title('Авторизация с неверным паролем')
    @allure.description('Проверка, что система вернёт ошибку при неправильном пароле')
    def test_login_courier_wrong_password(self, registered_courier):
        with allure.step('Проверка подмены пароля на неверный'):
            courier_data = create_login_data(registered_courier)
            courier_data['password'] = courier_data['password'][::-1]
        with allure.step('Проверка ошибки авторизации с неверным паролем'):
            response = login_courier(courier_data)
            assert response.status_code == 404
            assert response.json()['message'] == WRONG_CREDENTIALS
