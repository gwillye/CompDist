from flask import Response, current_app as app
from flask_admin.contrib.sqla import ModelView
from werkzeug.exceptions import HTTPException
from .basic_auth import validate_authentication, auth

# Add administrative views here
class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))

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