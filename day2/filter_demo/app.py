from flask import Flask,render_template
from datetime import datetime
app = Flask(__name__)
app.config['DEBUG']=True#开启debug 模式
app.config['TEMPLATES_AUTO_RELOAD']=True
#自动加载

@app.route('/')
def hello_world():
    context = {
        'position':-9,
        # 'signature':'我心带明月'
        # 'signature':'<script>alert("666")</script>',
        'person':['zhangsan','lisi'],
        'article':'我的每一支笔 都知道你的名字 tianxin',
        'test':'',
        'create_time':datetime(2018,9,4,16,56,13)
    }
    return render_template('index.html',**context)

#过滤器本质上就是个函数
@app.template_filter('handle_time') #这个名字就是在模板中使用的名字
def handle_time(time):
    # 小于一分钟 显示刚刚
    # 一分钟到一个小时  几分钟之前
    # 一个小时到24小时  几小时之前
    # 24小时到30天    几天之前
    # 否则显示具体日期
    # 发表的时间 跟当前的时间完成对比
    if isinstance(time,datetime):#判断传递过来的时间是否是日期
        now = datetime.now() #当前的时间
        timestamp = (now-time).total_seconds() #当前时间 减去发表时间  转化成秒数
        if timestamp < 60:
            return "%s秒前" % int(timestamp)
        elif timestamp>=60 and timestamp<60*60:
            minutes = timestamp/60
            return "%s分钟前" % int(minutes)
        elif timestamp>=60*60 and timestamp<60*60*24:
            hours = timestamp/(60*60)
            return "%s小时前" % int(hours)
        elif timestamp>=60*60*24 and timestamp<60*60*24*30:
            days = timestamp/(60*60*24)
            return "%s天前" % int(days)
        else:
            return time.strftime('%Y/%m/%d %H:%M')
    else:
        return time #如果变量不是日期 那么直接返回

if __name__ == '__main__':
    app.run(port=5002)
