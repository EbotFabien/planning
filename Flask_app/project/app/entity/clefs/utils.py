from app import mail
from flask_mail import Message


def send_email(user):
    msg = Message('Notifications',
                  sender='noreply@amexpert.pro',
                  recipients=[user])
    msg.body = f''' Pour réinitialiser votre mot de passe, visitez le lien suivant:
               
     
                si vous n'avez pas fait cette demande, ignorez simplement cet e-mail et aucun changement ne sera effectué.
                '''
    mail.send(msg)