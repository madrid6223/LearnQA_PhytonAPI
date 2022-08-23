import pytest # for @pytest.mark.parametrize
import requests

class TestFirstApi:
    names = [
        ("Vovo"),
        ("Marynka"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url="https://playground.learnqa.ru/api/hello"
        #name = 'Vovo'
        data = {'name':name}

        response = requests.get(url, params=data)

        assert response.status_code ==200, "Ошибка кода ответа"

        response_dict=response.json()
        assert "answer" in response_dict, "Поля 'answer' нет а response"

        if len(name) ==0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text=f"Hello, {name}"

        actual_response_text=response_dict["answer"]
        assert actual_response_text==expected_response_text, "Сравнение не прошло"