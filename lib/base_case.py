import json.decoder

from requests import Response

class BaseCase:
    def get_cookie(self,response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Не можна знайти кукі з іменем {cookie_name} в останньому запиті"
        return response.cookies[cookie_name]

    def get_header (self, response: Response, header_name):
        assert header_name in response.headers, f"Не можна знайти header з іменем {header_name_name} в останньому запиті"
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Відповідь не є формату JSON. Відповідь текст: '{response.text}'"

        assert name in response_as_dict, f"Відповідь JSON не має ключа '{name}'"

        return response_as_dict[name]


