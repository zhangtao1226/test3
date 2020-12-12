'''
事务的 4 个属性
1、原子性（atomicity) : 事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
2、一致性（consistency) : 事务必须使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
3、隔离性 (isolation) : 一个事务的执行不能被其他事务干扰，即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能相互干扰。
4、持久性 (durability) : 持续性也称永久性（pernanence) ，指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该
                        对其有任何影响。

    插入、更新和删除操作都是对数据库进行更改的操作，而更改操作都必须为一个事务，所以这些操作的标准写法就是：
    try:
        cursor.execute(sql)
        db.commit()  # 提交执行
    except:
        db.rollback() # 错误回滚
'''

import pymysql

db = pymysql.connect(host='localhost', user='root', password='zhangtao', port=3306, db='spiders')

cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# cursor.execute("create database spiders default character set utf8")

# 创建表
def create_table():
    '''
    创建表
    :return:
    '''
    sql = 'create table if not exists students (id varchar(255) not null, name varchar(255) not null, age int not null, primary key (id))'
    cursor.execute(sql)


def insert_data():
    '''
    插入数据
    :return:
    '''
    id = '20110001'
    user = 'Tao'
    age = 20
    sql = 'insert into students (id, name , age) value(%s, %s, %s)'
    try:
        cursor.execute(sql, (id, user, age))
        db.commit()
    except:
        db.rollback()

# insert_data()

def dynamic_insert():
    data = {
        'id': '20200002',
        'name': 'zhang',
        'age': 21
    }
    table_name = 'students'
    field_name = ', '.join(data.keys())
    value_list = ', '.join(['%s'] * len(data))
    print(field_name, value_list)

    sql = 'insert into {table_name}({field_name}) value({value_list})'.format(table_name=table_name,
                                                                               field_name=field_name,
                                                                               value_list=value_list)
    try:
        if cursor.execute(sql, tuple(data.values())):
            db.commit()
            print('successful')
        else:
            print('sql error')
    except:
        print("filed")
        db.rollback()
# dynamic_insert()

def select_data():
    '''
    查询数据， 不需要 db.commit()
    注：因为内部实现有一个偏移指针用来指向查询结果，最开始偏移指针指向第一条数据，取一次后，指针偏移到下一条数据，这样再取的话，就会取到
        下一条数据，而不是全部的数据。所以 通过 while 循环 加 fetchone() 方法来获取数据。如下：
        sql = 'select * from students where age >= 20

        try:
            cursor.execute(sql)
            print('Count:', cursor.rowCount)
            row = cursor.fetchone()
            while row:
                print('Row: ', row)
                row = cursor.fetchone()
        except:
            print('error')
    :return:
    '''
    sql = 'select * from students where age >= 20'
    try:
        if cursor.execute(sql):
            print('Count: ', cursor.rowcount)
            row = cursor.fetchone()
            while row:
                print('Row: ', row)
                row = cursor.fetchone()
        else:
            print('sql error')
    except:
        print('error')


select_data()

db.close()