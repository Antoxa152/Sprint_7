import allure
import pytest

from base_api import create_order
from helpers import generate_order_body
from data import COLORS


class TestCreateOrder:
    @allure.title('Создание заказа с разными вариантами цвета')
    @allure.description('Можно указать BLACK, GREY, оба или ни одного; в ответе есть track')
    @pytest.mark.parametrize('color', COLORS)
    def test_create_order_with_colors(self, color):
        with allure.step(f'Проверка создания заказа с цветами: {color}'):
            body = generate_order_body(color)
            response = create_order(body)
            assert response.status_code == 201
            assert 'track' in response.json()
