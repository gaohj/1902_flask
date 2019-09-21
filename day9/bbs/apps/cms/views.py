from flask import(
    Blueprint,
    render_template,
    views,
    request,
    session,
    redirect,
    url_for,
    g
)
import config
from .forms import LoginForm,ResetPwdForm
from .models import CMSUser
from .decorators import login_required
from utils import restful
from exts import db
bp = Blueprint("cms",__name__,url_prefix='/cms')

@bp.route('/')
def index():
    print(g.cms_user)
    return render_template('cms/cms_index.html')

@bp.route('/logout/',endpoint='logout')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))

@bp.route('/profile/',endpoint='profile')
@login_required
def profile():
    return render_template('cms/cms_profile.html')

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

class ResetPwdView(views.MethodView):
    def get(self):
        return render_template('cms/cms_reset_pwd.html')
    def post(self):
        form = ResetPwdForm(request.form)
        if form.validate():
            oldpassword = form.oldpwd.data
            newpassword = form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpassword):
                user.password = newpassword
                db.session.commit()
                return restful.success(message="成功")
            else:
                return restful.params_error("旧密码验证错误")
        else:
            return restful.params_error(form.get_errors())

bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))