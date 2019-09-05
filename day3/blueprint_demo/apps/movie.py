#encoding:utf-8
from flask import Blueprint,render_template,url_for

# movie_bp = Blueprint('movie',__name__,url_prefix='/movie',static_folder="movie_static",template_folder="movie")
movie_bp = Blueprint('movies',__name__,url_prefix='/movie',static_folder="movie_static")

#http://127.0.0.1:5001/user/profile/
@movie_bp.route("/list/")
def list():
    return render_template("movie_list.html")

@movie_bp.route("/detail/")
def detail():
    return '电影详情页面'