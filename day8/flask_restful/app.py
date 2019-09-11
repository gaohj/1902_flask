from flask import Flask,render_template
from flask_script import Manager
from flask_restful import Api,Resource,reqparse,inputs
#flask_restful提供了一个 类似于 wtfforms的 验证参数是否合法  叫 reqparse  inputs在这里用来强制转化
app = Flask(__name__)
manager = Manager(app)
api = Api(app)

# class LoginView(Resource):
#     def post(self,username=None):
#         return {"username":"chaoge"}

class LoginView(Resource):
    def post(self):
        from datetime import date
        #这是python自带的date
        #我们的flask_restfule验证日期类型 需要 inputs.date
        #区别: 原生的  date  date(2019,9,11)
        #inputs.date   2019-9-11  所以这里不用  自带的date
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=int,help="用户名验证错误",required=True)
        parser.add_argument('homepage',type=inputs.url,help="必须是url类型",required=True)
        parser.add_argument('telephone',type=inputs.regex(r'1[3-9]\d{9}'),help="手机号类型有错误",required=True)
        parser.add_argument('birth',type=inputs.date,help="生日字段验证错误",required=True)
        parser.add_argument('gender',type=str,choices=['male','female','secret'])
        args = parser.parse_args()
        print(args)
        return {"username": "chaoge"}
# api.add_resource(LoginView,'/login/<username>/','/signup/')
api.add_resource(LoginView,'/login/')

#注意事项
#如果你想要返回json数据 那么就使用flask_restful  还有就是类视图
#class JsonView(View): def dispath_request(self): jsonify(self.get_data)
#如果想返回给前端是个页面  那么  app.route 就可以了


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()
