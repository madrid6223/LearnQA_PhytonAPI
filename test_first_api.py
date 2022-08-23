import requests

class TestFirstApi:
    def test_hello_call(selfself):
        url="https://playground.learnqa.ru/api/hello"
        name = 'Vovo'
        data = {'name':name}

        response = requests.get(url)

        assert response.status_code ==200, "Ошибка кода ответа"

        response_dict=response.json()
        assert "answer" in response_dict, "Поля 'answer' нет а response"

        expected_response_text=f"Hello, {name}"
        actual_response_text=response_dict["answer"]
        assert actual_response_text==expected_response_text, "Сравнение не прошло"