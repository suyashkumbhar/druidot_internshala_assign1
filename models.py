# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person_info(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    image_path = db.Column(db.String(255), nullable=False)  # Store image path instead of image data

    def __repr__(self):
        return f'<Person {self.name}>'
