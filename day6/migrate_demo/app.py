from flask import Flask
import config
from ext import db



app = Flask(__name__)
app.config.from_object(config) #让配置文件生效
db.init_app(app) #db 跟 flask实例  app 绑定


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
