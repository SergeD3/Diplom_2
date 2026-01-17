import allure
import data

from methods.base_methods import BaseMethods


class OrderMethods(BaseMethods):

    @allure.step("Отправляю post-запрос на создание заказа")
    def post_create_order(self, token=None, req_body=None):
        payload = data.ORDER_BODY if req_body is None else req_body

        create_response = self.post_method(
            url=data.BASE_URL,
            req_path=data.ORDERS_PATH,
            token=token,
            req_data=payload
        )

        return create_response

    @allure.step("Отправляю get-запрос на получение списка заказов пользователя")
    def get_orders_by_user(self, token=None):
        order_response = self.get_method(
            url=data.BASE_URL,
            req_path=data.ORDERS_PATH,
            token=token
        )

        return order_response
