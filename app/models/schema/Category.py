from app.extensions import ma
from app.models.Category import Category

class CategorySchema(ma.Schema):
    class Mate:
        model = Category
    name = ma.Str(required=True)