from flask import Flask,request,render_template
from forms import RegisterForm
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register/',methods=['GET','POST'])
def register():

    if request.method == "GET":
        return render_template('register.html')
    else:
        # request.args.get()
        # request.POST.get()
        # request.form 接收表单过来的
        # request.file
        form = RegisterForm(request.form) # 表单提交多来的内容作为 参数
        if form.validate(): #如果用户的输入 满足要求
            return 'success'
        else:
            print(form.errors)  #打印表单错误消息
            return 'fail'


if __name__ == '__main__':
    app.run(debug=True,port=5001)
