import allure
import requests

from constants import *
from conftest import *
from helpers import generate_random_string


class TestCourierCreation:
    @allure.title('Проверка создания курьера')
    def test_unique_courier_creation(self, random_courier_data):
        response = requests.post(BASE_URL + COURIER_CREATE_URL, data=random_courier_data)

        assert response.status_code == 201 and response.text == OK_RESPONSE


    @allure.title('Проверяем, что нельзя создать двух одинаковых курьеров')
    def test_duplicate_courier_creation(self, random_courier_data):
        response = requests.post(BASE_URL + COURIER_CREATE_URL, data=random_courier_data)
        response = requests.post(BASE_URL + COURIER_CREATE_URL, data=random_courier_data)

        assert response.status_code == 409 and response.text == DUPLICATE_COURIER_ERROR

    @allure.title('Проверяем, что нельзя создать курьера без логина и пароля')
    def test_without_login_password_courier_creation(self):
        first_name = generate_random_string(10)

        payload = {
            "firstName": first_name
        }

        response = requests.post(BASE_URL + COURIER_CREATE_URL, data=payload)

        assert response.status_code == 400 and response.text == WITHOUT_LOGIN_PASSWORD_ERROR

