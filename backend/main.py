import os
import json
import http.client

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
def main():
    return 'test'

@app.route('/name/<name>')
def test(name):
    db.session.add(TestTable(name))
    db.session.commit()
    return name
