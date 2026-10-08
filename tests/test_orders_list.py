import allure

from base_api import get_orders_list


class TestOrdersList:
    @allure.title('Получение списка заказов')
    @allure.description('Проверка, что в теле ответа возвращается список заказов')
    def test_orders_list_success(self):
        with allure.step('Проверка получения списка заказов'):
            response = get_orders_list()
            assert response.status_code == 200
            assert 'orders' in response.json()
            assert isinstance(response.json()['orders'], list)
