from ..forms import BaseForm
from wtforms import StringField,IntegerField
from wtforms.validators import InputRequired,Email,Length,EqualTo
#{'password': ['密码长度在6-20位'], 'password_repeat': ['密码长度在6-20位', '两次密码必须一致']}

class LoginForm(BaseForm):
    email = StringField(validators=[Email(message="请输入正确的邮箱类型"),InputRequired(message="请输入邮箱")])
    password = StringField(validators=[Length(6,20,message="请输入正确格式的密码")])
    remember = IntegerField()

class ResetPwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(6,20,message="请输入正确格式的旧密码")])
    newpwd = StringField(validators=[Length(6,20,message="请输入正确格式的新密码")])
    newpwd2 = StringField(validators=[EqualTo('newpwd',message="两次密码必须保持一致")])