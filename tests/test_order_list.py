import allure
import requests

from constants import *


@allure.title('Проверка, что можно получить список заказов')
@allure.step('Отправить запрос на получение списка заказов')
def test_order_list():
    response = requests.get(BASE_URL + ORDERS_URL)
    assert response.status_code == 200 and 'orders' in response.text
