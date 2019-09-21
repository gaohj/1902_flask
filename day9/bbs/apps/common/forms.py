from apps.forms import BaseForm
from wtforms import StringField
from wtforms.validators import regexp,InputRequired


class SMSCaptcha(BaseForm):
    telephone = StringField(validators=[regexp(r'1[3-9]\d{9}')])
