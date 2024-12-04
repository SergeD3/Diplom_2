import allure

from methods.order_methods import OrderMethods


class TestGetOrderByUser(OrderMethods):

    @allure.title("Проверка возможности получения списка заказов пользователя по его токену")
    def test_get_orders_by_user_token(self, create_user_and_auth):
        expected_result = True
        token = create_user_and_auth[0].json()['accessToken']

        self.post_create_order(token)
        response = self.get_orders_by_user(token)

        assert response.ok and response.json().get('success') == expected_result

    @allure.title("Проверка, что нельзя получить список заказов без токена пользователя")
    def test_cannot_get_orders_without_user_token(self):
        expected_message = "You should be authorised"

        response = self.get_orders_by_user()

        assert response.status_code == 401 and response.json().get('message') == expected_message
