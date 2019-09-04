from flask import Flask,Response,render_template
app = Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/admin/')
def admin():
    return '欢迎来到管理后台'

@app.route('/about/')
def about():
    rep = Response(response='扛把子冲令兄',status=404,content_type='text/json;charset=utf-8')
    return rep

@app.route('/login/')
def login():
    return render_template('index.html')
if __name__ == '__main__':

    app.run(port=5001)
