from flask import (Blueprint,
                   render_template,
                   session,
                   url_for,
                   redirect)
from models import Item
from cart import set_cart

cart_app = Blueprint('cart_app', __name__,
                     template_folder='templates')

@cart_app.route("/add/<int:item_number>")
def add_item(item_number):
    cart = set_cart(session)
    item = Item.query\
           .filter(Item.id == item_number)\
           .first()
    cart.add_item(item)
    return redirect(url_for('cart_app.view_cart'))
    

@cart_app.route("/")
def view_cart():
    cart = set_cart(session)
    return render_template("cart.html",
                           cart=cart)


@cart_app.route("/clear")
def clear_cart():
    cart = set_cart(session)
    cart.clear()
    return redirect(url_for('cart_app.view_cart'))


@cart_app.route("/remove/<int:item_number>")
def remove_item(item_number):
    cart = set_cart(session)
    cart.remove_item(item_number)
    return redirect(url_for('cart_app.view_cart'))




