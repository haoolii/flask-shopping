from app.models.Category import Category
from app.extensions import db, ma
from datetime import datetime
from flask import jsonify


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    price = db.Column(db.Integer)
    image = db.Column(db.String(1024))
    url = db.Column(db.String(1024))
    description = db.Column(db.String(1024))
    product_type = db.Column(db.String(256))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('products', lazy=True, cascade='all, delete-orphan'))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'image': self.image,
            'url': self.url,
            'description': self.description,
            'product_type': self.product_type,
            'category': self.category.json
        }

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.create_at = datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_product(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_products_by_category(cls, category):
        return list(i.json for i in cls.query.join(Category).filter_by(name=category).all())

    @classmethod
    def get_all_products(cls):
        return list(i.json for i in cls.query.all())