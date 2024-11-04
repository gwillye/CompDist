import logging, os
from flask import Flask
from flask_migrate import Migrate
from flask_admin import Admin
from .model import db, Profile
from .admin import ProfileView, setup_admin
from .config import create_user_if_not_exists, setup_migrate, set_environments

def setup_log():
    # Caminho para o arquivo de log
    current_dir = os.path.abspath(os.path.dirname(__file__))
    project_root = os.path.dirname(current_dir)

    log_file_path = os.path.join(project_root, 'log', 'app.log')
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    # Application log
    logging.basicConfig(format='%(asctime)s - %(message)s', filename=log_file_path, level=logging.INFO)
    logging.info("Aplicação Flask iniciada.")

def create_app():
    setup_log()

    app = Flask(__name__)

    # atribui os valores das variáveis de ambiente
    set_environments(app)
    # inicia o banco de dados
    db.init_app(app)
    with app.app_context():
        from .routes import app as routes
        app.register_blueprint(routes)
        # configura a migration
        setup_migrate()
        # Habilitar o admin
        setup_admin()
        # cria as tabelas caso não existam
        db.create_all()
        # cria usuário padrão caso não exista
        username = app.config.get('DEFAULT_USERNAME')
        password = app.config.get('DEFAULT_PASSWORD')
        create_user_if_not_exists(username, password)

    return app
