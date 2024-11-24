import json
import requests
import data
import allure


class BaseMethods:

    @allure.step('Отправляю get-запрос на указанный эндпоинт')
    def get_method(self, url, req_path, parameters=None, req_data=None, req_json=None):
        body_data = json.dumps(req_data)
        body_json = json.dumps(req_json)

        response = requests.get(
            url=f"{url}{req_path}",
            headers=data.COMMON_HEADERS,
            data=body_data,
            json=body_json,
            params=parameters
        )

        return self.check_response(response)

    @allure.step('Отправляю post-запрос на указанный эндпоинт')
    def post_method(self, url, req_path, req_data=None, req_json=None):
        body_data = json.dumps(req_data)
        body_json = json.dumps(req_json)

        response = requests.post(
            url=f"{url}{req_path}",
            headers=data.COMMON_HEADERS,
            data=body_data,
            json=body_json
        )

        return self.check_response(response)

    @staticmethod
    def check_response(response):
        if response.ok:
            print("Запрос успешно обработан")
            return response
        else:
            print(f"Запрос вернул ошибку")
            return response
