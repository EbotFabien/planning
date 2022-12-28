from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import bcrypt,db,create_app
import requests
import json
from app.entity.clefs.utils import send_email
from app.models import document
from os.path import join, dirname, realpath
import os
from flask_cors import CORS,cross_origin
import xlrd
import requests
from time import sleep









doct=Blueprint('doct',__name__)

app= create_app()

@doct.route('/all/document/', methods=['GET'])
def commen():
    ide=request.args.get('rdv')
    comment=document.query.filter_by(rdv_id=ide).all()
    all_=[]
    for i in comment:
        json={
            "id":i.id,
            "user_id":i.user_id,
            "rdv_id":i.rdv_id,
            "Type":i.Type,
            "comment":i.comment,
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
            "id":comment.id,
            "user_id":comment.user_id,
            "rdv_id":comment.rdv_id,
            "Type":comment.Type,
            "comment":comment.comment,
            "route":comment.route,
            "date":comment.date
        }
    all_.append(json)
    return jsonify({"document": all_}), 200

@cross_origin(origin=['http://127.0.0.1',"http://195.15.218.172"],headers=['Content- Type','Authorization'])
@doct.route('/delete/document/', methods=['DELETE'])
def dele():
    ide=int(request.json['ide'])
    comment=document.query.filter_by(id=ide).delete()
    db.session.commit()
    return jsonify({"status": "document deleted"}), 200


@doct.route('/make/document/', methods=['POST','PUT'])
def make_document():
    user=request.form['user']
    check=requests.get("http://195.15.218.172/manager_app/user/"+str(user), headers={"Authorization":request.headers["Authorization"]})
    #try:
    if check.json()['id']:
            uploaded_file = request.files['fichier']
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            comme=str(file_path)
            uploaded_file.save(file_path)
            rdv=request.form['rdv']
            tp=request.form['type']
            comment=request.form['comment']
            commen=document(user_id=user,rdv_id=rdv,route=comme,Type=tp,comment=comment)
            db.session.add(commen)
            db.session.commit()

    return jsonify({"status": "document sent"}), 200
    #except:
        #return jsonify({"Fail": "donnee n'exist pas or token n'existe pas"}), 403


@cross_origin(origin=['http://127.0.0.1',"http://195.15.218.172"],headers=['Content- Type','Authorization'])
@doct.route('/make/doc/', methods=['POST','PUT'])
def make_doc():
    loc="/Users/pro2015/Desktop/pph folder/cmd/Flask_app/project/app/static/appointment_documents.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    sheet.cell_value(0,0)
    for i in range(0,20281):
        name=sheet.row_values(i+1)
        inv=name[5][::-1]
        url=inv[0:inv.index('/')]
        url="/work/fichiers/appointments/documents/" + url[::-1]
        json={
            'rdv':int(name[1]),
            'type':'Fichier',
            'route':url,
            'comment':name[4],
            'user':int(name[2]),
        }
        user=json['user']
        check=requests.get("http://195.15.218.172/manager_app/user/"+str(user), headers={"Authorization":request.headers["Authorization"]})
        #try:
        if check.json()['id']:
                rdv=json['rdv']
                tp=json['type']
                comme=json['route']
                comment=json['comment']
                commen=document(user_id=user,rdv_id=rdv,route=comme,Type=tp,comment=comment)
                db.session.add(commen)
                db.session.commit()
    loc="/Users/pro2015/Desktop/pph folder/cmd/Flask_app/project/app/static/appointment_photos.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    sheet.cell_value(0,0)
    for i in range(0,141):
        name=sheet.row_values(i+1)
        inv=name[5][::-1]
        url=inv[0:inv.index('/')]
        url="/work/fichiers/appointments/photos/" + url[::-1]
        json={
            'rdv':int(name[1]),
            'type':'Photos',
            'route':url,
            'comment':name[4],
            'user':int(name[2]),
        }
        user=json['user']
        check=requests.get("http://195.15.218.172/manager_app/user/"+str(user), headers={"Authorization":request.headers["Authorization"]})
        if check.json()['id']:
                rdv=json['rdv']
                tp=json['type']
                comme=json['route']
                comment=json['comment']
                commen=document(user_id=user,rdv_id=rdv,route=comme,Type=tp,comment=comment)
                db.session.add(commen)
                db.session.commit()
    
    return jsonify({"Fail": "donnee n'exist pas or token n'existe pas"}), 200
