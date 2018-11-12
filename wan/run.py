# -*- coding: utf-8 -*-
from flask import Flask,jsonify,request
def app():
    app = Flask(__name__)  # 创建一个服务，赋值给APP

    @app.route('/get_data', methods=['get'])  # 指定接口访问的路径，支持什么请求方式get，post
    # 讲的是封装成一种静态的接口，无任何参数传入
    def get_data():  # -----这里的函数名称可以任意取
        with open("fuwushuju.txt", "r", encoding='utf-8') as f:
            data=f.read()
            return (data)  # 把字典转成json串返回



    app.run(host='0.0.0.0', port=8803, debug=True)
    # http://192.168.18.88:8803/get_data
    # http://127.0.0.1/get_data

if __name__=='__main__':
    app()