import json
import os
import random
import string
from flask_migrate import Migrate
import config
from models import User
from flask import Flask,request,jsonify,render_template,redirect,url_for,session
from verify import RegisterForm,SignInForm
from exts import db,mail
from flask_cors import CORS
from flask_mail import Message
from models import EmailCaptcha
from werkzeug.security import check_password_hash,generate_password_hash
app = Flask(__name__)
CORS(app,supports_credentials=True)
#绑定配置文件
app.config.from_object(config)

db.init_app(app)


mail.init_app(app)
migrate = Migrate(app,db)
@app.route('/admin')
def admin():
    return render_template('admin.html')
@app.route('/mail_test')
def mail_test():
    message = Message(subject="test mail", recipients=["lsy110119120@outlook.com"], body="djslkdjf")
    mail.send(message)
    return "success"
@app.route('/login')
def login():
    return render_template("login.html")
@app.route('/recognize',methods=['GET','POST'])
def recognize():
    return render_template('recognize.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/index')
def index():
    # if not session.get("user_name"):
    #     return "error"
    # else:
        return render_template("index.html")
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/sign_in',methods=['POST','GET'])
def sign_in():
    if request.method=="GET":
        return render_template("sign-in.html")
    else:
        form = SignInForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if check_password_hash(user.password,password):
                print("登录成功")
                return redirect(url_for("index"))
            else:
                return "密码错误"
        else:
            print(form.errors)
            return "errors"

@app.route('/sign_up',methods=['POST','GET'])
def sign_up():
    print(request.method)
    print(request.form.get('email'))
    if request.method=="GET":
        return render_template('sign-up.html')

    form = RegisterForm(request.form)
    print(form.email.data)
    print(form.password.data)
    print("hello")
    if form.validate():
        print("valicate success")
        email = form.email.data
        username = form.username.data
        password = form.password.data
        user = User(email=email, username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        print(email, password)
        return render_template("sign-in.html")
    else:
        print(form.errors)
        return "error"
@app.route('/get_captcha')
def get_captcha():

    email = request.args.get("email")
    source = string.digits*4
    captcha = random.sample(source,4)
    captcha = "".join(captcha)
    email_captcha = EmailCaptcha(email=email,captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    message = Message(subject="农业害虫识别系统注册验证码",recipients=[email],body=f'您的验证码是{captcha}')
    mail.send(message)
    print(email)
    print(captcha)
    return "success"

@app.route('/user_login',methods=['POST',"GET"])
def user_login():
    data = request.get_data()
    data = json.loads(data)
    username = data.get('username')
    password = data.get('password')
    captcha = data.get('captcha')
    user_in_database = User.query.filter_by(username= username)[0]
    if username==user_in_database.username and password == user_in_database.password:
        print("ok")
        session["user_name"]=user_in_database.username
        return "success"
    return "error"
@app.route('/upload',methods=['POST','GET','PUT'])
def upload():
    file = request.files.get('file')
    filename = file.filename
    path ="./static/images"+filename
    file.save(path)
    #result = recognize(filename)
    return jsonify({"jsldf":"jlskjdf"})

def table_data_get():
    result =[{}]
    users = User.query.all()
    for i,k in enumerate(users):
        result[i]["id"] = k.id
        result[i]["username"]=k.username
        result[i]["email"]=k.email
        result.append({})
    result.pop()

    return result

@app.route('/table_data')
def table_data():
    data = table_data_get()
    data_json={
        "code": 0,
        "msg": "",
        "count": 1000,
        "data": data}
    return jsonify(data_json)

@app.route('/test_table')
def test_table_data():
    result =[{}]
    users = User.query.all()
    for i,k in enumerate(users):
        result[i]["id"]=str(k.id)
        result[i]["username"]=k.username
        result[i]["email"]=k.email
        result.append({})
    result.pop()
    result = jsonify(result)
    print(result)


    return result

@app.route('/del_row',methods=["POST","GET"])
def del_row():
    email = (request.get_data()).decode("utf-8")
    print(email,type(email))
    user = User.query.filter_by(email=email).first()
    print(user)
    db.session.delete(user)
    db.session.commit()
    return "success"
@app.route('/add_table_user',methods=["GET","POST"])
def add_table_user():
    data = request.get_json()
    print(data,type(data))
    username = data['username']
    email = data['email']
    password = data['password']
    user = User(email=email, username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return "success"
if __name__ == '__main__':
    app.run()
