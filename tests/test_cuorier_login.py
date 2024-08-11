import requests

from constants import *
from helpers import register_new_courier_and_return_login_password, generate_random_string


def test_login_courier():
    # создать курьера и записать результат создания в переменную courier_data
    courier_data = register_new_courier_and_return_login_password()
    # проверить, что переменная courier_data содержит два и более элемента
    if len(courier_data) == 3:
        # создать payload на логин и отправить post запрос на логин, получить ответ
        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }
        response = requests.post(BASE_URL + COURIER_LOGIN_URL, data=payload)
        assert response.status_code == 200 and 'id' in response.text
    else:
        raise Exception("Проблема при создании курьера")


def test_login_courier_incorrect_password():
    courier_data = register_new_courier_and_return_login_password()
    # проверить, что переменная courier_data содержит два и более элемента
    if len(courier_data) == 3:
        # создать payload на логин и отправить post запрос на логин, получить ответ
        payload = {
            "login": courier_data[0],
            "password": '00000'
        }
        response = requests.post(BASE_URL + COURIER_LOGIN_URL, data=payload)
        assert response.status_code == 404 and response.text == INCORRECT_LOGIN_OR_PASSWORD
    else:
        raise Exception("Проблема при создании курьера")


def test_login_courier_incorrect_login():
    # создать payload на логин и отправить post запрос на логин, получить ответ
    payload = {
        "login": generate_random_string(10),
        "password": generate_random_string(10)
    }
    response = requests.post(BASE_URL + COURIER_LOGIN_URL, data=payload)
    assert response.status_code == 404 and response.text == INCORRECT_LOGIN_OR_PASSWORD


def test_login_courier_missing_field():
    # создать payload на логин и отправить post запрос на логин, получить ответ
    payload = {
        "password": generate_random_string(10)
    }
    response = requests.post(BASE_URL + COURIER_LOGIN_URL, data=payload)
    assert response.status_code == 400 and response.text == MISSING_FIELD
