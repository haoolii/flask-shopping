from app.extensions import ma
from app.models.Product import Product

class ProductSchema(ma.Schema):
    class Mate:
        model = Product
    name = ma.Str(required=True)
    price = ma.Int(required=True)
    image = ma.Str(required=True)
    url = ma.Str(required=True)
    description = ma.Str(required=True)
    product_type = ma.Str(required=True)
    category_id = ma.Str(required=True)