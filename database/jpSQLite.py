# -*- coding:utf-8 -*-
# 2016-10-24 13:37
# auther:wjp
# SQLite

import sqlite3

# 连接到SQLite数据库
# 数据库文件是wjptest.db
# 如果文件不存在，自动再当前目录创建
conn = sqlite3.connect('wjptest.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一条记录:
cursor.execute('insert into user (id, name) values (\'1\',\'Michael\')')
# 影响的行数:
print cursor.rowcount

# 查询语句:
cursor.execute('select name from user where id = ?', ('1',))
# 获得结果集:
values = cursor.fetchall()
print values

# 关闭Cursor: 
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()