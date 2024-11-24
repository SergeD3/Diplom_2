
COMMON_HEADERS = {'Content-Type': 'application/json'}
BASE_URL = "https://stellarburgers.nomoreparties.site/api/"

USER_REGISTRATION_PATH = "auth/register"
USER_AUTH_PATH = "auth/login"
USER_EDIT_PATH = "auth/user"
ORDERS_PATH = "orders"

ORDER_BODY = {
    "ingredients": []
}

USER_BODY = {
    "email": "{email}",
    "password": "{password}",
    "name": "{username}"
}

