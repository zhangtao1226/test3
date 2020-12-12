'''
Mysql 连接测试
'''

import pymysql
host = 'localhost'
user = 'root'
password = 'zhangtao'
dbname = 'images360'

db = pymysql.connect(host, user, password, dbname)

cursor = db.cursor()

tables = cursor.execute('show tables')
print(tables)

db.close()
