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

    uid = Column(Integer,ForeignKey("user.id"))
    # author = relationship("User",backref="articles")
    author = relationship("User",backref=backref("articles",cascade="all"),cascade="save-update",single_parent=True)
    def __repr__(self):
        return "Article(title:%s,content:%s)" % (self.title,self.content)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)
    uid = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", backref="comments")

def my_init_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()

    user = User(username='青年之家')
    article = Article(title='我喜欢足球和梅西是假的',content="我喜欢你是假的")
    article.author = user

    comment = Comment(content="我爱你是真的")
    comment.author = user
    session.add(article)
    session.add(comment)

    session.commit()

def operation():
    # user = User(username="guodong")
    # article = Article(title='月亮很亮亮也没用没用也亮', content="我很喜欢你喜欢你也没用没用也喜欢你")
    # article.author = user
    #
    # session.add(user)
    # session.add(article)
    # user = session.query(User).filter_by(id=2).first()
    # session.expunge(user)
    # session.commit()
    # user = User(username="guodong2")
    # article = Article(title='月亮很亮亮也没用没用也亮2', content="我很喜欢你喜欢你也没用没用也喜欢你2")
    # article.author = user
    #
    # session.add(user)
    # session.add(article)
    # session.expunge(user)
    # session.commit()
    user = session.query(User).filter_by(id=3).first()
    session.delete(user)
    session.commit()

if __name__ == "__main__":
    # my_init_db()
    operation()

