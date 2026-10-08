BASE_URL = 'https://qa-scooter.praktikum-services.ru'

CREATE_COURIER_URL = f'{BASE_URL}/api/v1/courier'
LOGIN_COURIER_URL = f'{BASE_URL}/api/v1/courier/login'
CREATE_ORDER_URL = f'{BASE_URL}/api/v1/orders'

# --- Курьер ---
DUPLICATE_LOGIN = 'Этот логин уже используется. Попробуйте другой.'
MISSING_CREATE_FIELDS = 'Недостаточно данных для создания учетной записи'
MISSING_LOGIN_FIELDS = 'Недостаточно данных для входа'
WRONG_CREDENTIALS = 'Учетная запись не найдена'

# --- Заказ ---
ORDER_BODY = {
    'firstName': 'Антон',
    'lastName': 'Тестовый',
    'address': 'ул. Тестовая, 1',
    'metroStation': 4,
    'phone': '+79990000000',
    'rentTime': 3,
    'deliveryDate': '2026-10-10',
    'comment': 'Без коммента'
}

COLORS = [[], ['BLACK'], ['GREY'], ['BLACK', 'GREY']]
