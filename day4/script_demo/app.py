from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
#
# class Person(object):
#     name = 'xx'
#     age = 18
#     country = 'xx'
#
# p = Person('xx','xx')
# Person -> 数据表  名字
#Person 的属性  -> 一张表的字段
#Person类的对象  -> 一张表的数据行


if __name__ == '__main__':
    app.run()
