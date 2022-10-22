from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import bcrypt,db
import requests
import json
from app.entity.clefs.utils import send_email
from app.models import comment








omment=Blueprint('comment',__name__)


@omment.route('/all/comment/', methods=['GET'])
def commen():
    ide=request.args.get('rdv')
    commen=comment.query.filter_by(rdv_id=ide).all()
    all_=[]
    for i in commen:
        json={
            "id":i.id,
            "user_id":i.user_id,
            "rdv_id":i.rdv_id,
            "contenu":i.contenu,
            "date":i.date
        }
        all_.append(json)

    return jsonify({"comment":all_}), 200

@omment.route('/<int:ide>/comment/', methods=['POST'])
def commen_spe(ide):

    commen=comment.query.filter_by(id=ide).first()
    all_=[]
    json={
            "id":commen.id,
            "user_id":commen.user_id,
            "rdv_id":commen.rdv_id,
            "contenu":commen.contenu,
            "date":commen.date
        }
    all_.append(json)
    return jsonify({"comment": commen}), 200

@omment.route('/make/comment/', methods=['POST'])
def commen_make():
    rdv=request.json['rdv']
    user=request.json['user']
    comme=request.json['comment']
    commen=comment(user_id=user,rdv_id=rdv,contenu=comme)
    db.session.add(commen)
    db.session.commit()

    return jsonify({"status": "comment sent"}), 200

