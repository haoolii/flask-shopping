from app.extensions import db
from datetime import datetime


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pay_type = db.Column(db.String(60))
    fee = db.Column(db.Integer)

    @property
    def json(self):
        return {
            'pay_type': self.pay_type,
            'fee': self.fee
        }