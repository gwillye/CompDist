import logging, json
from flask import Blueprint, jsonify, Response
from .basic_auth import auth
from .controller import UserController

app = Blueprint("__main", __name__)

userController = UserController()

@app.route('/')
@auth.login_required
def index():
    user = userController.get_user()
    message_info = f"Usuário {user}, acessou o index."
    response = {"success": message_info}
    logging.info(message_info)
    return jsonify(response)