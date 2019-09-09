from flask_script import Manager
from app import app
from models import User
from ext import db
from flask_migrate import Migrate,MigrateCommand
# MigrateCommand 相当于上节课说的 db_script
manager = Manager(app)
Migrate(app,db) #用来绑定app 和db 到  flask_migrate
manager.add_command("db",MigrateCommand)


if __name__ == "__main__":
    manager.run()