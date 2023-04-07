from flask import Flask
from flask_mysqldb import MySQL
app = Flask(__name__)
# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'     #用户名
app.config['MYSQL_PASSWORD'] = 'Admin123!'  #密码
app.config['MYSQL_DB'] = 'warehouse'   #创建数据库
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


