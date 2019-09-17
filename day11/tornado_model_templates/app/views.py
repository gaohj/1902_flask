import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # self.write('hello tornado')
        items = ['Python','C++','java','linux']
        self.render('index.html',items=items,items2=items)