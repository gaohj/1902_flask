import tornado.web
from app.models import create_db,drop_db,Student
from utils.conn import session

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write('hello tornado')
        items = ['Python','C++','java','linux']
        self.render('index.html',items=items,items2=items)


class DbHandler(tornado.web.RequestHandler):
    def get(self):
        create_db()
        self.write("创建表成功")

class DropDbHandler(tornado.web.RequestHandler):
    def get(self):
        drop_db()
        self.write("删除表成功")

class AddDbHandler(tornado.web.RequestHandler):
    def post(self):
        # stu = Student(s_name="扛把子",s_age=18)
        # session.add(stu)
        # session.commit()
        stus = []
        for i in range(100):
            stu = Student()
            stu.s_name = 'qf_%s' % i
            stu.s_age = i
            stus.append(stu)
        session.add_all(stus)
        session.commit()
        self.write("新增数据成功")

class StuHandler(tornado.web.RequestHandler):
    def get(self):
        stus1 = session.query(Student).filter_by(s_name = 'qf_66').all()
        stus2 = session.query(Student).filter(Student.s_name == 'qf_88').all()
        print(stus1,stus2)
        self.write("查询数据成功")
    def delete(self):
        # stus2 = session.query(Student).filter(Student.s_name == 'qf_2').first()
        # if stus2:
        #     session.delete(stus2)
        #     session.commit()
        session.query(Student).filter(Student.s_name == 'qf_0').delete()
        session.commit()
        self.write("删除数据成功")
    def patch(self):
        # stus2 = session.query(Student).filter(Student.s_name == 'qf_1').first()
        # if stus2:
        #     stus2.s_name = 'kangbazi'
        #     session.add(stus2)
        #     session.commit()
        session.query(Student).filter(Student.s_name == 'qf_5').update({'s_name':'88888'})
        session.commit()
        self.write("更新数据成功")