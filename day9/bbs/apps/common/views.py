from flask import Blueprint,render_template,request
from .forms import SMSCaptcha
from utils.sms_send import send_sms
from utils import restful,bbs_cache
bp = Blueprint("common",__name__,url_prefix='/common')

@bp.route('/')
def index():
    return render_template('common/index.html')


@bp.route('/sms_captcha/',methods=['POST'])
def sms_captcha():
    form = SMSCaptcha(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = '这里应该重新写个方法生成指定位数的验证码'
        bbs_cache.set(captcha.lower(),captcha.lower())
        send_sms(telephone,captcha)
        return restful.success()
    else:
        return restful.params_error(message='参数有误')