from app.models.Payment import Payment
from app.models.Product import Product
from app.extensions import db
from datetime import datetime


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship(
        'Product', backref=db.backref('orders', lazy=True))
    amount = db.Column(db.Integer)
    receiver_name = db.Column(db.String(256))
    receiver_phone = db.Column(db.String(256))
    receiver_addr1 = db.Column(db.String(1024))
    receiver_addr2 = db.Column(db.String(1024))
    receiver_product_type = db.Column(db.String(256))
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.id'))
    payment = db.relationship(
        'Payment', backref=db.backref('orders', lazy=True))
    recode = db.Column(db.String(256))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def json(self):
        return {
            'product': self.product.json,
            'amount': self.amount,
            'receiver_name': self.receiver_name,
            'receiver_phone': self.receiver_phone,
            'receiver_addr1': self.receiver_addr1,
            'receiver_addr2': self.receiver_addr2,
            'payment': self.payment.json,
            'total': self.product.price * self.amount + self.payment.fee
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
    def get_order_by_phone(cls, phone):
        return cls.query.filter_by(receiver_phone=phone).first()

    @classmethod
    def get_order_by_name(cls, name):
        return cls.query.filter_by(receiver_name=name).first()

    @classmethod
    def get_all_orders(cls):
        return list(i.json for i in cls.query.all())
