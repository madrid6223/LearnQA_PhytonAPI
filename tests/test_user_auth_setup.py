import pytest
import requests
from lib.base_case import BaseCase

class TestUserAuth(DaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")

        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")
        #assert "user_id" in response1.json(), "Не вірний user_id"
        #self.user_id_from_auth_method = response1.json()["user_id"]

    def test_auth_user(self):

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token":self.token},
            cookies={"auth_sid":self.auth_sid}
        )

        assert "self.user_id" in response2.json(), "Не вірний user_id у response2"
        user_id_from_check_method = response2.json()["user_id"]
        print(user_id_from_check_method)

        assert self.user_id_from_auth_method == user_id_from_check_method, "User_id не співпадають"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        def test_auth_user(self):

            if condition == "no_cookie":
                response2 = requests.get(
                    "https://playground.learnqa.ru/api/user/auth",
                    headers={"x-csrf-token" : self.token}
                )

            else:
                response2 = requests.get(
                    "https://playground.learnqa.ru/api/user/auth",
                    headers={"auth_sid": self.auth_sid}
                )

            assert "user_id" in self.response1.json(), "user_id немає у response1"

            user_id_from_check_method = response2.json()["user_id"]

            assert user_id_from_check_method==0, f"user_id авторизовано з перемінно {condition}"

