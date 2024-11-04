import os
from flask import current_app as app
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash
from .model import db, Profile

def set_environments(app):
    # carrega variáveis do arquivo .cfg
    app.config.from_pyfile('../cfg/app.cfg', silent=True)
    # Configuration
    secret_key = os.getenv('SECRET_KEY') or app.config.get('SECRET_KEY')
    app.config['FLASK_SECRET'] = secret_key
    app.secret_key = secret_key
    app.config['BASIC_AUTH_FORCE'] = True

    # Set optional bootswatch theme
    app.config['FLASK_ADMIN_SWATCH'] = 'yeti'

    # adding configuration for using a database
    database_uri = os.getenv('DATABASE') or app.config.get('DATABASE')
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # set username and password default
    username = os.getenv('DEFAULT_USERNAME') or app.config.get('DEFAULT_USERNAME')
    password = os.getenv('DEFAULT_PASSWORD') or app.config.get('DEFAULT_PASSWORD')
    app.config['DEFAULT_USERNAME'] = username
    app.config['DEFAULT_PASSWORD'] = password

def setup_migrate():
    # Settings for migrations
    migrate = Migrate(app, db)

def create_user_if_not_exists(username, password):
    user = Profile.query.filter_by(username=username).first()
    # Verifica se o usuário já existe
    if user is None:
        # Se não existir, cria o novo usuário
        new_user = Profile(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        print(f'Usuário {username} criado com sucesso.')
    else:
        print(f'O usuário {username} já existe.')