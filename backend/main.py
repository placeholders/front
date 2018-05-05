import os
import json
import http.client

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def main():
    return 'test'
