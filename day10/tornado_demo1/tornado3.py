import tornado.ioloop
import tornado.web
from tornado.options import define,parse_command_line,options  #这是全局方法
from datetime import datetime,timedelta
define('port',default=8080,type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # # name = self.get_argument('username',default="小新",strip=True)
        # name = self.get_arguments('username',strip=True) #这个返回的是列表  所以不能设置默认值
        # #http://127.0.0.1:8080/?username=kangbazi&age=18&username=guodong
        # #hello ['kangbazi', 'guodong'] get 请求与响应
        # self.write('hello %s  get 请求与响应' % name)
        #name = self.get_query_argument('username',default="这个人很懒什么都不写",strip=True) #等同于  get_argument
        name = self.get_query_arguments('username',strip=True)#等同于  get_arguments  返回的是列表
        self.write('hello %s  get 请求与响应' % name)
    def post(self):
        # name = self.get_argument('username')
        # self.write('hello %s  post 请求与响应' % name)
        #name = self.get_body_argument('username',default="这个人很懒什么都不写",strip=True) #等同于  get_argument
        name = self.get_body_arguments('username', strip=True)  # 等同于  get_arguments  返回的是列表
        self.write('hello %s  post 请求与响应' % name)

class RequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<h1>武汉的秋天最多一个星期</h1>')
        out_time = datetime.now()+timedelta(days=1)
        self.set_cookie('token','asfasdfsdaf',expires=out_time)
        self.clear_cookie('token') #这是清除指定的cookie
        # self.clear_all_cookies() #清除所有的cookie
        # self.set_status(404)
        # self.redirect('/')

def make_app():
    return tornado.web.Application(handlers=[
        (r'/',IndexHandler),
        (r'/req/',RequestHandler),
    ],autoreload=True,debug=True)
#自动重启 开启debug模式  检测到代码修改重启服务

#python tornado2.py --port=8081
if __name__ == "__main__":
    #解析命令行
    parse_command_line()#读取命令行  获取其中的参数
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()



