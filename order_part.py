from flask import Blueprint,render_template,session,request
from cart import set_cart
from forms import OrderForm
from mail_lib import send_mail

orders_app = Blueprint('orders_app', __name__,
                       template_folder='templates')


@orders_app.route("/",methods=["GET","POST"])
def create_order():
    form = OrderForm()
    cart = set_cart(session)
    if request.method == "POST":
        form_data = request.form
        order = cart.create_order(form_data)
        message = order.get_message_text()
        send_mail("Нове замовлення на сайті",
                  message,
                  recipients=["egen13@ukr.net"])
        cart.clear()
        return render_template("thanks.html")

    return render_template("order.html",
                           cart=cart,
                           form=form)
