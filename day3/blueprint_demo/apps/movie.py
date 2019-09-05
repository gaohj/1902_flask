#encoding:utf-8
from flask import Blueprint

movie_bp = Blueprint('movie',__name__,url_prefix='/movie')

#http://127.0.0.1:5001/user/profile/
@movie_bp.route("/list/")
def list():
    return '电影列表页面'

@movie_bp.route("/detail/")
def detail():
    return '电影详情页面'