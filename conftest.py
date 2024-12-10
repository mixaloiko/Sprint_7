import pytest

from helpers import generate_random_string, register_new_courier_and_return_login_password


@pytest.fixture()
def random_courier_data():
    # Генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # Собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload


@pytest.fixture()
def courier_data():
    courier_data = register_new_courier_and_return_login_password()

    return courier_data
