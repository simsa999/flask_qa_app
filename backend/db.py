##########################################
#                                        #
#               Company 4                #
#    Flask Application Configuration     #
#                                        #
##########################################


from flask_cors import CORS, cross_origin
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from flask_bcrypt import Bcrypt
from celery import Celery


import os

#Create config for app

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
CORS(app, max_age=300, resources={r"/api/*": {"origins": "*"}})
#app.config['CORS_HEADERS'] = 'Content-Type'
#CORS_MAX_AGE = 600

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#Create path for celery variable from its module
from RedisCeleryConfig import celery
