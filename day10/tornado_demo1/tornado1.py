import tornado.ioloop
import tornado.web

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


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()



