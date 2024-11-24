from methods.user_methods import UserMethods


class TestAuthorization(UserMethods):

    def test_authorization_real_user(self, create_user_and_auth):
        empty_string = ""
        response = create_user_and_auth

        assert response.ok and response.json()['accessToken'] != empty_string

    def test_authorization_wrong_credentials(self, create_user_and_auth):
        pass
        # user_credentials: dict = create_user_and_auth[2]
        # user_credentials.get('email') = ''
        # auth_response = self.post_auth_user(user_credentials)
