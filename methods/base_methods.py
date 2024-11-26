import json
import requests
import data
import allure


class BaseMethods:
    # print(f"Отправлен запрос: {url}{req_path} : {headers=} : {body_data=}")

    @allure.step('Отправляю get-запрос на указанный эндпоинт')
    def get_method(self, url, req_path, token, parameters=None, req_data=None, req_json=None):
        body_data = json.dumps(req_data)
        body_json = json.dumps(req_json)
        req_headers = self.format_authorization_header(token)

        response = requests.get(
            url=f"{url}{req_path}",
            headers=req_headers,
            data=body_data,
            json=body_json,
            params=parameters
        )

        return self.check_response(response)

    @allure.step('Отправляю post-запрос на указанный эндпоинт')
    def post_method(self, url, req_path, token=None, req_data=None, req_json=None):
        body_data = json.dumps(req_data)
        body_json = json.dumps(req_json)
        req_headers = data.COMMON_HEADERS if token is None else self.format_authorization_header(token)

        print(f"Отправлен запрос: {url}{req_path} : {req_headers=} : {body_data=}")
        response = requests.post(
            url=f"{url}{req_path}",
            headers=req_headers,
            data=body_data,
            json=body_json
        )

        return self.check_response(response)

    @allure.step('Отправляю patch-запрос на указанный эндпоинт')
    def patch_method(self, url, req_path, token, req_data=None):
        body_data = json.dumps(req_data)
        auth_header = self.format_authorization_header(token)
        headers = self.merge_headers(auth_header)

        response = requests.patch(
            url=f"{url}{req_path}",
            headers=headers,
            data=body_data
        )

        return self.check_response(response)

    @staticmethod
    def check_response(response):
        if response.ok:
            return response
        else:
            print(f"Запрос вернул ошибку")
            return response

    @staticmethod
    def format_authorization_header(value):
        req_headers = data.AUTH_HEADER
        req_headers['Authorization'] = value

        return req_headers

    @staticmethod
    def merge_headers(headers):
        new_headers = data.COMMON_HEADERS
        new_headers.update(headers)

        return new_headers
