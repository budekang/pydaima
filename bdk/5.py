import pymysql
db = pymysql.connect(host='192.168.18.1', port=3306,
                     user='root', passwd='123456', db='test', charset='utf8')
cur = conn.cursor()
sql = "insert into admin (name,addres) values (%s,%s)" 
params = ('zhang','san')
#sql = "insert into table(key1,key2,key3) values (%s,%s,%s)"%(value1,value2,value3)
temp=cur.execute(sql,params)
conn.commit()
recount = cur.execute('select *from admin')
rows = cur.fetchall()

cur.close()
conn.close()
for time in rows:
 #print temp #查看影响条目
 #print rows #查看数据库表内容
 print time