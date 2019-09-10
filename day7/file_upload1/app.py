from flask import Flask,render_template,request,send_from_directory,url_for
import os
from flask_script import Manager
#处理图片 要装上一个库  pillow pip install pillow 才能导入Image库
from PIL import Image
app = Flask(__name__)
#设置允许的后缀
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif'])
#设置保存的位置
app.config['UPLOAD_FOLDER'] = os.getcwd()
#设置上传文件的大小
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
manager = Manager(app)

#判断是否是允许的后缀
def allowed(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

#生成随机字符串
def random_string(length=20):
    import random
    base_str = '1234567890QRERTYUIOPASDFGHJKLZXCVBNM'
    return ''.join( random.choice(base_str) for i in range(length))



@app.route('/')
def hello_world():
    return 'Hello World!'
#http://127.0.0.1:5001/uploaded/CISF2QG1LNC0PR04FRQU.png/  让图片能访问 才能渲染到页面上
@app.route('/uploaded/<filename>/')
def uploaded(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/upload/',methods=['GET','POST'])
def upload():
    img_url = None
    if request.method == 'POST':#判断请求方式
        #获取表单提交的文件
        #保存上传文件
        file = request.files.get('photo') #接收表单提交的文件
        #print(file.filename) #输入文件的名字
        if file and allowed(file.filename):
            #获取文件后缀
            suffix = os.path.splitext(file.filename)[1]

            #生成随机的文件名
            filename = random_string()+suffix
            pathname = os.path.join(app.config['UPLOAD_FOLDER'],filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            file.save(pathname)
            #生成缩略图

            #1.打开文件
            img = Image.open(pathname)
            #2.重设尺寸
            img.thumbnail((128,128))
            #3.保存
            img.save(pathname)

            img_url = url_for('uploaded',filename=filename)

    return render_template('index.html',img_url=img_url)


if __name__ == '__main__':
    manager.run()
