import allure
import requests

from constants import *
from helpers import generate_random_string


@allure.title('Проверка создания курьера')
def test_unique_courier_creation():
    #Генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    #Собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    #Отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(BASE_URL + COURIER_CREATE_URL, data=payload)

    assert response.status_code == 201 and response.text == OK_RESPONSE


@allure.title('Проверяем, что нельзя создать двух одинаковых курьеров')
def test_duplicate_courier_creation():
    #Генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    #'Собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    #Отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(BASE_URL + COURIER_CREATE_URL, data=payload)
    response = requests.post(BASE_URL + COURIER_CREATE_URL, data=payload)

    assert response.status_code == 409 and response.text == DUPLICATE_COURIER_ERROR

@allure.title('Проверяем, что нельзя создать курьера без логина и пароля')
def test_without_login_password_courier_creation():

    first_name = generate_random_string(10)


    payload = {
        "firstName": first_name
    }


    response = requests.post(BASE_URL + COURIER_CREATE_URL, data=payload)

    assert response.status_code == 400 and response.text == WITHOUT_LOGIN_PASSWORD_ERROR

