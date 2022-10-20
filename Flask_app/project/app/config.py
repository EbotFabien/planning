class Config:
    SECRET_KEY='FABIENCLASSIC'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///fabienflask.db'
    MAIL_SERVER ='mail.infomaniak.ch'
    MAIL_PORT = 587
    MAIL_USE_TLS =True
    MAIL_USERNAME = 'noreply@amexpert.pro'
    MAIL_PASSWORD = 'TooR123$'











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
