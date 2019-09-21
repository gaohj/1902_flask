#实名认证  创建短信模板  获取模板id
#找到接口的Appkey 我的接口中能看到
#保证有剩余次数
#查看接口文档
#接口地址
#请求方式
#返回值类型
#请求参数  哪些是必填的 哪些可以不用填

#pip install requests

#导入requests库
import requests

def send_sms(mobile,captcha):
    #接口地址
    url = 'http://v.juhe.cn/sms/send'
    #根据接口文档看看 哪些参数 必填
    params = {
        "mobile":mobile,
        "tpl_id":135629,
        "tpl_value":"#code#"+captcha,
        "key":"06f0dbbb56b6771ad15248a17ba8c8d5"
    }

    #带着参数向接口地址发送请求
    response=requests.get(url,params=params)
    #将结果序列化成json
    result = response.json()
    #根据接口文档返回结果 提示  0表示 短信发送成功
    if result['error_code'] == 0:
        return True
    else:
        return False




