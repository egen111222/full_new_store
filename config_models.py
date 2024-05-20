from models import db


class MenuElement(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(100))
    link = db.Column(db.String(200))
