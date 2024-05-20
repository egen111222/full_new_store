from flask_mail import Mail
from flask_mail import Message

mail = Mail()


def send_mail(title,
              body,
              recipients=[]):
    msg = Message(title,
                  body=body,
                  sender="Мій_Магазин",
                  recipients=recipients)
    mail.send(msg)
