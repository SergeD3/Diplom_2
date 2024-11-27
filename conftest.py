import json
import pytest
import requests as req
import data

from helpers import helpers as hp


@pytest.fixture
def create_unique_user():
    creds = hp.get_random_user_credentials()
    creds_json = json.dumps(creds)
    response = req.post(
        url=f"{data.BASE_URL}{data.USER_REGISTRATION_PATH}",
        headers=data.COMMON_HEADERS,
        data=creds_json
    )

    assert response.ok, f"Ошибка: {response.status_code} : {response.text}"

    return response, creds


@pytest.fixture
def create_user_and_auth(create_unique_user):
    created_user_creds = json.dumps(create_unique_user[1])

    auth_user_response = req.post(
        url=f"{data.BASE_URL}{data.USER_AUTH_PATH}",
        headers=data.COMMON_HEADERS,
        data=created_user_creds
    )

    assert auth_user_response.ok, f"Ошибка: {auth_user_response.status_code} : {auth_user_response.text}"

    yield auth_user_response, json.loads(created_user_creds)

    access_token = auth_user_response.json()['accessToken']
    headers = data.COMMON_HEADERS
    headers['Authorization'] = access_token

    delete_user_response = req.delete(
        url=f"{data.BASE_URL}{data.USER_EDIT_PATH}",
        headers=headers,
        data=created_user_creds
    )

    assert delete_user_response.ok, f"Ошибка удаления пользователя: {auth_user_response.status_code} : {auth_user_response.text}"
