import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/usersdb.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASIC_AUTH_FORCE = True
    FLASK_ADMIN_SWATCH = 'yeti'
