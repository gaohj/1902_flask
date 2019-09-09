from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ADADSSDA12211ASDD'
#在实例化 bootstrap 之前  设置  使用本地文件 不用 官网css.js
#提高打开速度
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap(app)



class  LoginForm(FlaskForm):
    username = StringField("用户名",validators=[DataRequired()])
    password = PasswordField("密码",validators=[DataRequired()])
    submit = SubmitField("立即登录")


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/')
def login():
    form = LoginForm()
    return render_template("login.html",form=form)


if __name__ == '__main__':
    app.run(debug=True,port=5001)
