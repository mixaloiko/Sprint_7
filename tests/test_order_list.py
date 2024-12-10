import allure
import requests

from constants import *


class TestOrderList:
    @allure.title('Проверка, что можно получить список заказов')
    def test_order_list(self):
        response = requests.get(BASE_URL + ORDERS_URL)
        assert response.status_code == 200 and 'orders' in response.text
