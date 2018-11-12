# -*- coding: utf-8 -*-
import codecs
import json

test_dict = {
		'name': '智能解答',
		'data': [43938, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
	}

print(test_dict)
print(type(test_dict))
#dumps 将数据转换成字符串
json_str = json.dumps(test_dict,ensure_ascii=False)
print(json_str)
print(type(json_str))

with open("record.json","w",encoding='utf-8') as f:
    json.dump(json_str,f,ensure_ascii=False)
    print("Success!")