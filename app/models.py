# app/models.py

from . import db

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    tiny_url = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f'<URL {self.original_url}>'
