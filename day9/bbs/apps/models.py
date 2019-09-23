from exts import db
from datetime import datetime
class PostModel(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title =  db.Column(db.String(50),nullable=False)
    content =  db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)


