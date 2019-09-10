from flask import Flask,request,render_template
from forms import RegisterForm,LoginForm
from flask_bootstrap import Bootstrap
from wtforms.validators import ValidationError
app = Flask(__name__)
app.config['SECRET_KEY'] = '123ADFASD112'
app.config['BOOTSTRAP_SERVE_LOCAL']=True
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register/',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == "GET":
        return render_template('register.html',form=form)
    else:
        # request.args.get()
        # request.POST.get()
        # request.form 接收表单过来的
        # request.file
        form = RegisterForm(request.form) # 表单提交多来的内容作为 参数
        if form.validate_on_submit(): #如果用户的输入 满足要求
            return 'success'
        else:
            print(form.errors)  #打印表单错误消息
            return 'fail'

@app.route('/login/',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template('login.html',form=form)
    else:
        form = LoginForm(request.form) # 表单提交多来的内容作为 参数
        if form.validate(): #如果用户的输入 满足要求
            return 'success'
        else:
            print(form.errors)  #打印表单错误消息
            return 'fail'

if __name__ == '__main__':
    app.run(debug=True,port=5001)
