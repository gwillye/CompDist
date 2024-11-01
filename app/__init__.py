import logging, os
from flask import Flask
from flask_migrate import Migrate
from flask_admin import Admin
from .model import db, Profile
from .admin import ProfileView

def set_environments(app):
    # Configuration
    app.config.from_pyfile('../cfg/app.cfg', silent=True)
    app.config['FLASK_SECRET'] = app.config.get('SECRET_KEY')
    app.config['BASIC_AUTH_FORCE'] = True
    app.secret_key = app.config.get('SECRET_KEY')

    # Set optional bootswatch theme
    app.config['FLASK_ADMIN_SWATCH'] = 'yeti'

    # adding configuration for using a database
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get('DATABASE')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def setup_migrate(app, db):
    # Settings for migrations
    migrate = Migrate(app, db)

def setup_admin(app, db):
    # Admin Interface
    admin = Admin(app, name='Super App', template_mode='bootstrap4')
    admin.add_view(ProfileView(Profile, db.session))

def create_app():

    # Caminho para o arquivo de log
    current_dir = os.path.abspath(os.path.dirname(__file__))
    project_root = os.path.dirname(current_dir)

    log_file_path = os.path.join(project_root, 'log', 'app.log')
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    # Application log
    logging.basicConfig(format='%(asctime)s - %(message)s', filename=log_file_path, level=logging.INFO)
    logging.info("Aplicação Flask iniciada.")

    app = Flask(__name__)

    # atribui os valores das variáveis de ambiente
    set_environments(app)

    db.init_app(app)

    # configura a migration
    setup_migrate(app, db)

    # Habilitar o admin
    setup_admin(app, db)

    with app.app_context():
        from .routes import app as routes
        app.register_blueprint(routes)
        # cria as tabelas caso não existam
        db.create_all()

    return app
