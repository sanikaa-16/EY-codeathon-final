from .. import db
from datetime import datetime

from .. import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    
    user_id = db.Column(db.Integer, primary_key=True)
    college_email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # Dean, HoD, Teacher, Student
    phone_number = db.Column(db.String(15), unique=True, nullable=True)
    salary = db.Column(db.Float, nullable=True)  # Only for Faculty
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }
