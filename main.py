from json.decoder import JSONDecodeError
import requests

# response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "Userok2"})
# parsed_response_text = response.json()
# print(parsed_response_text["answer"])

##response = requests.get("https://playground.learnqa.ru/api/get_text")
##print(response.text)
##
##try:
##    parsed_response_text = response.json()
##    print(parsed_response_text)
##except JSONDecodeError:
##    print("Response is not JSON format")

#import requests
#response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
#first_response = response.history[0]
#second_response = response
#
#print(first_response.url)
#print(second_response.url)


#import requests
#
#headers = {"some_header":"1234"}
#response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
#
#print(response.text)
#print(response.headers)

import requests

payload = {"login":"secret_login", "password":"secret_pass2"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookie_value = response1.cookies.get('auth_cookie')

my_cookies = {'auth_cookie':cookie_value}
#my_cookies = {}
#    if cookie_value is not None:
#    my_cookies.update({'auth_cookie': cookie_value})

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies = my_cookies)

print(response2.text)
