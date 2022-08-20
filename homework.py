#import json

#json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
#obj = json.loads(json_text)

#key = "messages"
#if key in obj:
#    print(obj[key])
#else:
#    print(f"Ключа {key} в JSON немає")

import json

json_text = {"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}
print(type(json_text))
parsed_json_text = json.loads(json_text)
#print(parsed_json_text)



