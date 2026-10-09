import allure
import pytest

from base_api import create_courier
from helpers import generate_courier
from data import DUPLICATE_LOGIN, MISSING_CREATE_FIELDS


class TestCreateCourier:
    @allure.title('Создание курьера')
    @allure.description('Успешное создание возвращает 201 и тело {"ok": True}')
    def test_create_courier(self):
        with allure.step('Генерируем уникальные данные для курьера'):
            payload = generate_courier()

        with allure.step('Отправляем запрос на создание курьера'):
            response = create_courier(payload)

        with allure.step('Проверяем статус и тело ответа'):
            assert response.status_code == 201
            assert response.json() == {'ok': True}

    @allure.title('Дубликат логина курьера')
    @allure.description('Попытка создать курьера с существующим логином возвращает 409')
    def test_create_duplicate_courier(self, registered_courier):
        with allure.step('Используем данные уже существующего курьера'):
            payload = registered_courier

        with allure.step('Повторяем создание с теми же данными'):
            response = create_courier(payload)

        with allure.step('Ожидаем ошибку дубликата'):
            assert response.status_code == 409
            assert response.json()['message'] == DUPLICATE_LOGIN

    @allure.title('Отсутствие обязательного поля при создании курьера')
    @allure.description('Без логина или пароля сервер возвращает 400 и сообщение об ошибке')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_missing_field(self, missing_field):
        with allure.step('Генерируем полный набор данных'):
            payload = generate_courier()

        with allure.step(f'Убираем поле {missing_field} из запроса'):
            payload.pop(missing_field)

        with allure.step('Отправляем неполный запрос и проверяем ошибку'):
            response = create_courier(payload)
