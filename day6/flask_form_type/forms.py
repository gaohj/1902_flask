from wtforms import Form,StringField,PasswordField,SubmitField,IntegerField,BooleanField,SelectField,DateField
from wtforms.validators import Length,EqualTo,Email,InputRequired,NumberRange,Regexp,URL,UUID
from flask_wtf import FlaskForm
class RegisterForm(Form):
    username = StringField("用户名",validators=[Length(min=6,max=20,message="用户名长度在6-20位")])
    password = PasswordField("密码",validators=[Length(min=6,max=20,message="密码长度在6-20位")])
    password_repeat =  PasswordField("确认密码",validators=[Length(min=6,max=20,message="密码长度在6-20位"),EqualTo("password",message="两次密码必须一致")])
    submit = SubmitField("立即注册")


class LoginForm(FlaskForm):
    email = StringField("邮箱",validators=[Email(message="必须是邮箱类型")])
    username = StringField("用户名", validators=[Length(min=6, max=20, message="用户名长度在6-20位"),InputRequired("请填写用户名")])
    age = IntegerField(validators=[NumberRange(18,90)])
    phone = StringField(validators=[Regexp(r'1[3-9]\d{9}')])
    homepage = StringField(validators=[URL()])
    uuid = StringField(validators=[UUID()])
    captcha = StringField(validators=[Length(4,4)])
    creat_time = DateField("注册时间",validators=[])
    remember = BooleanField("记住我:")
    tags = SelectField("标签",choices=[('1','python'),('2','java')])
    submit = SubmitField("立即登录")
    #http://www.jiabin.com







