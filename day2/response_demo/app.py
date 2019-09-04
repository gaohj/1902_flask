from flask import Flask,Response,render_template,request,redirect,url_for
from werkzeug.routing import BaseConverter
app = Flask(__name__)
app.config['DEBUG']=True

class TelConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'

app.url_map.converters['tel'] = TelConverter

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/admins/<tel:number>/')
def admin(number):
    return '欢迎来到管理后台 %s' % number

@app.route('/about/')
def about():
    rep = Response(response='扛把子冲令兄',status=404,content_type='text/json;charset=utf-8')
    return rep

@app.route('/signin/')
def login():
    return render_template('index.html')

@app.route('/profile/')
def profile():
    #http://127.0.0.1:5001/profile/?name=kangbazi
    name = request.args.get('name')
    if name:
        return render_template('profile.html')
    else:
        # return redirect('/signup/')
        # return url_for('login')
        return redirect(url_for('login'))



if __name__ == '__main__':

    app.run(port=5001)
