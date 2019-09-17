
import tornado.web
import tornado.ioloop
from app.views import IndexHandler
from utils.settings import TEMPLATE_PATH,STATIC_PATH
from tornado.options import parse_command_line,define,options

define('port',default=80,type=int)

def make_app():
    return tornado.web.Application(handlers=[
        (r'/',IndexHandler),

    ],
    template_path=TEMPLATE_PATH,
    static_path=STATIC_PATH,
    debug=True,
    autoreload=True
    )

#程序运行入口
if __name__ == "__main__":
    #解析命令行
    parse_command_line()
    #创建Application对象
    app = make_app()
    #监听端口号
    app.listen(options.port)
    #启动
    tornado.ioloop.IOLoop.current().start()