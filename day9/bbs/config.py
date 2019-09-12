#encoding:utf-8
import os
SECRET_KEY = os.urandom(24)



HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = '1902bbs'
USERNAME = 'root'
PASSWORD = '123456'

DB_UI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)


SQLALCHEMY_DATABASE_URI = DB_UI
SQLALCHEMY_TRACK_MODIFICATIONS= False

CMS_USER_ID = 'ASDFSADFDSFSDFSDF'