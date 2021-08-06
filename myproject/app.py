from flask import Flask
from api import board
from db_connect import db
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.register_blueprint(board)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:qwerqwer123@127.0.0.1:3306/elice"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'asodfajsdofijac'

db.init_app(app)
bcrypt = Bcrypt(app)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
