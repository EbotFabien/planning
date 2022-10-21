from app import mail
from flask_mail import Message


def send_email(user,message):
    msg = Message('Notifications',
                  sender='noreply@amexpert.pro',
                  recipients=user)
    msg.body = f''' Vous avez recu ce mail depuis CMD:
               
                        {message}

                        
                si vous n'avez pas fait cette demande, ignorez simplement cet e-mail et aucun changement ne sera effectué.
                '''
    mail.send(msg)