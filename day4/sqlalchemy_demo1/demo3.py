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
)
# pip install sqlalchemy
#pip install  pymysql
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


class TagNum(enum.Enum):
    python = "python"
    linux = "linux"
    mysql = "mysql"

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    price = Column(Float)
    is_delete = Column(Boolean)
    prices = Column(DECIMAL(10,4)) #100000.0001
    tag = Column(Enum(TagNum))
    create_time = Column(DateTime)
    content = Column(LONGTEXT)
Base.metadata.create_all()


article = Article(prices=100000.9999)
session.add(article)
session.commit()