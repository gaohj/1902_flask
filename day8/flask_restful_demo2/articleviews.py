from flask import Blueprint,render_template,make_response,Response
from flask_restful import Api,Resource,fields,marshal_with
from models import Article
import json
article_bp = Blueprint('article',__name__,url_prefix='/article')

api = Api(article_bp)
# 这个方法 用来 在浏览器显示的字符串按照  html的方式 显示
#如果没有这一步  那么显示的就是字符串
#如果 想以页面的形式返回  那么使用representation来定义一个函数
#在这个函数中 封装一个方法  支持返回 页面 和 json
#这个方式支持返回 html和  json  
@api.representation('text/html')
def out_html(data,code,headers):
    #如果是字符串  那么就以页面的形式展示
    if isinstance(data,str):
        resp = make_response(data)
        return resp
    else:
        #否则以json形式展示
        return Response(json.dumps(data),mimetype="application/json")


class ArticleView(Resource):
    resource_fields = {
        'article_tile':fields.String(attribute='title'),
        'content':fields.String,
        'author':fields.Nested({
            'username':fields.String,
            'email':fields.String,
        }),
        'tags':fields.List(fields.Nested({
            'id':fields.Integer,
            'name':fields.String
        })),
        'read_count':fields.Integer(default=100)

    }
    @marshal_with(resource_fields)
    def get(self,article_id):
        article = Article.query.get(article_id)
        return article
    # def post(self):
    #     pass
    # def put(self):
    #     pass
    # def delete(self):
    #     pass

api.add_resource(ArticleView,'/<article_id>/',endpoint="article")


class AboutView(Resource):
    def get(self):
        return render_template('index.html')
api.add_resource(AboutView,'/about/',endpoint="about")
