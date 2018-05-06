import os
import json
import datetime

from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
CORS(app)

db.init_app(app)

@app.route('/user/register', methods=['GET', 'POST'])
def register_user():
    #name = request.form.get('name')
    #login = request.form.get('login')
    #password = request.form.get('password')
    #confirm_password = request.form.get('confirmed_password')
    data = request.json
    name = data['name']
    login = data['login']
    password = data['password']
    confirm_password = data['confirmed_password']

    user = UserTable.query.filter_by(login=login).first()

    if user:
        return 'login already exists'
    elif password != confirm_password:
        return 'passwords does not match'
    else:
        db.session.add(UserTable(name, login, password))
        db.session.commit()
        return 'success'

@app.route('/login', methods=['GET', 'POST'])
def login():
    #login = request.form.get('user')
    #password = request.form.get('password')
    data = request.json
    login = data['login']
    password = data['password']

    user = UserTable.query.filter_by(login=login).first()

    if not user:
        return json.dumps({'status': 1, 'message': 'invalid login', 'date': datetime.datetime.now().isoformat()})

    if user.password == password:
        return 'success'
    else:
        return 'Wrong password'

@app.route('/issue/add', methods=['GET', 'POST'])
def add_issue():
    #user = request.form.get('user')
    #title = request.form.get('title')
    #description = request.form.get('description')
    data = request.json
    user = data['login']
    title = data['title']
    description = data['description']

    issue = IssueTable.query.filter_by(title=title).first()

    if issue:
        return 'an issue with this title already exists'
    else:
        creator_id = UserTable.query.filter_by(login=user).first().id
        db.session.add(IssueTable(title, description, creator_id, None, datetime.datetime.now(), 0, 0))
        db.session.commit()
        return json.dumps({'status': 0, 'message': 'success'})

@app.route('/issue/update', methods=['GET', 'POST'])
def update_issue():
    #issue_id = request.form.get('issue_id')
    #title = request.form.get('title')
    #description = request.form.get('description')
    data = request.json
    issue_id = data['issue_id']
    title = data['title']
    description = data['description']

    issue = IssueTable.query.filter_by(id=issue_id).first()
    issue.title = title
    issue.description = description

    db.session.commit()

    return 'success'

@app.route('/solution/add', methods=['GET', 'POST'])
def add_solution():
    #login = request.form.get('user')
    #issue_id = request.form.get('issue_id')
    #description = request.form.get('description')
    data = request.json
    login = data['login']
    issue_id = data['issue_id']
    description = data['description']

    user = UserTable.query.filter_by(login=login).first()
    issue = IssueTable.query.filter_by(id=issue_id).first()

    issue.user_solver_id = user.id
    db.session.add(SolutionTable(description, user.id, issue_id, datetime.datetime.now(), 0, 0))
    db.session.commit()

    return 'success'

@app.route('/issue/update/upvote', methods=['GET', 'POST'])
def upvote_issue():
    #user = request.form.get('user')
    #issue_id = request.form.get('issue_id')
    data = request.json
    user = data['login']
    issue_id = data['issue_id']

    user = UserTable.query.filter_by(login=user).first()
    issue = IssueTable.query.filter_by(id=issue_id).first()
    issue_vote = VoteIssueTable.query.filter_by(user_id=user.id, issue_id=issue_id).first()

    if issue_vote:
        if not issue_vote.isupvote:
            issue.down_votes -= 1
            issue_vote.isupvote = True
        else:
            return 'success vini'
    else:
        db.session.add(VoteIssueTable(user.id, issue_id, True))

    issue.up_votes += 1

    db.session.commit()

    return 'success'

@app.route('/issue/update/downvote', methods=['GET', 'POST'])
def downvote_issue():
    #user = request.form.get('user')
    #issue_id = request.form.get('issue_id')
    data = request.json
    user = data['login']
    issue_id = data['issue_id']

    user = UserTable.query.filter_by(login=user).first()
    issue = IssueTable.query.filter_by(id=issue_id).first()
    issue_vote = VoteIssueTable.query.filter_by(user_id=user.id, issue_id=issue_id).first()

    if issue_vote:
        if issue_vote.isupvote:
            issue.up_votes -= 1
            issue_vote.isupvote = False
        else:
            return 'success vini'
    else:
        db.session.add(VoteIssueTable(user.id, issue_id, False))

    issue.down_votes += 1

    db.session.commit()

    return 'success'

@app.route('/solution/update/upvote', methods=['GET', 'POST'])
def upvote_solution():
    #user = request.form.get('user')
    #solution_id = request.form.get('solution_id')
    data = request.json
    user = data['login']
    solution_id = data['solution_id']

    user = UserTable.query.filter_by(login=user).first()
    solution = SolutionTable.query.filter_by(id=solution_id).first()
    #solution_vote = VoteSolutionTable.query.filter_by(user_id=user.id, solution_id=solution_id).first()
    solution_vote = VoteSolutionTable.query.filter_by(user_id=user.id, solution_id=solution_id).first()

    if solution_vote:
        if not solution_vote.isupvote:
            solution.down_votes -= 1
            solution_vote.isupvote = True
        else:
            return 'success vini'
    else:
        db.session.add(VoteSolutionTable(user.id, solution_id, True))

    solution.up_votes += 1

    db.session.commit()

    return 'success'

@app.route('/solution/update/downvote', methods=['GET', 'POST'])
def downvote_solution():
    #user = request.form.get('user')
    #solution_id = request.form.get('solution_id')
    data = request.json
    user = data['login']
    solution_id = data['solution_id']

    user = UserTable.query.filter_by(login=user).first()
    solution = SolutionTable.query.filter_by(id=solution_id).first()
    solution_vote = VoteSolutionTable.query.filter_by(user_id=user.id, solution_id=solution_id).first()

    if solution_vote:
        if solution_vote.isupvote:
            solution.up_votes -= 1
            solution_vote.isupvote = False
        else:
            return 'success vini'
    else:
        db.session.add(VoteSolutionTable(user.id, solution_id, False))

    solution.down_votes += 1

    db.session.commit()

    return 'success'
