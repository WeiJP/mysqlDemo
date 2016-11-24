# -*- coding:utf-8 -*-
# 2016-10-25 10:20
# auther:wjp
# MySQL

import mysql.connector

# 创建连接
conn = mysql.connector.connect(user = 'root', password = 'root', database = 'wjptestdb', use_unicode = True)
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print cursor.rowcount

# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print values

cursor.close()
conn.close()

