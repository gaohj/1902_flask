from flask import Flask,views,render_template,jsonify

app = Flask(__name__)

class JsonView(views.View):

    def get_data(self):
        raise NotImplementedError

    def dispatch_request(self):
        return jsonify(self.get_data())

class ListView(JsonView):
    def get_data(self):
        return {'username':'kangbazi','password':'123456'}

app.add_url_rule('/list/',view_func=ListView.as_view('list'))
class CommonView(views.View):
    def __init__(self):
        super(CommonView, self).__init__()
        self.context = {
            'teacher_day':'他们要去轰趴'
        }


class LoginView(CommonView):
    def dispatch_request(self):
        self.context.update({
            'username':'wupython_ganggangde'
        })
        return render_template('login.html',**self.context)

class RegisterView(CommonView):
    def dispatch_request(self):
        return render_template('register.html',**self.context)

app.add_url_rule('/login/',view_func=LoginView.as_view('login'))
app.add_url_rule('/register/',view_func=RegisterView.as_view('register'))










@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True,port=5052)
