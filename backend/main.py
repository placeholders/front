import os
import json

from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db.init_app(app)

@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/user/register', methods=['GET', 'POST'])
def register_user():
    name = request.form.get('name')
    login = request.form.get('login')
    password = request.form.get('password')
    confirm_password = request.form.get('confirmed_password')
    #db.session.add(TestTable(name))
    #db.session.commit()
    return name + ' ' + login + ' ' + password + ' ' + confirm_password


@app.route('/login', methods=['GET', 'POST'])
def login():
    user = request.form.get('user')
    password = request.form.get('password')
    #db.session.add(TestTable(name))
    #db.session.commit()
    return user + ' ' + password;

@app.route('/issue/add', methods=['GET', 'POST'])
def add_issue():
    return login + ' ' + description
