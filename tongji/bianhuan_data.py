# -*- coding: utf-8 -*-
import codecs
import json
import random
from random import choice
from flask import Flask,jsonify,request
import time
import os
import threading


def data():
    for i in range(1, 99999999):
        if i >= 0:
            print('第' + str(i) + '次变换数据')

        a = range(-100, 100)

        x1 = choice(a)
        x2 = choice(a)
        x3 = choice(a)
        x4 = choice(a)
        x5 = choice(a)
        x6 = choice(a)

        test_dict = {
            'name': '智能解答',
            'data': [43934 + x1, 52503 + x2, 57177 + x3]
        }
        test_dict2 = {
            'name': '涉及政策',
            'data': [26565 + x4, 24851 + x5, 46182 + x6]
        }
        # print(test_dict)
        # print(type(test_dict))
        json_str = json.dumps(test_dict, ensure_ascii=False)
        # print(json_str)
        # print(type(json_str))
        json_str2 = json.dumps(test_dict2, ensure_ascii=False)
        # print(json_str2)
        data = json_str + "," + json_str2
        # data1=json.dumps(data).encode()
        with open("fuwushuju.txt", "w", encoding='utf-8') as f:
            #print(json_str + "," + json_str2)
            f.write(json_str + "," + json_str2)
            print("Success!")
        i += 1

        print(data)
        time.sleep(10)


if __name__=='__main__':
    data()







