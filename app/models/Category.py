from app.extensions import db
from datetime import datetime


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    @property
    def json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_category(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_all_categories(cls):
        return list(i.json for i in cls.query.all())