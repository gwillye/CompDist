from app.models import Profile
from werkzeug.security import generate_password_hash, check_password_hash

def verify_password(username, password):
    user = Profile.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return user

def hash_password(password):
    return generate_password_hash(password)
