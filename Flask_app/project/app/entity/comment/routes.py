from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import bcrypt,db
import requests
import json
from app.entity.clefs.utils import send_email
from app.models import comment








omment=Blueprint('comment',__name__)


@omment.route('/all/comment/', methods=['GET'])
def commen():
    ide=request.get('rdv')
    commen=comment.query.filter_by(rdv_id=ide).all()

    return jsonify({"comment": commen}), 200

@omment.route('/<int:ide>/comment/', methods=['POST'])
def commen_spe(ide):

    commen=comment.query.filter_by(id=ide).first()

    return jsonify({"comment": commen}), 200

