
COMMON_HEADERS = {'Content-Type': 'application/json'}
AUTH_HEADER = {'Authorization': ''}

BASE_URL = "https://stellarburgers.nomoreparties.site/api/"

# пользователь
USER_REGISTRATION_PATH = "auth/register"
USER_AUTH_PATH = "auth/login"
USER_EDIT_PATH = "auth/user"
USER_BODY = {
    "email": "{email}",
    "password": "{password}",
    "name": "{username}"
}

# заказ
ORDERS_PATH = "orders"
ORDER_BODY = {
    "ingredients": [
        "61c0c5a71d1f82001bdaaa7a",
        "61c0c5a71d1f82001bdaaa78",
        "61c0c5a71d1f82001bdaaa77",
        "61c0c5a71d1f82001bdaaa76"
        ]
}

# ингредиенты
ING_PATH = "ingredients"
