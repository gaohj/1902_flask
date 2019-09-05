from flask import Flask,url_for

app = Flask(__name__)


# @app.route('/',endpoint="index")
@app.route('/')
def hello_world():
    print(url_for('hello_world'))
    return 'Hello World!'

def my_list():
    return '我是列表页'
# app.add_url_rule('/list/',endpoint="haha",view_func=my_list)
app.add_url_rule('/list/',view_func=my_list)

with app.test_request_context():
    # print(url_for('haha'))
    # print(url_for('index'))
    print(url_for('my_list'))
if __name__ == '__main__':
    app.run(debug=True,port=5002)
