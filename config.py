USERNAME = "root"
PASSWORD="123456"
host = "localhost"
db_name = "flask_database"
SQLALCHEMY_DATABASE_URI= f"mysql+pymysql://{USERNAME}:{PASSWORD}@{host}/{db_name}"
SQLALCHEMY_COMMIT_ON_TEARDOWN= True
SECRET_KEY="abcdefgh"
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_DEFAULT_SENDER = "1848180030@qq.com"
MAIL_USERNAME = '1848180030@qq.com'
MAIL_PASSWORD = 'udhhwondlukxeeah'