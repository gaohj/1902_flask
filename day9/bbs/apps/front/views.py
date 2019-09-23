from flask import Blueprint,render_template,request
from ..models import PostModel
from flask_paginate import Pagination,get_page_parameter
import config
bp = Blueprint("home",__name__)

@bp.route('/')
def index():
    page = request.args.get(get_page_parameter(),type=int,default=1)
    start = (page-1)*config.PER_PAGE
    #1 0 9 10
    #2 10 19 10
    end = start + config.PER_PAGE

    posts = None
    total = 0

    #上一页 1 2... 48 49 50 51 52... 97 98下一页

    query_obj = PostModel.query.order_by(PostModel.create_time.desc())
    total = query_obj.count()
    #相当于 select * from posts limit 1,2
    posts = query_obj.slice(start,end)

    pagination = Pagination(bs_version=3,page=page,total=total,inner_window=2,outer_window=0)
    context = {
        'pagination':pagination,
        'posts':posts
    }
    return render_template('front/index.html',**context)