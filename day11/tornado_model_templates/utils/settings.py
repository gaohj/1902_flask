import os

#先获取到项目的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#模板文件路径
TEMPLATE_PATH = os.path.join(BASE_DIR,'templates')
STATIC_PATH = os.path.join(BASE_DIR,'static')