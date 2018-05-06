import os
import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class TestTable(db.Model):
    __tablename__ = 'test'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

@app.route('/')
def login_page():
    return render_template("login");

@app.route('/register/user/<name>/<user>/<password>/<confirm_password>')
def register_user(name, user, password, confirm_password):
    #db.session.add(TestTable(name))
    #db.session.commit()
    return name+" "+user+" "+password+" "+confirm_password

@app.route('/login/<user>/<password>')
def login(name, user, password):
    #db.session.add(TestTable(name))
    #db.session.commit()
    return user+" "+password;
