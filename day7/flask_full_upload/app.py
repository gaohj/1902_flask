import os
from flask import Flask,render_template
from flask_script import Manager
from flask_uploads import UploadSet,IMAGES,configure_uploads,patch_request_class
from flask_wtf import FlaskForm #导入表单基类
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import SubmitField
from flask_bootstrap import Bootstrap
from PIL import Image
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ADSFASD1212ASFSFSD'
app.config['MAX_CONTENT_LENGTH'] = 8*1024*1024  #自己设定的文件大小
#设置保存的位置
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.path.dirname(__file__),'uploads')
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
#创建文件上传对象 主要用来设置 允许的上传类型
photos = UploadSet('photos',IMAGES)

#将上传对象 跟 app实例完成绑定
configure_uploads(app,photos)

#配置上传文件大小 size默认64M 如果size为None
#那么就会按照我们自己设置的 app.config['MAX_CONTENT_LENGTH'] 大小
patch_request_class(app,size=None)
bootstrap = Bootstrap(app)
manager = Manager(app)

#生成随机字符串
def random_string(length=20):
    import random
    base_str = '1234567890QRERTYUIOPASDFGHJKLZXCVBNM'
    return ''.join( random.choice(base_str) for i in range(length))

# 创建一个上传表单类
class UploadForm(FlaskForm):
    photo = FileField('头像上传',validators=[FileRequired('请选择文件'),FileAllowed(photos,message="只允许上传图片")])
    submit = SubmitField("立即上传")





@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload/',methods=['GET','POST'])
def upload():
    img_url = None
    form = UploadForm()
    if form.validate():
        #获取文件后缀
        suffix = os.path.splitext(form.photo.data.filename)[1]
        #随机字符串+后缀名 = 新的文件名
        filename = random_string()+suffix
        #保存
        photos.save(form.photo.data,name=filename)
        #生成缩略图
        pathname = os.path.join(app.config['UPLOADED_PHOTOS_DEST'],filename)
        img = Image.open(pathname)

        img.thumbnail((128,128))

        img.save(pathname)


        #获取文件上传的图片完整url
        img_url = photos.url(filename)
    return render_template('index.html',form=form,img_url=img_url)

if __name__ == '__main__':
    manager.run()
