from flask import current_app

import jwt, uuid, os
from datetime import datetime
from app import db
from flask_login import UserMixin
from sqlalchemy import ForeignKeyConstraint,ForeignKey,UniqueConstraint
from sqlalchemy.dialects.mysql import TIME



class comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer)
    rdv_id=db.Column(db.Integer)
    contenu=db.Column(db.String)
    date = db.Column(db.DateTime(),default=datetime.utcnow)
    

    def __repr__(self):
        return '<comment %r>' %self.id


class document(db.Model):
    __tablename__ = 'document'

    id = db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer)
    rdv_id=db.Column(db.Integer)
    Type=db.Column(db.String)
    route=db.Column(db.String)
    comment=db.Column(db.String) 
    date = db.Column(db.DateTime(),default=datetime.utcnow)
    visibility =db.Column(db.Boolean,default=True)
    

    def __repr__(self):
        return '<document %r>' %self.id