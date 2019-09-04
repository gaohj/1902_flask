from flask import Flask,render_template

app = Flask(__name__,template_folder=r'C:\templates')
app.config['DEBUG']=True

@app.route('/')
def hello_world():
    #默认会到templates目录下面查找页面
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5001)
