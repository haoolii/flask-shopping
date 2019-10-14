from app.extensions import ma
from app.models.Order import Order

class OrderSchema(ma.Schema):
    class Mate:
        model = Order
    product_id = ma.Int(required=True)
    amount = ma.Int(required=True)
    receiver_name = ma.Str(required=True)
    receiver_phone = ma.Str(required=True)
    receiver_addr1 = ma.Str(required=True)
    receiver_addr2 = ma.Str(required=True)
    payment_id = ma.Int(required=True)