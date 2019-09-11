from  flask import Blueprint,request

bp = Blueprint('cms',__name__,url_prefix='/cms')

#http://jd.com:5001/cms
@bp.route('/')
def index():
    #cookie是前端提交过来的
    # request.args
    #request.form
    #request.files
    username = request.cookies.get('username')
    return username or '没有任何的cookie'