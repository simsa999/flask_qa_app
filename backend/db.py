from flask_cors import CORS, cross_origin
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from flask_bcrypt import Bcrypt


import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

"""       Om det inte fungerar att skapa databasen, testa att lägga till ett '/' i slutet av 'sqlite:///'.         """
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
app.config['CORS_HEADERS'] = 'Content-Type'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
