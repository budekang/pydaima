# -*- coding: utf-8 -*-
import codecs
import json

test_dict = {'name': '智能解答','data': [43938, 52503, 57177, 69658, 97031, 119931, 137133, 154175]}

test_dict2 = {'name': '涉及政策','data': [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]}

print(test_dict)
print(type(test_dict))
print(test_dict2)
print(type(test_dict2))

#dumps 将数据转换成字符串
json_str = json.dumps(test_dict,ensure_ascii=False)
print(json_str)
print(type(json_str))

json_str2 = json.dumps(test_dict2,ensure_ascii=False)
print(json_str2)
print(type(json_str2))

with open("record.json","w",encoding='utf-8') as f:
    json.dump(json_str+","+json_str2,f,ensure_ascii=False)
    print("Success!")