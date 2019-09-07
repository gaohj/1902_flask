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
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.dialects.mysql import LONGTEXT
import enum
from datetime import datetime
#sessionmaker在这里也是个基类
# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'jianshu'
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

    def __repr__(self):
        return "User(username:%s)" % self.username
# 外键添加到多的那个表上   user 1 article多  外键添加到多的上面
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text,nullable=False)
    create_time = Column(DateTime,nullable=False,default=datetime.now)
    uid = Column(Integer,ForeignKey("user.id"))
    author = relationship("User",backref="articles")
    # author = relationship("User",backref=backref("articles",cascade="all"),cascade="save-update",single_parent=True)
    # mapper_args = {
    #     "order_by": create_time
    # }
    __mapper_args__ = {
        "order_by":create_time.desc()
    }

    def __repr__(self):
        return "Article(title:%s,content:%s,create_time:%s)" % (self.title,self.content,self.create_time)

# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user = User(username='青年之家')
# article1 = Article(title='我喜欢足球和梅西是假的', content="我喜欢你是假的")
# # article.author = user
# user.articles = [article1]
#
# session.add(user)
# session.commit()
#
# import time
# time.sleep(2)
#
# article2 = Article(title='我深夜老睡不着是假的', content="我想你你是真的")
# user.articles.append(article2)
# session.commit()

articles = session.query(Article).all()
print(articles)
