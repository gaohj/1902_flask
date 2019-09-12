from flask import Blueprint,render_template

bp = Blueprint("cms",__name__,url_prefix='/cms')

@bp.route('/')
def index():
    return render_template('cms/index.html')