import data
import allure

from methods.order_methods import OrderMethods


class TestCreateOrder(OrderMethods):

    @allure.title("Проверка возможности создания заказа с токеном пользователя и ингредиентами")
    def test_create_order_with_authorization_and_ingredients(self, create_user_and_auth):
        empty_string = ""
        token = create_user_and_auth[0].json()['accessToken']

        create_response = self.post_create_order(token)

        assert create_response.ok and create_response.json().get('name') != empty_string

    # Пояснение к тесту ниже: тест будет всегда падать из-за бага на сайте stellarburgers.
    # Подгонять тест под фактический результат и соответственно баг - кажется мне плохой идеей.
    # Поэтому, тест написан на основе требований из документации и отражает ожидаемый результат в
    # соответствии с оной.
    @allure.title("Проверка, что нельзя создать заказ без токена авторизации пользователя")
    def test_cannot_create_order_without_authorization(self):
        expected_message = "You should be authorised"
        create_response = self.post_create_order()

        assert create_response.status_code == 401 and create_response.json().get('message') == expected_message

    @allure.title("Проверка, что нельзя создать заказ без ингредиентов")
    def test_cannot_create_order_without_ingredients(self):
        expected_message = "Ingredient ids must be provided"
        payload = data.ORDER_BODY
        payload['ingredients'] = []

        create_response = self.post_create_order(req_body=payload)

        assert create_response.status_code == 400 and create_response.json().get('message') == expected_message

    @allure.title("Проверка, что нельзя создать заказ с невалидными ингредиентами")
    def test_cannot_create_order_with_invalid_hash_ingredients(self):
        payload = data.ORDER_BODY
        payload['ingredients'] = ['invalid_ingredient-1', 'invalid_ingredient-2']

        create_response = self.post_create_order(req_body=payload)

        assert create_response.status_code == 500
