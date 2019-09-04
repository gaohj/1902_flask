#从flask框架中导入flask类
from flask import Flask

#传入__name__ 创建一个Flask实例

app = Flask(__name__)

#app.route装饰器 将url 和 方法  进行映射
@app.route('/')
def hello_world():
    return 'Hello World888888!'


if __name__ == '__main__':
    #启动
    app.run()
