from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from .model import Profile

auth = HTTPBasicAuth()

# Authentication control
@auth.verify_password
def verify_password(username, password):
    user = Profile.query.filter(Profile.username == username)

    if user.all():
        user_query = user.all()[0]
        if check_password_hash(generate_password_hash(user_query.password), password):
            return username
