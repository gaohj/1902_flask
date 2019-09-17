from utils.conn import Base
from sqlalchemy import Column,Integer,String

def create_db():
    Base.metadata.create_all()

def drop_db():
    Base.metadata.drop_all()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True,autoincrement=True)
    s_name = Column(String(10),unique=True,nullable=False)
    s_age = Column(Integer,default=18)

    def __repr__(self):
        return "Student(name:%s,age:%s)" % (self.s_name,self.s_age)
