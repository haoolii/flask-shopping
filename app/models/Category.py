from app.extensions import db
from datetime import datetime


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }