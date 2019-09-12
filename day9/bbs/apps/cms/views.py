from flask import(
    Blueprint,
    render_template,
    views,
    request,
    session,
    redirect,
    url_for
)
import config
from .forms import LoginForm
from .models import CMSUser
bp = Blueprint("cms",__name__,url_prefix='/cms')

@bp.route('/')
def index():
    return render_template('cms/cms_index.html')

class LoginView(views.MethodView):
    def get(self,message=None):
        return render_template('cms/cms_login.html',message=message)
    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    #如果session.permanent = True
                    #session的持久化日期为 31天
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message="用户名或者密码错误")
        else:
            message = form.get_errors()
            return self.get(message=message)



bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))