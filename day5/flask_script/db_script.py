from flask_script import Manager

db_manager = Manager()

@db_manager.command
def init():
    print("初始化完成")

@db_manager.command
def revision():
    print("迁移成功")

@db_manager.command
def upgrade():
    print("映射数据库成功")

#在manage.py中 先引入 from db_script import db_manager

#manager.add_command("db",db_manager) 表示执行数据库相关命令

#python manage.py db init
#python manage.py db revision
#python manage.py db upgrade