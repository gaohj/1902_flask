from wtforms import Form,StringField,PasswordField,SubmitField,IntegerField,BooleanField,SelectField,DateField
from wtforms.validators import Length,EqualTo,Email,InputRequired,NumberRange,Regexp,URL,UUID
from flask_wtf import FlaskForm
from wtforms import ValidationError
class RegisterForm(FlaskForm):
    username = StringField("用户名",validators=[Length(min=6,max=20,message="用户名长度在6-20位")])
    password = PasswordField("密码",validators=[Length(min=6,max=20,message="密码长度在6-20位")])
    password_repeat =  PasswordField("确认密码",validators=[Length(min=6,max=20,message="密码长度在6-20位"),EqualTo("password",message="两次密码必须一致")])
    submit = SubmitField("立即注册")

#FlaskForm 继承于 Form
#如果你想用 flask_bootstrap渲染 那么必须继承于 FlaskForm
#如果使用 {{form.email.label}}{{form.email()}} 那么继承于 Form即可
class LoginForm(Form):
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

    #单独对某个字段做验证 那么需要在字段前加上 validate_
    def validate_email(self,field):
        #第一步导入模型
        #email = db.session.query(User).fileter(User.email==self.email).first()
        #if email:
        #抛出错误  该邮箱已经存在了
        # email = self.email.data  #表示用户在表单中输入的内容
        email = field.data  #表示用户在表单中输入的内容
        if email != 'kangbazi@163.com':
            raise ValidationError("邮箱已经存在")










