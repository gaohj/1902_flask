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
func,
or_,
and_
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

    def __repr__(self):
        return "Article(title:%s,price:%s)" % (self.title,self.price)

# Base.metadata.drop_all()
# Base.metadata.create_all()

# for x in range(100):
#     article = Article(title='title%s'%x,price=random.randint(50,100))
#     session.add(article)
# session.commit()


def  select_data():
     # result = session.query(Article).filter_by(id=1)
     # result = session.query(Article).filter(Article.id==1).first()
     # print(result)

     # article = session.query(Article).filter(Article.title == 'title0').first()
     # print(article)
     #
     # articles = session.query(Article).filter(Article.title != 'title0').all()
     # print(articles)

     #like  模糊查询 只需要后边这个%即可
     # ilike 不区分大小写
     #SELECT users.username as 用户,order_goods.`name` as 商品,order_goods.buytime as "购买时间" FROM users,order_goods WHERE users.uid=order_goods.uid;
     #select 表1.字段,表n.字段 from 表1 INNER JOIN 表2 ON 条件;
     #select users.username,users.uid,order_goods.name,order_goods.buytime from users INNER JOIN order_goods ON users.uid=order_goods.uid;
     #外连接
     #left join 以左边表为准 和 right join 以右边表为准
     #select users.username,users.uid,order_goods.name,order_goods.buytime from users LEFT JOIN order_goods ON users.uid=order_goods.uid;
     #select users.username,users.uid,order_goods.name,order_goods.buytime from users RIGHT JOIN order_goods ON users.uid=order_goods.uid;

     # 子查询
     #SELECT * from users where uid in(SELECT uid from order_goods);
     # articles = session.query(Article).filter(Article.title.ilike('title%')).all()
     # print(articles)

     #in
     # articles = session.query(Article).filter(Article.title.in_(['title1','title2'])).all()
     # print(articles)

     #not in
     # articles = session.query(Article).filter(Article.title.notin_(['title1', 'title2'])).all()
     # print(articles)

     #not in
     # articles = session.query(Article).filter(~Article.title.in_(['title1', 'title2'])).all()
     # print(articles)

     #判断为空  也就是 is null
     # articles = session.query(Article).filter(Article.price==None).all()
     # print(articles)

     # articles = session.query(Article).filter(Article.price != None).all()
     # print(articles)

    # and

     # articles = session.query(Article).filter(Article.title=='title1',Article.price==81).all()
     # print(articles)

     # articles = session.query(Article).filter(or_(Article.title == 'title1', Article.price == 81)).all()
     # print(articles)

     articles = session.query(Article).filter(and_(Article.title == 'title1', Article.price == 81)).all()
     print(articles)




if __name__ == "__main__":
    select_data()