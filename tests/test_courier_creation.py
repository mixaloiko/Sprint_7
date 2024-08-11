import requests

from constants import *
from helpers import generate_random_string


def test_unique_courier_creation():
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(BASE_URL + COURIER_CREATE_URL, data=payload)

    assert response.status_code == 201 and response.text == OK_RESPONSE


def test_duplicate_courier_creation():
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(BASE_URL + COURIER_CREATE_URL, data=payload)
    response = requests.post(BASE_URL + COURIER_CREATE_URL, data=payload)

    assert response.status_code == 409 and response.text == DUPLICATE_COURIER_ERROR

def test_without_login_password_courier_creation():
    # генерируем логин, пароль и имя курьера
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(BASE_URL + COURIER_CREATE_URL, data=payload)

    assert response.status_code == 400 and response.text == WITHOUT_LOGIN_PASSWORD_ERROR

