from flask_script import Manager
from app import app,Users,db
from db_script import db_manager
manager = Manager(app)
manager.add_command("db",db_manager)
# manager.add_command("cms",db_manager)
# manager.add_command("admin",db_manager)
## python manage.py greet  返回 hello boy
## 添加不需要传递参数的命令
@manager.command
def greet():
    print("hello boy")

#python manage.py add_user -u kangbazi -a 19
@manager.option("-u","--username",dest="username")
@manager.option("-a","--age",dest="age")
def add_user(username,age):
    print("你的姓名:%s;您的年龄:%s" % (username,age))


#python manage.py addUser -u kangbazi666 -e kangbazi666@163.com
@manager.option("-u","--username",dest="username")
@manager.option("-e","--email",dest="email")
def addUser(username,email):
    user = Users(username=username,email=email)
    db.session.add(user)
    db.session.commit()

if __name__  =="__main__":
    manager.run()