from flask import Flask
from flask import abort, request, redirect
from flask import jsonify, json, url_for
from flask_sqlalchemy import SQLAlchemy
from models import *
from db import app
from datetime import datetime
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from flask_cors import CORS, cross_origin

import os

app.config['JWT_SECRET_KEY'] = 'CompanyC4'
app.secret_key = 'CompanyC4'
jwt = JWTManager(app)