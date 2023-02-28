from exts import db

from flask_migrate import Migrate



class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(30))
    username = db.Column(db.String(30))
    password = db.Column(db.String(200))


class EmailCaptcha(db.Model):
    __tablename__ = 'emailcaptcha'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(30))
    captcha = db.Column(db.String(5))
