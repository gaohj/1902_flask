from wtforms import Form,StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo

class RegisterForm(Form):
    username = StringField(validators=[Length(min=6,max=20,message="用户名长度在6-20位")])
    password = PasswordField(validators=[Length(min=6,max=20,message="密码长度在6-20位")])
    password_repeat =  PasswordField(validators=[Length(min=6,max=20,message="密码长度在6-20位"),EqualTo("password",message="两次密码必须一致")])




