from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#连接数据库
db_url = 'mysql+pymysql://root:123456@127.0.0.1:3306/jianshu'


#创建引擎
engine = create_engine(db_url)

#创建一个模型并把它映射到数据表中  需要继承于Base基类

Base = declarative_base(engine)

#数据库的增删改查需要一个session对象
session = sessionmaker(engine)()

