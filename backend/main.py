import os
import json
import http.client

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db.init_app(app)

@app.route('/')
def main():
    return 'running'

@app.route('/test/<name>/<passwd>')
def test(name, passwd):
    db.session.add(UserTable(name, passwd))
    db.session.commit()
    return name, passwd
