from app import db

class ContactUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    messages = db.Column(db.String(500), nullable=False)
    
