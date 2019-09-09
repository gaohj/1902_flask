from flask import Flask,render_template,request,flash,redirect,url_for
from flask_script import  Manager
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ad12ADFA12'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
manager = Manager(app)
bootstrap = Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField('用户名',validators=[DataRequired()])
    submit = SubmitField("立即提交")

    def validate_name(self,field):
        if len(field.data) < 6:
            raise ValidationError("用户名不能少于6个字符")



@app.route('/',methods=['GET','POST'])
def hello_world():
    form = NameForm()
    if form.validate():
        lastname = "十年前的流行是火星文"
        if lastname != form.name.data:
            flash("常换签名两种情况，要么你是性情中人，要么你是不专一")
            return redirect(url_for('hello_world'))
    name = form.name.data
    return render_template('form.html',form=form,name=name)


if __name__ == '__main__':
    manager.run()
