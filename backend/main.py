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
    user = request.form.get('user')
    title = request.form.get('title')
    description = request.form.get('description')
    #don't forget to add line in votes_issue
    return user +" "+title+" "+description

@app.route('/issue/update', methods=['GET', 'POST'])
def update_issue():
    issue_id = request.form.get('issue_id')
    title = request.form.get('title')
    description = request.form.get('description')
    return issue_id +" "+title+" "+description

@app.route('/solution/add', methods=['GET', 'POST'])
def add_solution():
    user = request.form.get('user')
    issue_id = request.form.get('issue_id')
    description = request.form.get('description')
    #update issue table too
    #don't forget to add line in votes_solution
    return issue_id +" "+title+" "+description

@app.route('/issue/update/upvote', methods=['GET', 'POST'])
def upvote_issue():
    user = request.form.get('user')
    issue_id = request.form.get('issue_id')
    #don't forget to update line in votes_issues
    return issue_id +" "+title+" "+description

@app.route('/issue/update/downvote', methods=['GET', 'POST'])
def downvote_issue():
    user = request.form.get('user')
    issue_id = request.form.get('issue_id')
    #don't forget to update line in votes_issues
    return issue_id +" "+title+" "+description

@app.route('/solution/update/upvote', methods=['GET', 'POST'])
def upvote_solution():
    user = request.form.get('user')
    solution_id = request.form.get('solution_id')
    #don't forget to update line in votes_solutions
    return issue_id +" "+title+" "+description

@app.route('/solution/update/downvote', methods=['GET', 'POST'])
def downvote_solution():
    user = request.form.get('user')
    solution_id = request.form.get('solution_id')
    #don't forget to update line in votes_solutions
    return issue_id +" "+title+" "+description
