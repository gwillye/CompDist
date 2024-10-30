from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth
from app.config import Config
import logging
import os

# Configuração de logs
logging.basicConfig(filename="log/app.log", level=logging.INFO)
log = logging.getLogger()

db = SQLAlchemy()
migrate = Migrate()
auth = HTTPBasicAuth()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        from app import models, views, admin  

        db.create_all()
        create_admin_user()
    
    return app

from app.services.auth_service import hash_password
from app.models import Profile

def create_admin_user():
    admin_username = os.environ.get("ADMIN_USERNAME", "admin")
    admin_password = os.environ.get("ADMIN_PASSWORD", "admin_password")
    admin_email = os.environ.get("ADMIN_EMAIL", "admin@example.com")

    if not Profile.query.filter_by(username=admin_username).first():
        user = Profile(
            username=admin_username,
            password=hash_password(admin_password),
            email=admin_email
        )
        db.session.add(user)
        db.session.commit()
