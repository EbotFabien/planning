from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import bcrypt,db,create_app
import requests
import json
from app.entity.clefs.utils import send_email
from app.models import tarifs
from os.path import join, dirname, realpath
import os
from flask_cors import CORS,cross_origin








tarif=Blueprint('tarif',__name__)

app= create_app()

@cross_origin(origin='127.0.0.1',headers=['Content- Type','Authorization'])
@tarif.route('/all/tarif/', methods=['GET'])
def tar():
    start=request.args.get('start')
    count=request.args.get('count')
    user=request.args.get('user')
    commen=tarifs.query.filter_by(user_id=str(user))
    comment=commen.paginate(int(start),int(count),False)
    nx=str(comment.next_num)
    previous="http://195.15.218.172/cmdplannif/all/tarif/+?start="+start+"&count="+count+"&user="+user
    next="http://195.15.218.172/cmdplannif/all/tarif/+?start="+nx+"&count="+count+"&user="+user
    total=(comment.total/int(count))
    all_=[]
    for i in comment.items:
        json={
            "id":i.id,
            "user_id":i.user_id,
            "name":i.name,
            "Type":i.Type,
            "comment":i.comment,
            "price":i.price,
            "created":i.created,
            "comment":i.comment,
            "updated":i.updated
        }
        all_.append(json)

    return jsonify({"start":start,"count":count,"next":next,"previous":previous,"Total":total,"document":all_}), 200

@tarif.route('/make/tarif/', methods=['POST'])
def make_tarif():

    loc="prices.json"
    f = open(loc,)
    fil=json.load(f)
    for i in fil[2]["data"]:
        commen=tarifs(user_id=i["customer_id"],price=i["price_ht"],name=i["name"],Type=i["type"],created=i["created_at"],comment=i["comments"],updated=i["updated_at"])
        db.session.add(commen)
        db.session.commit()
    return jsonify({"tarifs": 'made'}), 200




