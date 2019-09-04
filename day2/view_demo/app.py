from flask import Flask,render_template,redirect,url_for

# app = Flask(__name__,template_folder=r'C:\templates')
app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def hello_world():
    context = {
        'username':'chonglingling',
        'password':'123456',
        'age':25,
        'country':'china',
        'children':{
            'name':'xiaoling',
            'age':3
        }
    }
    #默认会到templates目录下面查找页面
    return render_template('index.html',**context)

@app.route('/test/')
def test():
    return render_template('test.html',username="chongling",password='666666',age=18)

@app.route('/login/<id>/')
def logins(id):
    # return redirect(url_for('test'))
    return render_template('login.html',id=id)

@app.route('/urlfor/')
def urlfor():
    return render_template('urlfor.html')

if __name__ == '__main__':
    app.run(port=5001)
