from sqlalchemy import (
create_engine,
Integer,
String,
Column,
Enum,
Float,
Text,
Boolean,
DECIMAL,
DateTime,
Date,
Time,
func,
or_,
and_,
ForeignKey
)
# pip install sqlalchemy
#pip install  pymysql
import random
from sqlalchemy.ext.declarative import declarative_base
#declarative_base 它是一个基类  类的父类
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.dialects.mysql import LONGTEXT
import enum
#sessionmaker在这里也是个基类
# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'jianshu6'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
# 创建数据库引擎
engine = create_engine(DB_URI)
Base = declarative_base(engine)
# Session = sessionmaker(engine)  # 这个Session是个类
# session = Session()
session = sessionmaker(engine)()  #session 是个对象

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)
    extend = relationship("UserExtend",uselist=False)

    def __repr__(self):
        return "User(username:%s)" % self.username


class UserExtend(Base):
    __tablename__ = 'user_extend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50),nullable=False)
    uid = Column(Integer,ForeignKey("user.id"))
    user = relationship("User",backref="extends")
    #backref   user可以通过这个获取到 school
    def __repr__(self):
        return "Extend(school:%s)" % self.school




class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text,nullable=False)

    uid = Column(Integer,ForeignKey("user.id"))

    def __repr__(self):
        return "Article(title:%s,content:%s)" % (self.title,self.content)

# Base.metadata.drop_all()
# Base.metadata.create_all()

# user = User(username="qfedu")
# extends = UserExtend(school="qfdaxue")
# user.extend = extends
#
# session.add(user)
# session.commit()

user = session.query(User).first()
print(user)
print(user.extends) #显示的学校的信息