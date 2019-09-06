from flask import Flask,render_template,request,redirect,url_for,views

app = Flask(__name__)

def login_required(func):
    def wrapper(*args,**kwargs):
        username = request.args.get('username')
        if username and username == "kangbazi":
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper


@app.route('/login/')
def login():
    return render_template('login.html')

#装饰器 实在 response到达浏览器之前执行
#
@app.route('/profile/')
@login_required #必须在路由下面添加装饰器
def profile():
    return '个人中心页面'

class SettingView(views.View):
    decorators = [login_required]
    def dispatch_request(self):
        return  '个人设置页面'

app.add_url_rule('/settings/',view_func=SettingView.as_view('settings'))

if __name__ == '__main__':
    app.run(debug=True,port=5002)
