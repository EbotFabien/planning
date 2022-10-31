import os

class Config:
    SECRET_KEY='FABIENCLASSIC'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///cmd.db'
    MAIL_SERVER ='mail.infomaniak.ch'
    MAIL_PORT = 587
    MAIL_USE_TLS =True
    MAIL_USERNAME = 'noreply@amexpert.pro'
    MAIL_PASSWORD = 'TooR1234$'
    UPLOAD_FOLDER=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    CORS_HEADERS= 'Content-Type'












class Development(Config):
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 8000

class Production(Config):
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 80


config = {
    'dev': Development,
    'prod': Production,
    'default': Development
}
