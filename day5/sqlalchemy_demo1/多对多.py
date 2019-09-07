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
ForeignKey,
Table
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
DATABASE = 'jiangxiligong'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
# 创建数据库引擎
engine = create_engine(DB_URI)
Base = declarative_base(engine)
# Session = sessionmaker(engine)  # 这个Session是个类
# session = Session()
session = sessionmaker(engine)()  #session 是个对象


article_tag = Table(
    "article_tag",
    Base.metadata,
    Column("article_id",Integer,ForeignKey("article.id"),primary_key=True),
    Column("tag_id",Integer,ForeignKey("tag.id"),primary_key=True)

)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text,nullable=False)
    # tags = relationship("Tag", backref="articles", secondary=article_tag)
    def __repr__(self):
        return "Article(title:%s,content:%s)" % (self.title,self.content)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    articles = relationship("Article",backref="tags",secondary=article_tag)

    def __repr__(self):
        return "Tag(name:%s)" % self.name


# 1.定义两个需要多对多的模型
#2.使用Table定义一个中间表 这个中间表包含两个模型的外键字段  并且让它们两个作为复合主键
#3.在两个需要多对多的模型中随便选一个定义一个relationship属性 来绑定三者之间的关系  绑定的时候需要传一个secondary  等于 中间表的名字
Base.metadata.drop_all()
Base.metadata.create_all()

article1 = Article(title="article3",content="kangbazi3")
article2 = Article(title="article4",content="kangbazi4")

tag1 = Tag(name='tag3')
tag2 = Tag(name='tag4')

# article1.tags.append(tag1)
# article1.tags.append(tag2)
#
# article2.tags.append(tag1)
# article2.tags.append(tag2)
#
# session.add(article1)
# session.add(article2)

tag1.articles.append(article1)
tag1.articles.append(article2)

tag2.articles.append(article1)
tag2.articles.append(article2)

session.add(tag1)
session.add(tag2)
session.commit()