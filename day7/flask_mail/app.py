import os
from flask import Flask,render_template
from flask_script import Manager
from flask_mail import Message,Mail
app = Flask(__name__)

#wxrzwztzgcmhdhgc 这是授权码 不是 密码
#2287228249@qq.com  #邮件账户名
#smtp.qq.com 右键发送服务器

app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER','smtp.126.com')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME','gaohj66666@126.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD','zxasqw12')

#创建邮件发送对象之前 必须完成相关配置
mail = Mail(app)
manager = Manager(app)

def send_mail(to,sub,template,**kwargs):
    #创建邮件对象
    msg = Message(subject=sub, recipients=[to], sender=app.config['MAIL_USERNAME'])
    # 如果你是用浏览器访问 邮件
    msg.html =render_template(template+'.html',**kwargs)

    # 如果你是用客户端 来查看邮件
    msg.body = render_template(template+'.txt',**kwargs)
    mail.send(message=msg)
@app.route('/')
def index():
    # #创建邮件对象
    # msg = Message(subject="账户激活",recipients=['2592668397@qq.com'],sender=app.config['MAIL_USERNAME'])
    # #如果你是用浏览器访问 邮件
    # msg.html = '<h1>你好,请点击以下链接完成激活</h1>'
    #
    # # 如果你是用客户端 来查看邮件
    # msg.body = '你好,请点击以下链接完成激活'
    #
    # mail.send(message=msg)
    send_mail('2592668397@qq.com','激活汝账户','activate',username="佳彬")
    return '邮件已经发送'


if __name__ == '__main__':
    manager.run()
