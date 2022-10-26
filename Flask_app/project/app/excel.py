import xlrd
import openpyxl
from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify

def worklo():
    loc="Book(notif).xlsx"
    wb = openpyxl.load_workbook(loc)
    dataset=[{
        "creation":[],
        "modification":[],
        "suppression":[],
    }]
    loader=["creation","modification","suppression"]
    for load in loader:
        sheet = wb[load]
        
        
        for i in range(1,int(sheet.max_row)):
            dataset[0][load].append({"user":sheet["A"][i].value,"sujet":sheet["B"][i].value,"message":sheet["C"][i].value})
            
           

    print(dataset)     



worklo()