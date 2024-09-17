import allure
import requests

from conftest import *
from constants import *
from helpers import generate_random_string


class TestCourierLogin:
    @allure.title('Проверить, что курьер может авторизоваться')
    def test_login_courier(self, courier_data):
        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }
        response = requests.post(BASE_URL + COURIER_LOGIN_URL, data=payload)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверить, что вернется сообщение об ошибке при неверном пароле')
    def test_login_courier_incorrect_password(self, courier_data):
        payload = {
            "login": courier_data[0],
            "password": '00000'
        }
        response = requests.post(BASE_URL + COURIER_LOGIN_URL, data=payload)
        assert response.status_code == 404 and response.text == INCORRECT_LOGIN_OR_PASSWORD

    @allure.title('Проверить, что вернется сообщение об ошибке при неверном логине')
    def test_login_courier_incorrect_login(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }
        response = requests.post(BASE_URL + COURIER_LOGIN_URL, data=payload)
        assert response.status_code == 404 and response.text == INCORRECT_LOGIN_OR_PASSWORD


    @allure.title('Проверить, что вернется сообщение об ошибке при незаполненном поле')
    def test_login_courier_missing_field(self):
        payload = {
            "password": generate_random_string(10)
        }
        response = requests.post(BASE_URL + COURIER_LOGIN_URL, data=payload)
        assert response.status_code == 400 and response.text == MISSING_FIELD
