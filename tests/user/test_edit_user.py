import pytest
import allure

from methods.user_methods import UserMethods
from helpers import helpers


class TestEditUser(UserMethods):

    @allure.title('Проверка возможности изменять учётные данные пользователя с авторизацией')
    @pytest.mark.parametrize("key, value", [
        ['name', helpers.generate_random_string(10)],
        ['email', helpers.get_random_email()]
    ])
    def test_edit_user_name_email_with_auth(self, create_user_and_auth, key, value):
        token = create_user_and_auth[0].json()['accessToken']

        expected_key, expected_value = str(key), value
        user_creds = create_user_and_auth[1]
        user_creds[expected_key] = expected_value

        response = self.edit_user_info(token=token, req_body=user_creds)

        assert response.ok and response.json()['user'][expected_key] == expected_value

    @allure.title('Проверка возможности сменить пароль пользователю с авторизацией')
    def test_edit_user_password_with_auth(self, create_user_and_auth):
        empty_string = ''
        token = create_user_and_auth[0].json()['accessToken']
        user_creds = create_user_and_auth[1]
        new_password = helpers.generate_random_string(10)
        user_creds['password'] = new_password

        edit_response = self.edit_user_info(token=token, req_body=user_creds)

        assert edit_response.ok

        auth_response = self.post_auth_user(user_creds)

        assert auth_response.ok and auth_response.json()['accessToken'] != empty_string

    @allure.title('Проверка невозможности изменить учётные данные пользователя без авторизации')
    @pytest.mark.parametrize("key, value", [
        ['name', helpers.generate_random_string(10)],
        ['email', helpers.get_random_email()],
        ['password', helpers.generate_random_string(10)],
    ])
    def test_edit_user_without_auth(self, create_user_and_auth, key, value):
        token = None
        expected_message = "You should be authorised"

        creds_key, creds_value = str(key), value
        user_creds = create_user_and_auth[1]
        user_creds[creds_key] = creds_value

        edit_response = self.edit_user_info(token=token, req_body=user_creds)

        assert edit_response.status_code == 401 and edit_response.json()['message'] == expected_message
