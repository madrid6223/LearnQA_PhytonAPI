import pytest
import requests

class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in response1.cookies, "Не вірний auth cookie"
        assert "x-csrf-token" in response1.headers, "Не вірний CSRF"
        assert "user_id" in response1.json(), "Не вірний user_id"

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_from_auth_method = response1.json()["user_id"]

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token":token},
            cookies={"auth_sid":auth_sid}
        )

        assert "user_id" in response2.json(), "Не вірний user_di у response2"
        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_auth_method == user_id_from_check_method, "User_id не співпадають"

    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        def test_auth_user(self):
            data = {
                'email': 'vinkotov@example.com',
                'password': '1234'
            }

            response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

            assert "auth_sid" in response1.cookies, "Не вірний auth cookie"
            assert "x-csrf-token" in response1.headers, "Не вірний CSRF"
            assert "user_id" in response1.json(), "Не вірний user_id"

            auth_sid = response1.cookies.get("auth_sid")
            token = response1.headers.get("x-csrf-token")
            #user_id_from_auth_method = response1.json()["user_id"]

            if condition == "no_cookie":
                response2 = requests.get(
                    "https://playground.learnqa.ru/api/user/auth",
                    headers={"x-csrf-token":token}
                )

            else:
                response2 = requests.get(
                    "https://playground.learnqa.ru/api/user/auth",
                    headers={"auth_sid": auth_sid}
                )

            assert "user_id" in response1.json(), "user_id немає у response1"

            user_id_from_check_method = response2.json()["user_id"]

            assert user_id_from_check_method==0, f"user_id авторизовано з перемінно {condition}"

