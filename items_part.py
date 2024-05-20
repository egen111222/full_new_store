from flask import Blueprint,render_template
from models import Item
from models import db

items_app = Blueprint('items_app', __name__,
                      template_folder='templates')



@items_app.route("/")
def view_items():
    items = db.paginate(Item.query,per_page=6)
    return render_template("items.html",
                           items=items)

@items_app.route("/<int:item_number>")
def view_item(item_number):
    item = Item.query\
           .filter(Item.id == item_number)\
           .first()
    return render_template("item.html",
                           item=item)
