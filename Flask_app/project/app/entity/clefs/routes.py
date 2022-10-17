from flask import render_template, url_for,flash,redirect,request,abort,Blueprint,jsonify
from app import bcrypt
import requests
import json








clefs =Blueprint('clefs',__name__)

@clefs.route('/change/<int:ide>/rdv/', methods=['POST'])
def change(ide):
    rdv=requests.get("http://195.15.218.172/rdv_app/rdv/"+str(ide), headers={"Authorization":request.json["token"]})
    print(rdv.json()[0]['statut'])
    try:
        status=rdv.json()[0]['status']
    except:
        status=rdv.json()[0]['statut']

    if status == "not_logged":
        return jsonify({"Fail": "donnee n'exist pas"}), 400
    
    if status == 'Realise':
        null=''
        json={
            "id": 8036,
            "propriete": {
            "id": 23781,
            "surface": "200",
            "numero": "1",
            "numeroParking": "1",
            "adresse": "string",
            "codePostal": "45657",
            "ville": "string",
            "adresseComplementaire": "string",
            "numeroCave": "1",
            "type": "F6 meuble",
            "numeroSol": "1",
            "bailleur": {
                "nom": "Michel",
                "prenom": "Foka",
                "email": "michel@gmail.com",
                "reference": ""
            },
            "locataire": {
                "nom": "Michel",
                "prenom": "Michel",
                "email": "tagnefabrice@gmail.com",
                "telephone": "1234567890"
            }
            },
            "intervention": {
            "type": "Constat entrant",
            "statut": 1,
            "created_at": "2019-04-01T14:07:41Z",
            "id": 1
            },
            "ref_lot": "string2",
            "ref_rdv_edl": "string",
            "client": {
            "id": 1,
            "user": {
                "nom": "DUART",
                "prenom": "DAVID",
                "email": "gestiongerance@cabinetgcardinal.com",
                "login": "AM5431",
                "id": 11,
                "group": "Client pro"
            },
            "ref_comptable": {
                "nom": "DUART DAVID",
                "mobile": "650894722.0",
                "email_envoi_facture": "d.duart@o-real.fr",
                "telephone": "145301240.0",
                "id": 468
            },
            "ref_service_gestion": {
                "nom_complet": "DUART DAVID",
                "mobile": "650894722.0",
                "email": "gestiongerance@cabinetgcardinal.com",
                "telephone": "145301240.0",
                "id": 468
            },
            "info_concession": {
                "agence_secteur_rattachement": "SECTEUR ILE DE FRANCE",
                "nom_concessionnaire": "AMEXPERT FRANCE",
                "numero_proposition_prestation": null,
                "nom_complet": null,
                "as_client": "AMF",
                "origine_client": null,
                "suivie_technique_client": null,
                "agent_rattache": {
                "nom": "MAFAT",
                "prenom": "CEDRIC",
                "email": "mafat2753@amexpert.biz",
                "trigramme": "CMF",
                "id": 13
                }
            },
            "statut": null,
            "type": "professionnel",
            "adresse": "62 RUE DE VOUILLE",
            "titre": "Mademoiselle",
            "fonction": "RESPONSABLE GESTION",
            "societe": "CABINET G.CARDINAL",
            "ref_societe": "CABINET G.CARDINAL",
            "email_agence": "gestiongerance@cabinetgcardinal.com",
            "siret": "79501577500013.0",
            "tva_intercommunautaire": "FR85795015775",
            "complement_adresse": null,
            "code_postal": "75015.0",
            "ville": "PARIS",
            "telephone": "145301240.0",
            "mobile": "650894722.0",
            "telephone_agence": "145301240.0",
            "code_client": "123360.0",
            "created_at": "2018-06-22T09:01:49Z",
            "updated_at": "2019-07-16T11:20:40Z",
            "passeur": []
            },
            "date": "2022-02-21T23:00:00Z",
            "passeur": {
            "id": 1,
            "user": {
                "nom": "AGENT TEST 1",
                "prenom": "XAVIER",
                "email": "xavierdetoc@gmail.com",
                "login": "AMI0186",
                "id": 186,
                "group": "Salarie"
            },
            "agent_rattache": {
                "user": {
                "nom": "AMEXPERT",
                "prenom": "FRANCE",
                "email": "franceggle@amexpert.biz",
                "login": "AMI0260",
                "id": 260
                },
                "trigramme": "AMF",
                "id": 47
            },
            "client": {
                "nom": "FALL",
                "prenom": "BARBARA",
                "email": "b.fall@de-valiere.com",
                "type": "Client pro",
                "id": 177
            },
            "adresse": null,
            "titre": "Monsieur",
            "fonction": "GESTIONNAIRE",
            "company": "AGENCE EDELE SOLUTION",
            "code": null,
            "telephone": "102030405.0",
            "mobile": "102030405.0",
            "created_at": "2019-04-01T22:17:48Z",
            "updated_at": "2019-04-27T16:10:15Z"
            },
            "agent": {
            "id": 92,
            "user": {
                "nom": "string",
                "prenom": "string",
                "email": "brunoowona12@gmail.com",
                "login": "stringb",
                "id": 652,
                "group": "Agent secteur"
            },
            "adresse": "string12",
            "trigramme": "string",
            "created_at": "2022-09-27T10:27:26.547949Z",
            "updated_at": "2022-10-11T17:47:25.101772Z",
            "secteur_primaire": null,
            "secteur_secondaire": null,
            "agent_secteur": null
            },
            "longitude": "238.43",
            "latitude": "238.43",
            "liste_document_recuperer": "string",
            "consignes_particuliere": "string",
            "info_diverses": "string",
            "statut": "Realise",
            "couleur": "purple",
            "ancien_client_id": null,
            "ancien_agent_trigramme": null,
            "agent_constat": null,
            "audit_planneur": null,
            "numero": null,
            "ref_commande": null,
            "last_update_by": null,
            "created_at": null,
            "updated_at": null
        }
        json['statut']="prise en charge"
        json['couleur']="Orange"
        
        
        '''json={
        "nom_bailleur":string,
        "prenom_bailleur":	string,
        "email_bailleur": string,
        "reference_bailleur":string,
        "nom_locataire":	string,
        "prenom_locataire":	True,
        "email_locataire":	string,
        "telephone_locataire":	string,
        "surface_propriete":	string,
        "numero_propriete":	string,
        "numero_parking_propriete":	string,
        "adresse_propriete":	string,
        "code_postal_propriete":	string,
        "ville_propriete":	string,
        "adresse_complementaire_propriete":	string,
        "numero_cave_propriete":	string,
        "numero_sol_propriete":	rdv.json()[0]["propriete"]["numeroSol"],
        "ref_lot":	string,
        "ref_edl":	string,
        "intervention":rdv.json()[0]["intervention"]["id"],
        "client":rdv.json()[0]["client"]["id"],
        "date":	string,
        "statut": "prise en charge",
        "passeur":	rdv.json()[0]["passeur"]["id"],
        "agent":rdv.json()[0]["agent"]["id"],
        "longitude":	string,
        "latitude":	string,
        "type_propriete":	1,
        "type":string,
        "consignes_part":string,
        "list_documents":	string,
        "info_diverses":	string,
        }
        rdv=requests.put("http://195.15.218.172/rdv_app/rdv/"+str(ide),json=json,headers={"Authorization":request.json["token"]})'''

        return jsonify({"Rendez vous":json}), 200
    else:
        return jsonify({"Status rdv":rdv.json()[0]['statut']}), 400


@clefs.route('/affectation/rdv/<int:ide>', methods=['POST', 'PUT'])
def update(ide):
        rdv=requests.get("http://195.15.218.172/rdv_app/rdv/"+str(ide), headers={"Authorization":request.json["token"]})

        try:
            status=rdv.json()[0]['status']
        except:
            status=rdv.json()[0]['statut']

        if status == "not_logged":
            return jsonify({"Fail": "donnee n'exist pas"}), 400
        if status == 'Realise':
            null=''
            json={
                "id": 8036,
                "propriete": {
                "id": 23781,
                "surface": "200",
                "numero": "1",
                "numeroParking": "1",
                "adresse": "string",
                "codePostal": "45657",
                "ville": "string",
                "adresseComplementaire": "string",
                "numeroCave": "1",
                "type": "F6 meuble",
                "numeroSol": "1",
                "bailleur": {
                    "nom": "Michel",
                    "prenom": "Foka",
                    "email": "michel@gmail.com",
                    "reference": ""
                },
                "locataire": {
                    "nom": "Michel",
                    "prenom": "Michel",
                    "email": "tagnefabrice@gmail.com",
                    "telephone": "1234567890"
                }
                },
                "intervention": {
                "type": "Constat entrant",
                "statut": 1,
                "created_at": "2019-04-01T14:07:41Z",
                "id": 1
                },
                "ref_lot": "string2",
                "ref_rdv_edl": "string",
                "client": {
                "id": 1,
                "user": {
                    "nom": "DUART",
                    "prenom": "DAVID",
                    "email": "gestiongerance@cabinetgcardinal.com",
                    "login": "AM5431",
                    "id": 11,
                    "group": "Client pro"
                },
                "ref_comptable": {
                    "nom": "DUART DAVID",
                    "mobile": "650894722.0",
                    "email_envoi_facture": "d.duart@o-real.fr",
                    "telephone": "145301240.0",
                    "id": 468
                },
                "ref_service_gestion": {
                    "nom_complet": "DUART DAVID",
                    "mobile": "650894722.0",
                    "email": "gestiongerance@cabinetgcardinal.com",
                    "telephone": "145301240.0",
                    "id": 468
                },
                "info_concession": {
                    "agence_secteur_rattachement": "SECTEUR ILE DE FRANCE",
                    "nom_concessionnaire": "AMEXPERT FRANCE",
                    "numero_proposition_prestation": null,
                    "nom_complet": null,
                    "as_client": "AMF",
                    "origine_client": null,
                    "suivie_technique_client": null,
                    "agent_rattache": {
                    "nom": "MAFAT",
                    "prenom": "CEDRIC",
                    "email": "mafat2753@amexpert.biz",
                    "trigramme": "CMF",
                    "id": 13
                    }
                },
                "statut": null,
                "type": "professionnel",
                "adresse": "62 RUE DE VOUILLE",
                "titre": "Mademoiselle",
                "fonction": "RESPONSABLE GESTION",
                "societe": "CABINET G.CARDINAL",
                "ref_societe": "CABINET G.CARDINAL",
                "email_agence": "gestiongerance@cabinetgcardinal.com",
                "siret": "79501577500013.0",
                "tva_intercommunautaire": "FR85795015775",
                "complement_adresse": null,
                "code_postal": "75015.0",
                "ville": "PARIS",
                "telephone": "145301240.0",
                "mobile": "650894722.0",
                "telephone_agence": "145301240.0",
                "code_client": "123360.0",
                "created_at": "2018-06-22T09:01:49Z",
                "updated_at": "2019-07-16T11:20:40Z",
                "passeur": []
                },
                "date": "2022-02-21T23:00:00Z",
                "passeur": {
                "id": 1,
                "user": {
                    "nom": "AGENT TEST 1",
                    "prenom": "XAVIER",
                    "email": "xavierdetoc@gmail.com",
                    "login": "AMI0186",
                    "id": 186,
                    "group": "Salarie"
                },
                "agent_rattache": {
                    "user": {
                    "nom": "AMEXPERT",
                    "prenom": "FRANCE",
                    "email": "franceggle@amexpert.biz",
                    "login": "AMI0260",
                    "id": 260
                    },
                    "trigramme": "AMF",
                    "id": 47
                },
                "client": {
                    "nom": "FALL",
                    "prenom": "BARBARA",
                    "email": "b.fall@de-valiere.com",
                    "type": "Client pro",
                    "id": 177
                },
                "adresse": null,
                "titre": "Monsieur",
                "fonction": "GESTIONNAIRE",
                "company": "AGENCE EDELE SOLUTION",
                "code": null,
                "telephone": "102030405.0",
                "mobile": "102030405.0",
                "created_at": "2019-04-01T22:17:48Z",
                "updated_at": "2019-04-27T16:10:15Z"
                },
                "agent": {
                "id": 92,
                "user": {
                    "nom": "string",
                    "prenom": "string",
                    "email": "brunoowona12@gmail.com",
                    "login": "stringb",
                    "id": 652,
                    "group": "Agent secteur"
                },
                "adresse": "string12",
                "trigramme": "string",
                "created_at": "2022-09-27T10:27:26.547949Z",
                "updated_at": "2022-10-11T17:47:25.101772Z",
                "secteur_primaire": null,
                "secteur_secondaire": null,
                "agent_secteur": null
                },
                "longitude": "238.43",
                "latitude": "238.43",
                "liste_document_recuperer": "string",
                "consignes_particuliere": "string",
                "info_diverses": "string",
                "statut": "prise en charge",
                "couleur": "orange",
                "ancien_client_id": null,
                "ancien_agent_trigramme": null,
                "agent_constat": null,
                "audit_planneur": null,
                "numero": null,
                "ref_commande": null,
                "last_update_by": null,
                "created_at": null,
                "updated_at": null
            }
            json['agent_constat']=request.json["constat"]
            json['audit_planneur']=request.json["planner"]
            '''json={
            "agent_constat":request.json["constat"],
            "audit_planneur": request.json["planner"]
            }
            rdv=requests.put("http://195.15.218.172/rdv_app/rdv/"+str(ide),json=json,headers={"Authorization":request.json["token"]})'''

            return jsonify({"Rendez vous":json}), 200
        else:
            return jsonify({"Status rdv":rdv.json()[0]['statut']}), 400
            
    
        

  