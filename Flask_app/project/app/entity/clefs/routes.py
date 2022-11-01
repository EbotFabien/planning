from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import bcrypt,db
import requests
import json
from app.entity.clefs.utils import send_email








clefs =Blueprint('clefs',__name__)

@clefs.route('/change/<int:ide>/rdv/', methods=['POST'])
def change(ide):
    rdv=requests.get("http://195.15.218.172/rdv_app/rdv/"+str(ide), headers={"Authorization":request.headers["Authorization"]})
    
    try:
        status=rdv.json()[0]['status']
    except:
        status=rdv.json()[0]['statut']

    if status == "not_logged":
        return jsonify({"Fail": "donnee n'exist pas"}), 400
    
    if status == 1:
        
        
        
        
        json={
                "nom_bailleur": rdv.json()[0]["propriete"]["bailleur"]["nom"],
                "prenom_bailleur": rdv.json()[0]["propriete"]["bailleur"]["prenom"],
                "email_bailleur": rdv.json()[0]["propriete"]["bailleur"]["email"],
                "reference_bailleur": rdv.json()[0]["propriete"]["bailleur"]["reference"],
                "nom_locataire": rdv.json()[0]["propriete"]["locataire"]["nom"],
                "prenom_locataire":True,#change back to string
                "email_locataire": rdv.json()[0]["propriete"]["locataire"]["nom"],
                "telephone_locataire": rdv.json()[0]["propriete"]["locataire"]["telephone"],
                "surface_propriete": rdv.json()[0]["propriete"]["surface"],
                "numero_propriete": rdv.json()[0]["propriete"]["numero"],
                "numero_parking_propriete": rdv.json()[0]["propriete"]["numeroParking"],
                "adresse_propriete": rdv.json()[0]["propriete"]["adresse"],
                "code_postal_propriete": rdv.json()[0]["propriete"]["codePostal"],
                "ville_propriete":rdv.json()[0]["propriete"]["ville"],
                "adresse_complementaire_propriete":rdv.json()[0]["propriete"]["adresseComplementaire"],
                "numero_cave_propriete": rdv.json()[0]["propriete"]["numeroCave"],
                "ref_lot":rdv.json()[0]["ref_lot"],
                "ref_edl": rdv.json()[0]["ref_rdv_edl"],
                "type": rdv.json()[0]["propriete"]["type"],
                "longitude": rdv.json()[0]["longitude"],
                "latitude": rdv.json()[0]["latitude"],
                "consignes_part": rdv.json()[0]["consignes_particuliere"],
                "list_documents": rdv.json()[0]["liste_document_recuperer"],
                "info_diverses": rdv.json()[0]["info_diverses"],
                "numero_sol_propriete":rdv.json()[0]["propriete"]["numeroSol"],
                "intervention":rdv.json()[0]["intervention"]["id"],
                "client":rdv.json()[0]["client"]["id"],
                "passeur":int(rdv.json()[0]["passeur"][0]["id"]),
                "agent":int(rdv.json()[0]["agent"]["id"]),
                "type_propriete":int(rdv.json()[0]["propriete"]["type_propriete"]["id"]),
                "date":rdv.json()[0]["date"]
                #"agent_constat": null,
                #"audit_planneur": null,

            }
        json["statut"]=2
        rdv=requests.put("http://195.15.218.172/rdv_app/rdv/"+str(ide),json=json,headers={"Authorization":request.headers["Authorization"]})

        return jsonify({"Rendez vous":rdv.json()}), 200
    else:
        return jsonify({"Status rdv":rdv.json()[0]['statut']}), 400


@clefs.route('/affectation/rdv/<int:ide>', methods=['POST', 'PUT'])
def update(ide):
        rdv=requests.get("http://195.15.218.172/rdv_app/rdv/"+str(ide), headers={"Authorization":request.headers["Authorization"]})

        try:
            status=rdv.json()['status']
        except:
            status=int(rdv.json()[0]['statut'])

        if status == "not_logged":
            return jsonify({"Fail": "donnee n'exist pas"}), 400
        if status == 2:
            
            json={
                "nom_bailleur": rdv.json()[0]["propriete"]["bailleur"]["nom"],
                "prenom_bailleur": rdv.json()[0]["propriete"]["bailleur"]["prenom"],
                "email_bailleur": rdv.json()[0]["propriete"]["bailleur"]["email"],
                "reference_bailleur": rdv.json()[0]["propriete"]["bailleur"]["reference"],
                "nom_locataire": rdv.json()[0]["propriete"]["locataire"]["nom"],
                "prenom_locataire":True,#change back to string
                "email_locataire": rdv.json()[0]["propriete"]["locataire"]["nom"],
                "telephone_locataire": rdv.json()[0]["propriete"]["locataire"]["telephone"],
                "surface_propriete": rdv.json()[0]["propriete"]["surface"],
                "numero_propriete": rdv.json()[0]["propriete"]["numero"],
                "numero_parking_propriete": rdv.json()[0]["propriete"]["numeroParking"],
                "adresse_propriete": rdv.json()[0]["propriete"]["adresse"],
                "code_postal_propriete": rdv.json()[0]["propriete"]["codePostal"],
                "ville_propriete":rdv.json()[0]["propriete"]["ville"],
                "adresse_complementaire_propriete":rdv.json()[0]["propriete"]["adresseComplementaire"],
                "numero_cave_propriete": rdv.json()[0]["propriete"]["numeroCave"],
                "ref_lot":rdv.json()[0]["ref_lot"],
                "ref_edl": rdv.json()[0]["ref_rdv_edl"],
                "type": rdv.json()[0]["propriete"]["type"],
                "longitude": rdv.json()[0]["longitude"],
                "latitude": rdv.json()[0]["latitude"],
                "consignes_part": rdv.json()[0]["consignes_particuliere"],
                "list_documents": rdv.json()[0]["liste_document_recuperer"],
                "info_diverses": rdv.json()[0]["info_diverses"],
                "numero_sol_propriete":rdv.json()[0]["propriete"]["numeroSol"],
                "intervention":rdv.json()[0]["intervention"]["id"],
                "client":rdv.json()[0]["client"]["id"],
                "passeur":int(rdv.json()[0]["passeur"][0]["id"]),
                "agent":int(rdv.json()[0]["agent"]["id"]),
                "type_propriete":int(rdv.json()[0]["propriete"]["type_propriete"]["id"]),
                "date":rdv.json()[0]["date"]
                #"agent_constat": null,
                #"audit_planneur": null,

            }
            json["statut"]=3
            #verify audit planneur and constat
            if request.json["constat"] != None:
                ag_con=requests.get("http://195.15.218.172/agent_app/agent/"+str(request.json["constat"]), headers={"Authorization":request.headers["Authorization"]})
                #do inserting of agent
                try:
                    status=ag_con.json()['status']
                except:
                    status=ag_con.json()[0]["user"]["group"]
                
                if status == "Agent constat":
                    json['agent_constat']=ag_con.json()[0]["id"]
                else:
                    return jsonify({"Status":"agent constat n'existe pas"}), 200

            else:
                json['agent_constat']=rdv.json()[0]['agent_constat']
            
            if request.json["planner"] != None:
                ag_con=requests.get("http://195.15.218.172/agent_app/agent/"+str(request.json["planner"]), headers={"Authorization":request.headers["Authorization"]})
                #do inserting of agent
                try:
                    status=ag_con.json()['status']
                except:
                    status=ag_con.json()[0]["user"]["group"]
                print(ag_con.json()[0]["user"]["group"])
                if status == "Audit planneur":
                    json['audit_planneur']=ag_con.json()[0]["id"]
                else:
                    return jsonify({"Status":"agent planneur n'existe pas"}), 200

            else:
                json['audit_planneur']=rdv.json()[0]['audit_planneur']
                
            
            rdv=requests.put("http://195.15.218.172/rdv_app/rdv/"+str(ide),json=json,headers={"Authorization":request.headers["Authorization"]})

            return jsonify({"Rendez vous":rdv.json()}), 200
        else:
            return jsonify({"Status rdv":rdv.json()[0]['statut']}), 400
            
    

@clefs.route('/modify/rdv/<int:ide>', methods=['POST', 'PUT',"GET"])
def modify(ide):
        #send_email("touchone0001@gmail.com")
        rdv=requests.get("http://195.15.218.172/rdv_app/rdv/"+str(ide), headers={"Authorization":request.headers["Authorization"]})
        
        
        try:
            status=rdv.json()['status']
        except:
            status=int(rdv.json()[0]['statut'])   
        if status == "not_logged":
            return jsonify({"Fail": "donnee n'exist pas or token n'existe pas"}), 400
        if status == 3:
            
            
            json={
                "nom_bailleur": rdv.json()[0]["propriete"]["bailleur"]["nom"],
                "prenom_bailleur": rdv.json()[0]["propriete"]["bailleur"]["prenom"],
                "email_bailleur": rdv.json()[0]["propriete"]["bailleur"]["email"],
                "reference_bailleur": rdv.json()[0]["propriete"]["bailleur"]["reference"],
                "nom_locataire": rdv.json()[0]["propriete"]["locataire"]["nom"],
                "prenom_locataire": true,#change back to string
                "email_locataire": rdv.json()[0]["propriete"]["locataire"]["nom"],
                "telephone_locataire": rdv.json()[0]["propriete"]["locataire"]["telephone"],
                "surface_propriete": rdv.json()[0]["propriete"]["surface"],
                "numero_propriete": rdv.json()[0]["propriete"]["numero"],
                "numero_parking_propriete": rdv.json()[0]["propriete"]["numeroParking"],
                "adresse_propriete": rdv.json()[0]["propriete"]["adresse"],
                "code_postal_propriete": rdv.json()[0]["propriete"]["codePostal"],
                "ville_propriete":rdv.json()[0]["propriete"]["ville"],
                "adresse_complementaire_propriete":rdv.json()[0]["propriete"]["adresseComplementaire"],
                "numero_cave_propriete": rdv.json()[0]["propriete"]["numeroCave"],
                "ref_lot":rdv.json()[0]["propriete"]["ref_lot"],
                "ref_edl": rdv.json()[0]["propriete"]["ref_rdv_edl"],
                "type": rdv.json()[0]["propriete"]["type"],
                "longitude": rdv.json()[0]["longitude"],
                "latitude": rdv.json()[0]["latitude"],
                "consignes_part": rdv.json()[0]["consignes_particuliere"],
                "list_documents": rdv.json()[0]["liste_document_recuperer"],
                "info_diverses": rdv.json()[0]["info_diverses"],
                "numero_sol_propriete":rdv.json()[0]["propriete"]["numeroSol"],
                "intervention":rdv.json()[0]["intervention"]["id"],
                "client":rdv.json()[0]["client"]["id"],
                "passeur":rdv.json()[0]["passeur"]["id"],
                "agent":rdv.json()[0]["agent"]["id"],
                "type_propriete":rdv.json()[0]["type_propriete"]["id"]
                #"agent_constat": null,
                #"audit_planneur": null,

            }
            json["statut"]=3
            
            if request.json["date"]== '':#control date
                json["date"]=rdv.json()[0]["date"]
            else:
                json["date"]=request.json["date"]
            #verify audit planneur and constat
            if request.json["constat"] != None:
                ag_con=requests.get("http://195.15.218.172/agent_app/agent/"+int(request.json["constat"]), headers={"Authorization":request.headers["Authorization"]})
                #do inserting of agent
                try:
                    status=ag_con.json()['status']
                except:
                    status=ag_con.json()[0]["user"]["group"]

                if status == "Agent constat":
                    json['agent_constat']=ag_con.json()[0]["id"]
                else:
                    return jsonify({"Status":"agent constat n'existe pas"}), 200

            else:
                json['agent_constat']=rdv.json()[0]['agent_constat']
            
            if request.json["planner"] != None:
                ag_con=requests.get("http://195.15.218.172/agent_app/agent/"+int(request.json["planner"]), headers={"Authorization":request.headers["Authorization"]})
                #do inserting of agent
                try:
                    status=ag_con.json()['status']
                except:
                    status=ag_con.json()[0]["user"]["group"]

                if status == "Audit planneur":
                    json['audit_planneur']=ag_con.json()[0]["id"]
                else:
                    return jsonify({"Status":"agent planneur n'existe pas"}), 200

            else:
                json['audit_planneur']=rdv.json()[0]['audit_planneur']

            rdv=requests.put("http://195.15.218.172/rdv_app/rdv/"+str(ide),json=json,headers={"Authorization":request.headers["Authorization"]})

            

            return jsonify({"Rendez vous":rdv.json()}), 200
        else:
            return jsonify({"Status rdv":rdv.json()[0]['statut']}), 400
        
        #return jsonify({"Rendez vous":'sent'}), 200


@clefs.route('/mail/rdv/', methods=['POST',"GET"])
def mail():
    db.create_all()
    users=request.json["users"]
    status=request.json["status"]
    if status == "CREATION COMMANDE":
        client=request.json["client"]
        Type=request.json["intervention"]
        jour=request.json["jour"]
        message="La commande du client "+client+" type d'intervention "+Type+" du "+jour+" a été créé avec succès"
    if status == "CHANGEMENT DE STATUT":
        client=request.json["client"]
        Type=request.json["intervention"]
        date=request.json["date"]
        nouvel=request.json["new"]
        if nouvel ==1:
            nouvel='Attente de prise en charge'
        if nouvel ==2:
            nouvel='Prise en charge'
        if nouvel ==3:
            nouvel='Action requise'
        if nouvel ==4:
            nouvel='Organise'
        message="Le RDV  type d'intervention "+Type+" du client "+client+" du "+date+" est passé de l'état "+nouvel+" Veuillez vous connecter pour consulter les différentes informations"
    if status == "AFFECTATION AGENT SECTEUR":
        client=request.json["client"]
        Type=request.json["intervention"]
        date=request.json["date"]
        agent1=request.json["agent1"]
        agent2=request.json["agent2"]
        message="L'agent constat responsable du RDV  type d'intervention "+Type+" du client "+client+" le "+date+" est "+agent1+ " et "+agent2
    if status == "CONFIRMATION HORAIRES":
        client=request.json["client"]
        Type=request.json["intervention"]
        date=request.json["date"]
        heure=request.json["heure"]
        message="Bonjour votre RDV pour la réalisation  type d'intervention "+Type+" du client "+client+" est confirmée pour le "+date+ " a " +heure
    if status == "Creation Compte":
        login=request.json["login"]
        MDP=request.json["mdp"]
        message="Bonjour votre compte a été activé "+login+','+MDP+" veuillez vous connecter pour vous authentifier"
    if status == "MODIFICATION USER":
        login=request.json["login"]
        MDP=request.json["mdp"]
        if MDP != '':
            message="Bonjour votre compte à été modifié "+login+','+MDP+" veuillez vous connecter pour consulter les mises à jour"
        else:
            message="Bonjour votre compte à été modifié ,veuillez vous connecter pour consulter les mises à jour"
    if status == "COMMENT":
        rdv=request.json["client"]
        Type=request.json["type"]
        Date=request.json["date"]
        message="Un commentaire a ete ajouter au rendezvous du client "+rdv+" de type d'intervention "+Type+' de la date '+Date+".veuillez vous connecter pour consulter les mises à jour"
    if status == "DOCUMENT":
        rdv=request.json["client"]
        Type=request.json["type"]
        Date=request.json["date"]
        message="Un Document a ete ajouter au rendezvous du client "+rdv+" de type d'intervention "+Type+' de la date '+Date+".veuillez vous connecter pour consulter les mises à jour"
    if status == "PASSE":
        login=request.json["login"]
        rdv=request.json["mdp"]
        message="Bonjour votre  mot de passe  a été changer "+login+','+MDP+" veuillez vous connecter pour vous authentifier"
    if status == "MODIFICATION":
        ref=request.json["ref"]
        Type=request.json["intervention"]
        Date=request.json["date"]
        client=request.json["client"]
        AS=request.json["AS"]
        AC=request.json["AC"]
        AP=request.json["AP"]
        message="Le RDV avec ref "+ref+"et intervention"+Type+"du"+Date+ " du client "+client+ " a été modifié.Veuillez vous connecter pour consulter les mises à jour,avec AS "+AS+' ,AC '+AC+' ,AP'+AP

    
        

    send_email(users,message)
    

    return jsonify({"Mail sent":'sent'}), 200