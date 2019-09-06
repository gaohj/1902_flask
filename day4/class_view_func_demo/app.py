from flask import Flask,views,render_template,request

app = Flask(__name__)
app.config.update({
    'DEBUG':True,
    'TEMPLATES_AUTO_RELOAD':True
})


class LoginView(views.MethodView):
    def __render(self,error=None):
        return render_template('login.html',error=error)
    def get(self):
        # 如果是get请求  那么就让用户看到登录页面
        return self.__render()
    def post(self):
        #如果是post请求 那么就提交数据到服务器
        username = request.form.get('username')
        #接收post表单提交
        password = request.form.get('password')
        if username == 'kangbazi' and password == '123456':
            return '登录成功'
        else:
            return self.__render(error="用户名或者密码错误")
    def put(self):
        pass
    def patch(self):
        pass
    def delete(self):
        pass

app.add_url_rule('/login/',view_func=LoginView.as_view('login'))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=5002)
