from app import db
from datetime import datetime

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False, index=True)
    password = db.Column(db.String(128), nullable=False)  # 128 chars for secure hash
    email = db.Column(db.String(65), unique=True, nullable=True)
    registered = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Profile {self.username}>"
