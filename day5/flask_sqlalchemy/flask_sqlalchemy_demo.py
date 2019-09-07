from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_sqlalchemy_demo'
USERNAME = 'root'
PASSWORD = '123456'

DB_UI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)


app.config['SQLALCHEMY_DATABASE_URI'] = DB_UI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class UserModel(db.Model):
    __tablename__ = "user_model"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return "User(id:%s,username:%s)" % (self.id,self.username)


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer,db.ForeignKey("user_model.id"))
    author = db.relationship("UserModel",backref="articles")

# db.drop_all()
# db.create_all()

# user = UserModel(username="kangbazi")
# article = Article(title="title one")
# article.author = user
# db.session.add(user)
# db.session.commit()
# users = UserModel.query.order_by(UserModel.id.desc()).all()
# print(users)
# users = UserModel.query.filter(UserModel.username=="kangbazi").first()
# users.username = "kangbazi666"
# db.session.commit()


users = UserModel.query.filter(UserModel.username=="kangbazi").first()
db.session.delete(users)
db.session.commit()


@app.route('/')
def index():
    return 'hello world'

if __name__ == "__main__":
    app.run(debug=True,port=5002)