from flask import Flask,render_template
from flask_moment import  Moment #导入类库
from flask_script import Manager
from datetime import datetime,timedelta
app = Flask(__name__)
manager = Manager(app)
moment = Moment(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/moments/')
def moments():
    public_time = datetime.utcnow()+timedelta(seconds=-360)
    return render_template('moment.html',public_time=public_time)

if __name__ == '__main__':
    manager.run()
