from flask import Flask
from werkzeug.routing import BaseConverter
import config
app = Flask(__name__)
#默认 flask不开启debug模式  debug 如果运行有错误 那么会在终端进行提示
app.config.from_object(config)

class TelConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'

app.url_map.converters['tel'] = TelConverter

@app.route('/tel/<tel:number>/')
def tel(number):
    return number


@app.route('/uuiddemo/<uuid:u_id>/')
def hello_world(u_id):
    return 'Hello World!我是5002 %s' % u_id

@app.route('/anys/<any(jiabin,liuqiong):any_id>/')
def anys(any_id):
    return any_id


@app.route('/path/<path:test>/')
def paths(test):
    return test


@app.route('/admin/<int:id>/')
def admin(id):
    return '我是管理后台 你是第%s 个用户' % id


@app.route('/teacher/<float:t_id>/')
def teacher(t_id):
    return '千锋教学保障 %s' % t_id
if __name__ == '__main__':
    # app.debug=True
    app.run(port=5002)
    # app.run(debug=True)
