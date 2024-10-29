from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth
from app.config import Config
import logging

# Configuração de logs
logging.basicConfig(filename="log/app.log", level=logging.INFO)
log = logging.getLogger()

# Instâncias de extensões
db = SQLAlchemy()
migrate = Migrate()
auth = HTTPBasicAuth()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        # Importa os módulos necessários
        from app import models, views, admin  
        
        # Cria o banco de dados, se não existir
        db.create_all()
    
    return app
