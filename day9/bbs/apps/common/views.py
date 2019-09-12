from flask import Blueprint,render_template

bp = Blueprint("common",__name__,url_prefix='/common')

@bp.route('/')
def index():
    return render_template('common/index.html')