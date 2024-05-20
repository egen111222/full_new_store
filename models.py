from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

item_order_table = db.Table("item_order_table",
                            db.Column("item_id",db.ForeignKey("items.id")),
                            db.Column("order_id",db.ForeignKey("orders.id"))
                            )


class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    img = db.Column(db.String(200))

    def __str__(self):
        return self.name

    def get_message_text(self):
        message_text = f"""
Назва товару {self.name}
Ціна товару {self.price}"""
        return message_text


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(150),info={"label":"Ім'я"})
    price = db.Column(db.Float,default=0.0)
    lastname = db.Column(db.String(150),info={"label":"Фамілія"})
    phone_or_email = db.Column(db.String(150),info={"label":"Телефон або email"})
    date_of_creation = db.Column(db.DateTime,
                                 default=datetime.now())
    items = db.relationship("Item",
                            secondary=item_order_table)

    def get_message_text(self):
        message_text = f"""Ім'я людини яка замовила {self.username}
Фамілія людини яка замовмила на сайті {self.lastname}
Контактні дані людини яка замовила на сайті {self.phone_or_email}
Дата замовлення {self.date_of_creation}
Ціна замовлення {self.price}
Придбані товари
-----------------------------------------"""
        for item in self.items:
            message_text += item.get_message_text()
            message_text += "\n ----------------------------------------- \n"
        return message_text

    
