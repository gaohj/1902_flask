from flask_script import Manager
from flask_restful_demo2 import app
from ext import db
import models
from flask_migrate import Migrate,MigrateCommand

Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()