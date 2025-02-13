from .. import db
from datetime import datetime

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    college_email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    is_profile_complete = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)