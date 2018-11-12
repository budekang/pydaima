
# coding: utf-8

# In[1]:


from flask import Flask, jsonify, make_response, request, render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
# import synonyms
import simcal
import collections
import re
import pymysql
pymysql.install_as_MySQLdb()


# from gevent import monkey
# from gevent.pywsgi import WSGIServer

# monkey.patch_all()



app = Flask(__name__, instance_relative_config=True)
app.config['JSON_AS_ASCII'] = False

app.config.from_pyfile('config.py')

app.config['SQLALCHEMY_DATABASE_URI'] #这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名smart
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] # 设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_BINDS'] # 申明数据库连接
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']

db = SQLAlchemy(app) # 实例化

class Sys_qa(db.Model):
#     __bind_key__ = 'db1'
    # id是主键db.Column是字段名， db.Integer是数据类型
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text(500), unique=False)

    def __repr__(self):
        return '<User %r>' % self.name
    

# 删除符号
def del_symbol(sen):
    return re.sub("[\s+\.\!\/_,$%^*(+\"\'\\\\:)]+|[+——()?《》【】“”！，。？、；：~@#￥%……&*（）]+", "", sen)


def get_sim_all(query, bind_name, probabilityNum):

#     db = SQLAlchemy(app) # 实例化
    
    # 去各种符号
    sen1 = del_symbol(query)
    
#    db_session = diff_db_session(bind_name)
    engine = db.get_engine(bind=bind_name)
    DBSession = sessionmaker(bind=engine)
    db_session = DBSession()
    
    id_questions = db_session.query(Sys_qa.id, Sys_qa.question).all()
    
    similarity = {}
    results = []
    
    for items in id_questions:
        id_num = items[0]
        sen2 = items[1]
        sen2 = del_symbol(sen2)
        # 最核心的方法,比较两个句子的相似度
        # r = synonyms.compare(sen1, sen2, seg=True)
        r = simcal.compare(sen1, sen2, seg=True)
        similarity[id_num] = r

    
    # 对结果进行排序
    vd = collections.OrderedDict(sorted(similarity.items(), key=lambda t: t[1], reverse=True))
    
    j = 1

    for k in vd:
        # question = db_session.query(Sys_qa.question).filter(Sys_qa.id == k)
        result = {
            'similarity': similarity[k],
            # 'question': question[0][0],
            'qaId': k
        }
        results.append(result)
        if j >= probabilityNum:
            break
        j += 1
    # final_results = sorted(results, key=lambda x:x['similarity'], reverse=True)
    
    db_session.close()

    return results


@app.route('/sim/get_results', methods = ['POST'])
def get_results():
    query = request.form.get('query')
    bind_name = request.form.get('bind_name')
    probabilityNum = request.form.get('probabilityNum')
    results = get_sim_all(query, bind_name, probabilityNum)
    # return jsonify({'results': results})
    return str(results)



# 使错误返回的信息为json格式的
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


