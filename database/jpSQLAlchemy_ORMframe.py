# -*- coding:utf-8 -*-
# 2016-10-25 11:21
# auther:wjp
# MySQL - SQLAlchemy,  ORM框架

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# create BaseClass
Base = declarative_base()

class User(Base):
	# 表名：
	__tablename__ = 'user'
	# 表结构：
	id = Column(String(20), primary_key = True)
	name = Column(String(20))

# init db connect
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/wjptestdb')
# 创建 DBSession类型：
DBSession = sessionmaker(bind = engine)

# 关键是获取session，
# 然后把对象添加到session，
# 最后提交并关闭。
# Session对象可视为当前数据库连接。

# 创建session对象：
session = DBSession()
# 创建新User对象：
new_user = User(id = '5', name = 'Bob')
# 添加到session：
session.add(new_user)
# 提交即保存到数据库：
session.commit()
# 关闭session：
session.close()

# 查询：
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，all()返回所有行
user = session.query(User).filter(User.id == '5').one()

print 'type:', type(user)
print 'name:', user.name

session.close()
