import os
from flask import Flask,request,render_template,send_from_directory
from forms import UploadForm
from flask_script import Manager
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
app = Flask(__name__)
UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')
manager = Manager(app)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload/',methods=['POST','GET'])
def upload():
    if request.method == "GET":
        return render_template('index.html')
    else:
        # request.form.get('desc')
        # request.files.get('avator')
        form = UploadForm(CombinedMultiDict([request.form,request.files]))
        if form.validate():
            desc = form.desc.data
            avator = form.avator.data
            #avator表示上传过来的文件的名字
            #secure_filename用它来堆上传文件的名字 进行安全过滤
            filename = secure_filename(avator.filename)
            avator.save(os.path.join(UPLOAD_PATH,filename))
            print(desc)
            return '上传成功'
        else:
            print(form.errors)
            return 'fail'

@app.route('/images/<filename>/')
def images(filename):
    return send_from_directory(UPLOAD_PATH,filename)




if __name__ == '__main__':
    manager.run()
