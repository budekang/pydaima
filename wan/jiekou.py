# coding:utf-8
from flask import Flask,jsonify,request
data = {'huhy':{'age':24,'sex':'女'},
        'liuer':{'age':12,'sex':'男'}
        }
app = Flask(__name__)#创建一个服务，赋值给APP
@app.route('/get_user',methods=['get'])#指定接口访问的路径，支持什么请求方式get，post
#讲的是封装成一种静态的接口，无任何参数传入
def get_user():#-----这里的函数名称可以任意取
    return  jsonify(data)#把字典转成json串返回

app.run(host='0.0.0.0',port=8802,debug=True)
