from flask import Flask,render_template
from flask_wtf import FlaskForm #导入表单基类
#导入字段类型
from wtforms import StringField,SubmitField
#导入验证器类
from wtforms.validators import DataRequired
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ASFSFSAD1212ADSFAS'
#<form>
#用户名:<input type="text" name="username">
#<input type="submit" value="立即提交">
class RegisterForm(FlaskForm):
    # 这个name叫什么  那么  <input type="text" name="username">
    username = StringField("用户名:",validators=[DataRequired()])
    submit = SubmitField("立即注册")

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register/',methods=['POST','GET'])
def register():
    name = None
    form = RegisterForm()
    if form.validate_on_submit(): #判断用户的输入是否符合要求
        name = form.name.data #接收表单提交的内容
        print(name)
        form.name.data = '' #提交之后 将输入框清空
    return render_template('index.html',form=form,name=name)


if __name__ == '__main__':
    app.run(debug=True,port=5001)
