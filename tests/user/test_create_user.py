from methods.user_methods import UserMethods
from helpers import helpers

import pytest
import allure


class TestUser(UserMethods):

    @allure.title("Проверка создания уникального пользователя")
    def test_create_unique_user(self, create_unique_user):
        empty_string = ""
        response = create_unique_user[0]

        assert response.ok and response.json()['accessToken'] != empty_string

    @allure.title("Проверка, что нельзя зарегистрировать двух одинаковых пользователей")
    def test_cannot_create_registered_user(self):
        expected_message = "User already exists"
        user_credentials = helpers.get_random_user_credentials()

        self.post_auth_user(user_credentials)
        response = self.post_auth_user(user_credentials)

        assert response.status_code == 403 and response.json()['message'] == expected_message

    @allure.title("Проверка, что нельзя создать пользователя с пустым обязательным полем")
    @pytest.mark.parametrize('field', [
        {"email": ""},
        {"password": ""},
        {"name": ""},
    ])
    def test_cannot_create_user_without_required_fields(self, field):
        expected_message = "Email, password and name are required fields"
        user_credentials = helpers.get_random_user_credentials()
        user_credentials.update(field)

        response = self.post_auth_user(user_credentials)

        assert response.status_code == 403 and response.json()['message'] == expected_message


