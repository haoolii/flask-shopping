from app.extensions import ma
from app.models.User import User

class UserSchema(ma.Schema):
    class Mate:
        model = User
    username = ma.Str(required=True)
    password = ma.Str(required=True)