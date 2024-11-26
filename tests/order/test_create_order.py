from methods.order_methods import OrderMethods


class TestCreateOrder(OrderMethods):

    def test_create_order_with_authorization(self, create_user_and_auth):
        empty_string = ""
        token = create_user_and_auth[0].json()['accessToken']

        create_response = self.post_create_order(token)
        print(f"{create_response.status_code=}")

        assert create_response.ok and create_response.json()['name'] != empty_string
