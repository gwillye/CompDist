from flask import Blueprint, jsonify
from .basic_auth import auth
from .controller import UserController

app = Blueprint("__main", __name__)

userController = UserController()

@app.route('/')
@auth.login_required
def index():
    response = userController.get_user()
    return jsonify(response)