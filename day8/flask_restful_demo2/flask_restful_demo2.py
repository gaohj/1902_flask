from flask import Flask
import config
from ext import db
from flask_restful import Api,Resource,fields,marshal_with
from models import User,Article,Tag
from articleviews import article_bp
app = Flask(__name__)
api = Api(app)
app.config.from_object(config)
db.init_app(app)
app.register_blueprint(article_bp)
# class Article(object):
#     def __init__(self,name,age,school=None):
#         self.name = name
#         self.age = age
#         self.school = school
# article = Article(name="kangbazi",age=18)
#
# class ArticleView(Resource):
#     resource_fields = {
#         'name':fields.String(attribute="username"),
#         'age':fields.Integer,
#         'school':fields.String
#     }
#
#     @marshal_with(resource_fields)
#     def get(self):
#         #即使你不写 age、school 也会给你返回 age  school
#         #调用了装饰器  返回内容的时候 自动的  调取 上面的useranme age  school
#         #拼接json 返回
#         # return {"username":"kangbazi"}
#         return article
#
# api.add_resource(ArticleView,'/article/',endpoint='article')
#

@app.route('/')
def index():
    user = User(username="kangbazi",email="kangbazi@qq.com")
    article = Article(title="教你礼尚往来",content="我喜欢你你也得喜欢我")
    article.author = user
    tag1 = Tag(name="python")
    tag2 = Tag(name="java")
    article.tags.append(tag1)
    article.tags.append(tag2)
    db.session.add(article)
    db.session.commit()
    return 'hello world'

if __name__ == "__main__":
    app.run()
