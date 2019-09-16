from flask import Flask,render_template
from flask_script import Manager
from ueditor import bp
import config
app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(bp)
manager = Manager(app)

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()
