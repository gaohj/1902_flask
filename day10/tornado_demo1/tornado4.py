import tornado.ioloop
import tornado.web
from tornado.options import define,parse_command_line,options  #这是全局方法
from datetime import datetime,timedelta
import pymysql
define('port',default=8080,type=int)

class TimesHandler(tornado.web.RequestHandler):
    def get(self,year,month,day):
        self.write('%s年%s月%s日' %(year,month,day))

class Times2Handler(tornado.web.RequestHandler):
    def get(self,year,month,day):
        self.write('%s年%s月%s日'%(year,month,day))

    def post(self,year,month,day):
        #127.0.0.1:8086/days2/2019/10/20/
        self.write('只负责新增数据')

    def put(self,year,month,day):
        #127.0.0.1:8086/days2/2019/10/20/
        self.write('全量更新 修改全部的属性')

    def patch(self,year,month,day):
        #127.0.0.1:8086/days2/2019/10/20/
        self.write('增量更新 修改部分属性')

    def delete(self,year,month,day):
        self.write('负责删除数据')

class EntryHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.conn = pymysql.Connection(host='127.0.0.1',port=3306,user='root',password='123456',database='jianshu')
        self.cursor = self.conn.cursor()
        self.write("我就相当于构造函数  init")
    def prepare(self):
        self.write("我在请求到达浏览器之前执行 ")
    def get(self):
        sql = 'select * from article where id>0 limit 0,10'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print(data)
        self.write("请求到了浏览器")
    def post(self):
        pass
    def on_finish(self):
        self.cursor.close()
        self.conn.close()
        print("it is over")

def make_app():
    return tornado.web.Application(handlers=[
        (r'/days/(\d{4})/(\d{2})/(\d{2})/',TimesHandler), #这个是不指定参数名

        (r'/days2/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/',Times2Handler),
        (r'/entry/',EntryHandler),
        #这是指定参数名
    ],autoreload=True,debug=True)
#自动重启 开启debug模式  检测到代码修改重启服务

#python tornado2.py --port=8081
if __name__ == "__main__":
    #解析命令行
    parse_command_line()#读取命令行  获取其中的参数
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()



