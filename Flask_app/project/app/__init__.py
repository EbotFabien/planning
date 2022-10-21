from flask import Flask, render_template, url_for,flash,redirect,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import  LoginManager
from flask_mail import Mail
from app.config import Config
import os
from firebase_admin import credentials, firestore, initialize_app
# Initialize Flask App

# Initialize Firestore DB



db=SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
   

    from app.entity.clefs.routes import clefs
    from app.entity.comment.routes import omment
    from app.entity.document.routes import doct
   
    
    
    app.register_blueprint(clefs)
    app.register_blueprint(omment)
    app.register_blueprint(doct)
    
    


    return app