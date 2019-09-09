from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
app = Flask(__name__)
app.config.from_object(config)
db =SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False)

db.create_all() #将这个改为命令行的方式








@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
