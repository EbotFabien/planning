import xlrd
import openpyxl
from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
import json
from app import create_app,db

def worklo():
    loc="prices.json"
    f = open(loc,)
    fil=json.load(f)
    for i in fil[2]["data"]:
        print(i["id"])

        



worklo()