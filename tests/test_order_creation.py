import allure
import pytest
import requests

from constants import *


@pytest.mark.parametrize(
        'color',
        [
            [],
            ['BLACK', ''],
            ['BLACK', 'GREY']
        ]
    )
@allure.title('Проверка, что при создании заказа можно выбрать один цвет, оба цвета, не выбрать ни один из цветов')
@allure.step('1. Отправить запрос с выбранным одним цветом'
             '2. Отправить запрос с двумя выбранными цветами'
             '3. Отправить запрос не выбрав ни один из цветов')
def test_create_order(color):
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": color
    }
    response = requests.post(BASE_URL + ORDERS_URL, data=payload)
    assert response.status_code == 201 and 'track' in response.text

