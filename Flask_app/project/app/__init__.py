from flask import Flask, render_template, url_for,flash,redirect,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import  LoginManager
from flask_mail import Mail
from app.config import Config
import os
from firebase_admin import credentials, firestore, initialize_app
from flask_cors import CORS
# Initialize Flask App

# Initialize Firestore DB



db=SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    #return response
    app.config.from_object(Config)
    CORS(app, resources=r'/api/*') 	
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
   

    from app.entity.clefs.routes import clefs
    from app.entity.comment.routes import omment
    from app.entity.document.routes import doct
    from app.entity.tarif.routes import tarif
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    
    app.register_blueprint(clefs)
    app.register_blueprint(omment)
    app.register_blueprint(doct)
    app.register_blueprint(tarif)
    
    


    return app
