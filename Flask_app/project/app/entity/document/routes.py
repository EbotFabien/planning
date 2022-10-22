from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import bcrypt,db
import requests
import json
from app.entity.clefs.utils import send_email
from app.models import document








doct=Blueprint('doct',__name__)


@doct.route('/all/document/', methods=['GET'])
def commen():
    ide=request.args.get('rdv')
    comment=document.query.filter_by(id=ide).all()
    all_=[]
    for i in commen:
        json={
            "id":i.id,
            "user_id":i.user_id,
            "rdv_id":i.rdv_id,
            "Type":i.Type,
            "route":i.route,
            "date":i.date
        }
        all_.append(json)

    return jsonify({"document":all_}), 200

@doct.route('/<int:ide>/document/', methods=['POST'])
def commen_spe(ide):

    comment=document.query.filter_by(id=ide).first()
    all_=[]
    json={
            "id":i.id,
            "user_id":i.user_id,
            "rdv_id":i.rdv_id,
            "Type":i.Type,
            "route":i.route,
            "date":i.date
        }
    all_.append(json)
    return jsonify({"document": all_}), 200