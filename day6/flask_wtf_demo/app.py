from flask import Flask,render_template,request

app = Flask(__name__)
app.config.update({
    'DEBUG':True,
    'TEMPLATES_AUTO_RELOAD':True
})

# @app.route('/login/')
# def login():
#     return render_template('login.html')
#
# @app.route('/check/',methods=['POST'])
# def check():
#     return "Hello %s" % request.form['username']

@app.route('/login/',methods=['GET','POST'])
def login():
    print(request.method)
    if request.method == "GET":
        return render_template('login.html')
    else:
        return "Hello %s" % request.form['username']




if __name__ == '__main__':
    app.run()
