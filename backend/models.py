from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserTable(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    login = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

class IssueTable(db.Model):
    __tablename__ = 'issue'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    description = db.Column(db.String())
    user_creator_id = db.Column(db.Integer())
    user_solver_id = db.Column(db.Integer())

    def __init__(self, description, user_creator_id, user_solver_id):
        self.description = description
        self.user_creator_id = user_creator_id
        self.user_solver_id = user_solver_id


class ScoreTable(db.Model):
    __tablename__ = 'score'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    issue_id = db.Column(db.Integer())
    solution_id = db.Column(db.Integer())
    user_id = db.Column(db.Integer())
    upvotes = db.Column(db.Integer())
    downvotes = db.Column(db.Integer())

    def __init__(self, issue_id, solution_id, user_id, upvotes, downvotes):
        self.issue_id = issue_id
        self.solution_id = solution_id
        self.userid = userid
        self.upvotes = upvotes
        self.downvotes = downvotes

class SolutionTable(db.Model):
    __tablename__ = 'solution'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    description = db.Column(db.String())
    user_id = db.Column(db.Integer())
    issue_id = db.Column(db.Integer())

    def __init__(self, description, user_id, issue_id):
        self.description = description
        self.user_id = user_id
        self.issue_id = issue_id



