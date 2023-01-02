from app import mail
from flask_mail import Message


def send_email(user,message):
    msg = Message('Notifications',
                  sender='no-reply@amexpert.pro',
                  recipients=user)
    msg.html=message
    mail.send(msg)
