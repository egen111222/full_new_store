from models import Order
from models import db

class Cart:
    def __init__(self):
        self.items = []

    def numerate_items(self):
        return enumerate(self.items)

    def add_item(self,item):
        self.items.append(item)

    def remove_item(self,number):
        self.items.pop(number)

    def clear(self):
        self.items = []

    def get_price(self):
        price = 0
        for item in self.items:
            price += item.price
        return price

    def get_count(self):
        return len(self.items)


    def create_order(self,form):
        order = Order(username = form.get("username"),
                      lastname = form.get("lastname"),
                      phone_or_email = form.get("phone_or_email"),
                      price = self.get_price())
        for item in self.items:
            order.items.append(item)
        db.session.add(order)
        db.session.commit()
        return order


    

def set_cart(session):
    if "cart" not in session:
        session["cart"] = Cart()
    return session.get("cart")
