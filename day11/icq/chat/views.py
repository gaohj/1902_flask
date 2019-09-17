import tornado.web
import tornado.websocket

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

class ChatHandler(tornado.websocket.WebSocketHandler): #存储连接的对象
    user_online = []
    def open(self,*args,**kwargs):
        self.user_online.append(self)
        for user in  self.user_online:
            #当跳转到chat.html的时候 触发open函数
            username = self.get_secure_cookie('username').decode('utf-8')
            user.write_message('系统提示:【%s】进入聊天室' % username)
    #接收前端发送过来的数据
    def on_message(self,message):
        username = self.get_secure_cookie('username').decode('utf-8')
        for user in self.user_online:
            user.write_message('%s说:%s' % (username,message))
    def on_close(self):
        self.user_online.remove(self)
        for user in self.user_online:
            username = self.get_secure_cookie('username').decode('utf-8')
            user.write_message('系统提示:【%s已经退出聊天室】' % username )

