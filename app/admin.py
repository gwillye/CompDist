from flask import current_app as app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .basic_auth import auth
from .model import Profile

# Protect the Flask-Admin using username/password strings and SQLAlchemy
def validate_authentication(username, password):
    user = Profile.query.filter(Profile.username == username)

    if user.all():
        user_query = user.all()[0]
        if user_query.password == password:
            return True
        return False
    return False

class MyModelView(ModelView):
    def is_accessible(self):
        if auth.get_auth():
            username = auth.get_auth()['username']
            password = auth.get_auth()['password']
        else:
            username = None
            password = None

        if username and password:
            if validate_authentication(username, password) and username in app.config.get('ADMINISTRATORS'):
                return True
            else:
                raise AuthException('Not authenticated.')
        else:
            raise AuthException('Not authenticated.')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(auth.login_required())

class ProfileView(MyModelView):
    column_exclude_list = ['password', ]
    column_searchable_list = ['username', ]
    can_export = True
    can_view_details = True

# # Admin Interface
# admin = Admin(app, name='Super App', template_mode='bootstrap4')
# admin.add_view(ProfileView(Profile, db.session))