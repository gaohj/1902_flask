import tornado.web

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        error = ''
        self.render('login.html',error=error)
    def post(self):
        #获取用户登录信息
        username= self.get_body_argument('username')
        password= self.get_body_argument('password')
        if username in ['coco','tony','james'] and password == '123456':
            self.set_secure_cookie('username',username)
            self.render('chat.html',username=username)
        else:
            error = '用户名或者密码错误'
            self.render('login.html', error=error)

