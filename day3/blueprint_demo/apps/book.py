#encoding:utf-8
from flask import Blueprint

book_bp = Blueprint('book',__name__,url_prefix='/book')

#http://127.0.0.1:5001/user/profile/
@book_bp.route("/list/")
def list():
    return '图书列表页面'

@book_bp.route("/detail/")
def detail():
    return '图书详情页面'