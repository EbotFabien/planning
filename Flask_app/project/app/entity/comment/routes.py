from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import bcrypt,db
import requests
import json
from app.entity.clefs.utils import send_email
from app.models import comment
from flask_cors import CORS,cross_origin




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

@cross_origin(origin=['http://127.0.0.1',"http://195.15.228.250"],headers=['Content- Type','Authorization'])
@omment.route('/<int:ide>/delete/comment/', methods=['DELETE'])
def commen_sp(ide):
    comment=comment.query.filter_by(id=ide).delete()
    db.session.commit()
    return jsonify({"status": "comment deleted"}), 200

@cross_origin(origin=['http://127.0.0.1',"http://195.15.228.250"],headers=['Content- Type','Authorization'])
@omment.route('/<int:ide>/modify/comment/', methods=['PUT','POST'])
def commen_md(ide):
    comme=request.json['comment']
    comment=comment.query.filter_by(id=ide).first()
    comment.contenu=comme
    db.session.commit()
    return jsonify({"status": "comment modfied"}), 200


@cross_origin(origin=['http://127.0.0.1',"http://195.15.228.250"],headers=['Content- Type','Authorization'])
@omment.route('/make/comment/', methods=['POST'])
def commen_make():
    user=request.json['user']
    
    check=requests.get("http://195.15.228.250/manager_app/user/"+str(user), headers={"Authorization":request.headers["Authorization"]})
    
    try:
        if check.json()['id']:
            rdv=request.json['rdv']
            comme=request.json['comment']
            commen=comment(user_id=user,rdv_id=rdv,contenu=comme)
            db.session.add(commen)
            db.session.commit()

        return jsonify({"status": "comment sent"}), 200
    except:
        return jsonify({"Fail": "donnee n'exist pas or token n'existe pas"}), 400


@cross_origin(origin=['http://127.0.0.1',"http://195.15.228.250"],headers=['Content- Type','Authorization'])
@omment.route('/comme/make/', methods=['POST','PUT'])
def make_com():
    loc="work/www/cmd/Flask_app/project/app/static/appointment_photos.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    sheet.cell_value(0,0)
    for i in range(0,4805):
        name=sheet.row_values(i+1)
        json={
            'rdv':int(name[1]),
            'comment':name[3],
            'user':int(name[2]),
        }
        user=json['user']
        rdv=json['rdv']
        comme=json['comment']
        date=name[4]
        commen=comment(user_id=user,rdv_id=rdv,contenu=comme)
        db.session.add(commen)
        db.session.commit()
    return jsonify({"Fail": "donnee n'exist pas or token n'existe pas"}), 200
