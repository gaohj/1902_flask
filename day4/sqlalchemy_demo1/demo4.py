from sqlalchemy import (
create_engine,
Integer,
String,
Column,
Enum,
Float,
Boolean,
DECIMAL,
DateTime,
Date,
Time,
func
)
# pip install sqlalchemy
#pip install  pymysql
import random
from sqlalchemy.ext.declarative import declarative_base
#declarative_base 它是一个基类  类的父类
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import LONGTEXT
import enum
#sessionmaker在这里也是个基类
# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
# 创建数据库引擎
engine = create_engine(DB_URI)
Base = declarative_base(engine)
# Session = sessionmaker(engine)  # 这个Session是个类
# session = Session()
session = sessionmaker(engine)()  #session 是个对象


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    price = Column(Float,nullable=False)

    def __str__(self):
        return "Article(title:%s,price:%s)" % (self.title,self.price)

# Base.metadata.drop_all()
# Base.metadata.create_all()

# for x in range(100):
#     article = Article(title='title%s'%x,price=random.randint(50,100))
#     session.add(article)
# session.commit()

#模型对象
# articles = session.query(Article).all()
# print(articles)
#模型的属性
# articles = session.query(Article.title,Article.price).all()
# print(articles)

result = session.query(func.count(Article.id)).first()
print(result)

result = session.query(func.avg(Article.price)).first()
print(result)

result = session.query(func.max(Article.price)).first()
print(result)

result = session.query(func.min(Article.price)).first()
print(result)

result = session.query(func.sum(Article.price)).first()
print(result)