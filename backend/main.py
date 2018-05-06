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

    user = UserTable.query.filter_by(login=login).first()

    if user:
        return 'login already exists'
    elif password != confirm_password:
        return 'passwords does not match'
    else:
        db.session.add(UserTable(name, login, password))
        db.session.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
    login = request.form.get('user')
    password = request.form.get('password')

    user = UserTable.query.filter_by(login=login).first()

    if not user:
        return json.dumps({'status': 1, 'message': 'invalid login'})

    if user.password == password:
        return 'success'
    else:
        return 'Wrong password'

@app.route('/issue/add', methods=['GET', 'POST'])
def add_issue():
    return login + ' ' + description

