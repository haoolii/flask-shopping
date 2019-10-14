from app.models.Payment import Payment
from app.models.Product import Product
from app.extensions import db
from datetime import datetime


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', backref=db.backref('orders', lazy=True))
    amount = db.Column(db.Integer)
    receiver_name = db.Column(db.String(256))
    receiver_phone = db.Column(db.String(256))
    receiver_addr1 = db.Column(db.String(1024))
    receiver_addr2 = db.Column(db.String(1024))
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.id'))
    payment = db.relationship('Payment', backref=db.backref('orders', lazy=True))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)