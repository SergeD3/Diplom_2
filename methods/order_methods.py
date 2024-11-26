import data

from methods.base_methods import BaseMethods


class OrderMethods(BaseMethods):

    def post_create_order(self, token):

        create_response = self.post_method(
            url=data.BASE_URL,
            req_path=data.ORDERS_PATH,
            token=token,
            req_data=data.ORDER_BODY
        )

        return create_response
