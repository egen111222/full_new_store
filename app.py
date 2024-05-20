from flask import Flask,render_template
from models import db
from dotenv import load_dotenv
import os
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import Item,Order
from items_part import items_app
from adapters import ItemView,OrderView,AdminView
from flask_session import Session
from cart_part import cart_app
from order_part import orders_app
from config_models import MenuElement
from auth_lib import login_manager
from auth_part import auth_app
from mail_lib import mail
from mail_lib import send_mail

load_dotenv()

app = Flask(__name__,
            static_url_path="")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB"]
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["SESSION_TYPE"] = os.environ["SESSION_TYPE"]
app.config["MAIL_SERVER"] = os.environ["MAIL_SERVER"]
app.config["MAIL_PORT"] = os.environ["MAIL_PORT"]
app.config["MAIL_USE_SSL"] = os.environ["MAIL_USE_SSL"]
app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]

db.init_app(app)

mail.init_app(app)
Session(app)

with app.app_context():
    db.create_all()
    menu_elements = MenuElement.query.all()
    app.jinja_env.globals["menu_elements"] = menu_elements


login_manager.init_app(app)




app.register_blueprint(items_app)
app.register_blueprint(cart_app,url_prefix="/cart")
app.register_blueprint(orders_app,url_prefix="/order")
app.register_blueprint(auth_app)

@app.errorhandler(404)
def user_error(e):
    return render_template("404.html")




admin = Admin(app, name='Магазин', template_mode='bootstrap3')
admin.add_view(ItemView(Item, db.session))
admin.add_view(OrderView(Order, db.session))
admin.add_view(AdminView(MenuElement, db.session))

if __name__ == "__main__":
    app.run()
