from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

import os

#from db import app, db
from RoutesPackage import *

    
if __name__ == '__main__': 
    with app.app_context():
        db.create_all()   
    app.run(debug=True, port = 5001)

def create_app():
    with app.app_context():
        db.create_all() 
    return app  

    
    