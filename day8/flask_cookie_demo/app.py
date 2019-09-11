from flask import Flask,request,Response
from flask_script import Manager
from datetime import datetime,timedelta
from getcookie import bp
app = Flask(__name__)
app.config['SERVER_NAME'] = 'jd.com:5001'
manager = Manager(app)
app.register_blueprint(bp)
@app.route('/')
def hello_world():
    resp = Response("千锋教育")
    # expires = datetime(year=2019,month=9,day=11,hour=9,minute=35,second=30)
    #浏览器  W3C浏览器  谷歌  火狐  safari  欧鹏
    #IE浏览器   IE8以下  浏览器  是不支持max_age的
    #如果同时写了 max_age  和  expires 那么以max_age 为准
    expires = datetime.now() +timedelta(days=30,hours=12)
    # resp.set_cookie("username","duodongxiong",expires=expires,max_age=60)
    # resp.set_cookie("username","duodongxiong",expires=expires,domain="jd.com")
    #domain只能指定的域名才可以访问
    # resp.set_cookie("username","duodongxiong",expires=expires,domain=".jd.com")
    #只能login才能有cookie
    resp.set_cookie("username","duodongxiong",expires=expires,path='/login/')
    return resp

@app.route('/login/')
def login():
    return '登录'

@app.route('/del/')
def delete_cookie():
    resp = Response("删除成功")
    #如果你要删除的 cookie 有域名限制  那么 你在删除cookie的时候也要加上 domain这个参数
    # resp.delete_cookie('username',domain=".jd.com")
    #如果你要删除的cookie 是 指定的 路径  那么 删除cookie的时候 也要加上 path参数
    resp.delete_cookie('username',path='/login/')
    return resp

if __name__ == '__main__':
    manager.run()
