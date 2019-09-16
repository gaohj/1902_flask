from flask import Flask,jsonify,render_template
import qiniu
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)
@app.route('/')
def hello_world():
    return render_template('index.html')

#将 你的 两个key 上传过去    七牛云会返回一个token过来
@app.route('/uptoken/')
def uptoken():
    access_key = 'p_p2-jutlTI1mlPCSfMEO8DyZnkQaiFrd9IOlvpz'
    secret_key = 'rN0YQux570vbhL5d8QvShrV-SnjzTdqhlfWstWri'
    q = qiniu.Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = 'bbs1902'
    #服务端生成 token
    # token = q.upload_token(bucket_name, key, 3600)
    token = q.upload_token(bucket_name)

    return jsonify({"uptoken":token})

if __name__ == '__main__':
    manager.run()
