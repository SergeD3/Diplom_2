import data
import allure

from methods.base_methods import BaseMethods


class UserMethods(BaseMethods):

    @allure.title("Отправляю POST-запрос на создание пользователя")
    def post_create_user(self, req_body):
        response = self.post_method(
            url=data.BASE_URL,
            req_path=data.USER_REGISTRATION_PATH,
            req_data=req_body
        )

        return response

    @allure.title("Отправляю POST-запрос на авторизацию пользователя")
    def post_auth_user(self, req_body):
        response = self.post_method(
            url=data.BASE_URL,
            req_path=data.USER_AUTH_PATH,
            req_data=req_body
        )

        return response
