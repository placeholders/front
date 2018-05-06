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
    title = db.Column(db.String())
    description = db.Column(db.String())
    user_creator_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    user_solver_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    created_date = db.Column(db.Date())
    up_votes = db.Column(db.Integer())
    down_votes = db.Column(db.Integer())

    # relationships
    creator = db.relationship('UserTable', foreign_keys=user_creator_id)
    solver = db.relationship('UserTable', foreign_keys=user_solver_id)

    def __init__(self, title, description, user_creator_id, user_solver_id, created_date, up_votes, down_votes):
        self.title = title
        self.description = description
        self.user_creator_id = user_creator_id
        self.user_solver_id = user_solver_id
        self.created_date = created_date
        self.up_votes = up_votes
        self.down_votes = down_votes


class SolutionTable(db.Model):
    __tablename__ = 'solution'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    description = db.Column(db.String())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    issue_id = db.Column(db.Integer(), db.ForeignKey('issue.id'))
    solved_date = db.Column(db.Date())
    up_votes = db.Column(db.Integer())
    down_votes = db.Column(db.Integer())

    # relationships
    user = db.relationship('UserTable')
    issue = db.relationship('IssueTable')

    def __init__(self, description, user_id, issue_id, solved_date, up_votes, down_votes):
        self.description = description
        self.user_id = user_id
        self.issue_id = issue_id
        self.solved_date = solved_date
        self.up_votes = up_votes
        self.down_votes = down_votes

class VoteIssueTable(db.Model):
    __tablename__ = 'vote_issue'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    issue_id = db.Column(db.Integer(), db.ForeignKey('issue.id'))
    isupvote = db.Column(db.Boolean())

    # relationships
    user = db.relationship('UserTable')
    issue = db.relationship('IssueTable')

    def __init__(self, user_id, issue_id, isupvote):
        self.user_id = user_id
        self.issue_id = issue_id
        self.isupvote = isupvote

class VoteSolutionTable(db.Model):
    __tablename__ = 'vote_solution'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    solution_id = db.Column(db.Integer(), db.ForeignKey('solution.id'))
    isupvote = db.Column(db.Boolean())

    # relationship
    user = db.relationship('UserTable')
    solution = db.relationship('SolutionTable')

    def __init__(self, user_id, solution_id, isupvote):
        self.user_id = user_id
        self.solution_id = solution_id
        self.isupvote = isupvote
