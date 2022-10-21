from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import bcrypt,db
import requests
import json
from app.entity.clefs.utils import send_email
from app.models import document








doct=Blueprint('doct',__name__)


@doct.route('/all/document/', methods=['GET'])
def commen():

    comment=document.query.all()

    return jsonify({"document": comment}), 200

@doct.route('/<int:ide>/document/', methods=['POST'])
def commen_spe(ide):

    comment=document.query.filter_by(id=ide).first()

    return jsonify({"document": comment}), 200