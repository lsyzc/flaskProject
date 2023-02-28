from models import User,EmailCaptcha
import wtforms
from exts import db
from wtforms.validators import Email,Length,EqualTo
from werkzeug.security import check_password_hash
class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
    captcha = wtforms.StringField(validators=[Length(min=4,max=4,message="验证码格式错误")])
    username = wtforms.StringField(validators=[Length(min=3,max=30,message="用户名格式错误")])
    password = wtforms.StringField(validators=[Length(min=6,max=20,message="密码格式错误")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password",message="密码不一致")])

    def validate_email(self,field):
        email = field.data
        user = User.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已经注册过了")

    def validate_captcha(self,field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptcha.query.filter_by(email=email,captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(message="邮箱或验证码错误")
        # else:
        #
        #     db.session.delete(captcha_model)
        #     db.session.commit()

# class SignInForm(wtforms.Form):
#     email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
#     password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误")])
#     def validate_email(self,field):
#         email = field.data
#         user = User.query.filter_by(email=email).first()
#         if(not user):
#             raise wtforms.ValidationError(message="用户名不存在")
#
#     def validate_password(self,field):
#         password = field.data
#         user = User.query.filter_by(email=self.email).first()
#         if(not check_password_hash(password,user.password)):
#             raise wtforms.ValidationError(message="密码错误")

class SignInForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误")])