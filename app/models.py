# app/models.py

from . import db

class URL(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    original_url: str = db.Column(db.String(500), nullable=False)
    tiny_url: str = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<URL {self.original_url}>'
