from flask_script import Manager
from bbs import create_app
from apps.cms import models as cms_models
from flask_migrate import Migrate,MigrateCommand
from exts import db
from apps.models import PostModel

CMSUser = cms_models.CMSUser
app = create_app()
manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.option('-u','--username',dest="username")
@manager.option('-p','--password',dest="password")
@manager.option('-e','--email',dest="email")
def create_cms_user(username,password,email):
    user = CMSUser(username=username,password=password,email=email)
    db.session.add(user)
    db.session.commit()
    print("cms用户添加成功")

@manager.command
def create_test_post():
    for x in range(1,200):
        title = "标题:%s" %x
        content = "内容:%s" %x
        post = PostModel(title=title,content=content)
        db.session.add(post)
        db.session.commit()
    print("帖子添加成功")



if __name__ == "__main__":
    manager.run()