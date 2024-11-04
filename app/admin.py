from flask import current_app as app
from flask_admin import Admin
from .model import Profile, db
from .view import ProfileView

def setup_admin():
    # Admin Interface
    admin = Admin(app, name='Super App', template_mode='bootstrap4')
    admin.add_view(ProfileView(Profile, db.session))