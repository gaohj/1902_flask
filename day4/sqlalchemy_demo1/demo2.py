from sqlalchemy import create_engine,Integer,String,Column
# pip install sqlalchemy
#pip install  pymysql
from sqlalchemy.ext.declarative import declarative_base
#declarative_base 它是一个基类  类的父类
from sqlalchemy.orm import sessionmaker
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
#创建一个orm模型  必须继承自sqlalchemy 提供给我们的一个基类
#create table person(id int(11) unsigned primary key auto_increment not null,name varchar(30) not null,age tinyint not null);
class User(Base):
    __tablename__ = 'user'
    #创建一些属性  跟表中的字段进行一一映射 这些属性必须是sqlalchemy 给我们提供的数据类型
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False)
    age = Column(Integer)
    country = Column(String(50))

    def __str__(self):
        return "(User(name:%s,age:%d,coutry:%s))" % (self.name,self.age,self.country)

#将创建好的模型映射到数据库中 一旦映射了以后 以后再修改字段 也不会重新映射了
# Base.metadata.drop_all() #创建之前先删除
Base.metadata.create_all()

def add_data():
    u1 = User(name="kangbazi1",age=19,country="dazhongguo1")
    u2 = User(name="kangbazi2",age=16,country="dazhongguo2")
    u3 = User(name="kangbazi3",age=17,country="dazhongguo3")
    #实现增删改查 需要一个session会话对象
    # session.add(u1)
    session.add_all([u1,u2,u3])
    session.commit()

def search_data():
    # all_user = session.query(User).all()
    # for a in all_user:
    #     print(a)
    # all_user = session.query(User).filter_by(name="xiaoqiong").all()
    # for a in all_user:
    #     print(a)

    # all_user = session.query(User).filter(User.name=="xiaoqiong").all()
    # for a in all_user:
    #     print(a)
    person = session.query(User).first()
    print(person)

def update_data():
    u1 = session.query(User).first()
    u1.name = 'qiongqiongxiaoxi'
    session.commit()

def delete_data():
    u1 = session.query(User).first()
    session.delete(u1)
    session.commit()
if __name__ == "__main__":
    # add_data()
    # search_data()
    # update_data()
    delete_data()