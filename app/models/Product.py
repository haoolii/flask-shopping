from app import db
from datetime import datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    price = db.Column(db.Integer)
    image = db.Column(db.String(1024))
    url = db.Column(db.String(1024))
    description = db.Column(db.String(1024))
    product_type = db.Column(db.String(256))
    category_id = db.Column(db.Integer)
    create_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)