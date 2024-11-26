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
    def post_auth_user(self, creds):
        response = self.post_method(
            url=data.BASE_URL,
            req_path=data.USER_AUTH_PATH,
            req_data=creds
        )

        return response

    @allure.title("Отправляю GET-запрос с токеном для получения информации о пользователе")
    def get_user_info(self, token):
        response = self.get_method(
            url=data.BASE_URL,
            req_path=data.USER_AUTH_PATH,
            token=token
        )

        return response

    @allure.title("Отправляю PATCH-запрос с токеном для изменения информации в пользователе")
    def edit_user_info(self, token, req_body):
        response = self.patch_method(
            url=data.BASE_URL,
            req_path=data.USER_EDIT_PATH,
            token=token,
            req_data=req_body
        )

        return response
