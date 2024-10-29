from flask import redirect, Response
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import db, auth
from app.services.auth_service import verify_password
from app.models import Profile
from werkzeug.exceptions import HTTPException


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "Authentication failed.", 401, {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))

class ProfileView(ModelView):
    def is_accessible(self):
        auth_data = auth.get_auth()
        if auth_data:
            user = verify_password(auth_data['username'], auth_data['password'])
            return user is not None
        raise AuthException("Not authenticated.")

admin = Admin(name='Super App', template_mode='bootstrap4')
admin.add_view(ProfileView(Profile, db.session))
