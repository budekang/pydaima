# -*- coding: utf-8 -*-
import codecs
import json
import random
from random import choice
a =range(-100,100)

x1=choice(a)
x2=choice(a)
x3=choice(a)
x4=choice(a)
x5=choice(a)
x6=choice(a)

test_dict = {
		'name': '智能解答',
		'data': [43934+x1, 52503+x2, 57177+x3]
	}
test_dict2 = {
		'name': '涉及政策',
		'data': [26565+x4, 24851+x5, 46182+x6]
	}
#print(test_dict)
#print(type(test_dict))
json_str = json.dumps(test_dict,ensure_ascii=False)
#print(json_str)
#print(type(json_str))
json_str2 = json.dumps(test_dict2,ensure_ascii=False)
#print(json_str2)
with open("fuwushuju.txt","w",encoding='utf-8') as f:
    print(json_str+","+json_str2)
    f.write(json_str+","+json_str2)
    print("Success!")
##############################################
b = range(0,50)
y1=choice(b)
y2=choice(b)
y3=choice(b)
y4=choice(b)
y5=choice(b)
y6=choice(b)
y7=choice(b)
y8=choice(b)
y9=choice(b)
y10=choice(b)
fazhan_qk = {
		'name': '融资总数',
		'data': [1005+y1, 1436+y2, 2063+y3, 3057+y4, 4618+y5]
	}
fazhan_qk2 = {
		'name': '新增企业',
		'data': [1005+y6, 1436+y7, 2063+y8, 3057+y9, 4618+y10]
	}
json_qk = json.dumps(fazhan_qk,ensure_ascii=False)
json_qk2 = json.dumps(fazhan_qk2,ensure_ascii=False)
with open("fazhan_qk.txt","w",encoding='utf-8') as f:
    print(json_qk+","+json_qk2)
    f.write(json_qk+","+json_qk2)
    print("Success!")
#################################################
c = range(1,8)
z1=choice(c)
z2=choice(c)
z3=choice(c)
z4=choice(c)
z5=choice(c)
mianji = {
		'type': 'area',
		'name': '面积',
		'data': [z1,z2, z3,z4, z5]}
json_mianji = json.dumps(mianji,ensure_ascii=False)
with open("mianji.txt","w",encoding='utf-8') as f:
    print(json_mianji)
    f.write(json_mianji)
    print("Success!")