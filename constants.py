BASE_URL = 'https://qa-scooter.praktikum-services.ru'
COURIER_LOGIN_URL = '/api/v1/courier/login'
COURIER_CREATE_URL = '/api/v1/courier'
ORDERS_URL = '/api/v1/orders'


OK_RESPONSE = '{"ok":true}'
DUPLICATE_COURIER_ERROR = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
WITHOUT_LOGIN_PASSWORD_ERROR = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
INCORRECT_LOGIN_OR_PASSWORD = '{"code":404,"message":"Учетная запись не найдена"}'
MISSING_FIELD = '{"code":400,"message":"Недостаточно данных для входа"}'
