import tornado.web
import tornado.ioloop
from tornado.options import define,parse_command_line,options
from chat.views import LoginHandler,ChatHandler
from utils.settings import TEMPLATE_PATH,STATIC_PATH
define('port',default=8080,type=int)

def make_app():
    return tornado.web.Application(handlers=[
        (r'/login/',LoginHandler),
        (r'/chat/',ChatHandler),
    ],
        template_path=TEMPLATE_PATH,
        static_path=STATIC_PATH,
        debug=True,
        autoreload=True,
        cookie_secret = 'adfadfsdfs=23ff2sdfasda'
    )

if __name__ == "__main__":
    parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

