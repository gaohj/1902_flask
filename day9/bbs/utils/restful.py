
# {
#     "code":200,
#     "message":"",
#     "data":{
#         "name":'xxx',
#         "age":'xxx',
#     }
# }
#2开头 成功
#3开头 301永久重定向
#302临时重定向

from flask import jsonify


class HttpCode(object):
    success = 200
    unautherror = 401
    paramserror  = 400
    servererror = 500

def restful_result(code,message,data):
    return jsonify({"code":code,"message":message,"data":data or {} })


def success(message="",data=None):
    return restful_result(code=HttpCode.success,message=message,data=data)

def unauth_error(message="",data=None):
    return restful_result(code=HttpCode.unautherror,message=message,data=data)

def params_error(message="",data=None):
    return restful_result(code=HttpCode.paramserror,message=message,data=data)

def server_error(message=""):
    return restful_result(code=HttpCode.servererror,message=message or '服务器内部错误')