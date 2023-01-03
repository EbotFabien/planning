
import xlrd
import sqlite3



con = sqlite3.connect('cmd1.db')


def doc():
    #with app.app_context():
    cursorObj = con.cursor()
    loc="/work/www/cmd/Flask_app/project/app/static/appointment_documents.xls"
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
            'comment':name[3],
            'user':int(name[2]),
        }
        user=json['user']
        #check=requests.get("http://195.15.228.250/manager_app/user/"+str(user), headers={"Authorization":request.headers["Authorization"]})
        #try:
        #if check.json()['id']:
        rdv=json['rdv']
        tp=json['type']
        comme=json['route']
        comment=json['comment']
        entities=(user,rdv,comme,tp,comment)
        cursorObj.execute('INSERT INTO document(user_id, rdv_id,route,Type,comment) VALUES(?, ?, ?,?,?)', entities)
        con.commit()
    
    cursorObj.close()
    con.close()
        


def pic():
    #with app.app_context():
    loc="/work/www/cmd/Flask_app/project/app/static/appointment_photos.xls"
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    sheet.cell_value(0,0)
    for i in range(0,141):
        name=sheet.row_values(i+1)
        inv=name[4][::-1]
        url=inv[0:inv.index('/')]
        url="/work/fichiers/appointments/photos/" + url[::-1]
        json={
            'rdv':int(name[1]),
            'type':'Photos',
            'route':url,
            'comment':name[3],
            'user':int(name[2]),
        }
        user=json['user']
        #check=requests.get("http://195.15.218.172/manager_app/user/"+str(user), headers={"Authorization":request.headers["Authorization"]})
        #if #check.json()['id']:
        rdv=json['rdv']
        tp=json['type']
        comme=json['route']
        comment=json['comment']
        entities=(user,rdv,comme,tp,comment)
        cursorObj.execute('INSERT INTO document(user_id, rdv_id,route,Type,comment) VALUES(?, ?, ?,?,?)', entities)
        con.commit()
        print(i)
    
    cursorObj.close()
    con.close()

def comment():
    with app.app_context():
        loc="/work/www/cmd/Flask_app/project/app/static/appointment_comments.xls"
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        
        sheet.cell_value(0,0)
        for i in range(0,4807):
            name=sheet.row_values(i+1)
            json={
                'rdv':int(name[1]),
                'comment':name[3],
                'user':int(name[2]),
            }
            user=json['user']
            #check=requests.get("http://195.15.218.172/manager_app/user/"+str(user), headers={"Authorization":request.headers["Authorization"]})
            #if #check.json()['id']:
            rdv=request.json['rdv']
            comme=request.json['comment']
            entities=(user,rdv,comme)
            cursorObj.execute('INSERT INTO comment(user_id, rdv_id,contenu) VALUES(?, ?, ?)', entities)
            con.commit()
            print(i)
    
    cursorObj.close()
    con.close()

pic()
print("first step")
comment()
print(23)