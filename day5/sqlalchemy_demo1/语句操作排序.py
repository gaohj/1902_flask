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

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text,nullable=False)
    create_time = Column(DateTime,nullable=False,default=datetime.now)
    def __repr__(self):
        return "Article(title:%s,content:%s,create_time:%s)" % (self.title,self.content,self.create_time)

Base.metadata.drop_all()
Base.metadata.create_all()

for x in range(100):
    title = "title%s" % x
    content = "content%s" % x
    article = Article(title=title,content=content)
    session.add(article)
session.commit()


article = session.query(Article).order_by(Article.id.desc())[0:20]
print(article)