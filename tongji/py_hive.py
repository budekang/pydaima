#!/usr/bin/python
#-*-coding:utf-8 -*-
import subprocess
import traceback
import sasl
from sasl.saslwrapper import *
from pyhive import hive
conn = hive.Connection(host='192.168.31.11', port=10000, username='hadoop', database='default')#host主机ip,port：端口号，username:用户名，database:使用的数据库名称
cursor=conn.cursor()
cursor.execute('select * from tomcat_logs limit 10')#执行查询
for result in cursor.fetchall():
     print(result)                      #将查询结果打印出来
