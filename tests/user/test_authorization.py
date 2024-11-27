import pytest
import allure

from methods.user_methods import UserMethods


class TestAuthorization(UserMethods):

    @allure.title('Проверка возможности аутентификации под существующим пользователем')
    def test_authorization_real_user(self, create_user_and_auth):
        empty_string = ""
        response = create_user_and_auth[0]

        assert response.ok and response.json()['accessToken'] != empty_string

    @allure.title('Проверка, что нельзя пройти аутентификацию с невалидными учётными данными')
    @pytest.mark.parametrize("key, value", [
        ['email', 'wrong_email'],
        ['password', 'wrong_password'],
    ])
    def test_authorization_invalid_credentials(self, create_user_and_auth, key, value):
        expected_message = "email or password are incorrect"
        user_credentials = create_user_and_auth[1]
        user_credentials[key] = value

        auth_response = self.post_auth_user(user_credentials)

        assert auth_response.status_code == 401 and auth_response.json()['message'] == expected_message
