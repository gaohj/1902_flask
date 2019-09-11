from flask import Flask,g,request,session,current_app,render_template
from utils import log_a,log_b,log_c
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ASDFSADF1221212FASDF'

@app.route('/')
def index():
    username = request.args.get('username')
    session['user_id'] = 6666
    g.username = username
    log_a()
    log_b()
    log_c()

    return render_template('index.html')

@app.before_first_request
def before_first_request():
    print("欢迎新会员，要不要办卡")


@app.before_request
def before_request():
    user_id = session.get('user_id')
    if user_id:
        g.user = 'jiabinxiong'
    print("每次来了把卫生先搞一搞")

@app.context_processor
def context_processor():
    if hasattr(g,'user'):
        return {"kangbazi888":g.user}
    else:
        return {}

if __name__ == '__main__':
    app.run(debug=True,port=5002)
