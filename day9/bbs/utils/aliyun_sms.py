from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('你的appkey id ', 'appkeysecret', 'cn-hangzhou')

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('dysmsapi.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('https') # https | http
request.set_version('2017-05-25')
request.set_action_name('SendSms')

request.add_query_param('RegionId', "cn-hangzhou")
request.add_query_param('PhoneNumbers', "要发送的手机号")
request.add_query_param('SignName', "小饭桌管理平台")
request.add_query_param('TemplateCode', "SMS_174580279")
request.add_query_param('TemplateParam', "{\"code\":要发送的验证码内容}")
#添加模板  模板中 有${code}  大括号中 是code  上面也是code

response = client.do_action(request)
# python2:  print(response)
print(str(response, encoding = 'utf-8'))

