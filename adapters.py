from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField
from flask_login import current_user
from flask import redirect

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect("http://google.com")



class ItemView(AdminView):
    form_extra_fields = {
        'img': ImageUploadField(base_path="static")
    }

class OrderView(AdminView):
    column_list = ("username",
                   "lastname",
                   "phone_or_email",
                   "date_of_creation",
                   "items")
