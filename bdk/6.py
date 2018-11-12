import pymysql

# 打开数据库连接
db = pymysql.connect(host='192.168.18.88', port=3306,
                     user='root', passwd='123456', db='test', charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
for i in range(1,1000):
    sql = "INSERT INTO CHARU(id) VALUES (2)"
    print(i)
# 一个tuple或者list
#T = (('xiaoming', 31, 'boy'), ('hong', 22, 'girl'), ('wang', 90, 'man'))

try:
    # 执行sql语句
    cursor.executemany(sql)
    # 提交到数据库执行
    db.commit()
except :
    # 如果发生错误则回滚
    #db.rollback()
    print("haha")
# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()