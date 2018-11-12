# -*- coding: utf-8 -*-
import codecs
import json
import random
from random import choice
from flask import Flask,jsonify,request
import time
import os



def main():
    for i in range(1, 10000):
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

        #print('到这没' + str(i))
        i += 1

        print(data)

        app = Flask(__name__)  # 创建一个服务，赋值给APP

        @app.route('/get_user', methods=['get'])  # 指定接口访问的路径，支持什么请求方式get，post
        # 讲的是封装成一种静态的接口，无任何参数传入
        def get_user():  # -----这里的函数名称可以任意取
            return (data)  # 把字典转成json串返回

        def killport(port):
            command = '''kill -9 $(netstat -nlp | grep :''' + str(
                port) + ''' | awk '{print $7}' | awk -F"/" '{ print $1 }')'''
            os.system(command)

        app.run(host='0.0.0.0', port=8803, debug=True)
        time.sleep(10)
        killport(8803)
        # http://192.168.18.88:8803/get_user
        # http://127.0.0.1/get_user

        time.sleep(10)




if __name__=='__main__':

    main()







