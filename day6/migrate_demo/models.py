from ext import db
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    age = db.Column(db.Integer)
    height = db.Column(db.String(30),default='165cm')