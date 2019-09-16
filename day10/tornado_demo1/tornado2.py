import tornado.ioloop
import tornado.web
from tornado.options import define,parse_command_line,options  #这是全局方法

define('port',default=8080,type=int)
#port 是 全局options的一个属性
#如果不写 --port=8082  那么默认端口号 就是 8080
#type 指的是  port的一个类型
#类似于类视图    也叫 请求处理函数类
# class IndexView(views.MethodView)
class IndexHandler(tornado.web.RequestHandler):
    #http://127.0.0.1:8888/?username=kangbazi
    def get(self):
        name = self.get_argument('username')

        #渲染相应给浏览器的数据
        self.write('hello %s  get' % name)
    def post(self):
        name = self.get_argument('username')
        self.write('hello %s  post' % name)

def make_app():
    return tornado.web.Application(handlers=[
        (r'/',IndexHandler),
    ])

#python tornado2.py --port=8081
if __name__ == "__main__":
    #解析命令行
    parse_command_line()#读取命令行  获取其中的参数
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()



