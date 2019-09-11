from flask import Flask,session
from flask_script import Manager
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ADFASDF1212ASDF'
manager = Manager(app)
@app.route('/')
def index():
    #当用户 提交用户名和密码  验证成功以后
    #我们就将用户名和密码存入session
    session['username'] = 'chaoge'
    session['user_id'] = '66'
    print(type(session))
    return 'Hello World!'

@app.route('/get_session/')
def get_session():
    username = session.get('username')
    user_id = session.get('user_id')
    print(username,user_id)
    return username or '没有任何session'

@app.route('/del_session/')
def del_session():
    session.clear()
    return '推出成功'



if __name__ == '__main__':
    manager.run()
