from flask import jsonify, redirect
from app import auth, log, db
from app.services.auth_service import verify_password
from app.models import Profile

@auth.verify_password
def verify(username, password):
    return verify_password(username, password)

@auth.login_required
def index():
    user = auth.current_user()
    user_db = Profile.query.filter_by(username=user).first()
    message_info = f"User {user.username} accessed the index."
    log.info(message_info)
    return jsonify({"success": message_info})
