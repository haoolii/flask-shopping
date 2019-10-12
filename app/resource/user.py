from flask_restful import Resource
from flask import request
from app.models.User import User
from app.models.schema.User import UserSchema
from marshmallow import ValidationError
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

user_schema = UserSchema(many=False)

def get_param():
    data = request.get_json(force=False)
    if data is None:
        data = request.form
    return data

class UserRegistration(Resource):
    def post(self):
        try:
            data = user_schema.load(get_param())
            
            if User.find_by_username(data['username']):
                return {'message': 'User {} already exists'. format(data['username'])}

            user = User(
                username = data['username'],
                password = User.generate_hash(data['password'])
            )
            user.add()
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'User {} was created'.format( data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except ValidationError as error:
            return {
                'message': error.messages
            }, 404
        except:
            return {'message': 'Something went wrong'}, 500

class UserLogin(Resource):
    def post(self):
        data = user_schema.load(get_param())
        current_user = User.find_by_username(data['username'])

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}
        
        if User.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': 'Wrong credentials'}

class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}

class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}

class AllUsers(Resource):
    def get(self):
        return {
            'message': 'get all users success',
            'users': User.return_all()
        }
    
    def delete(self):
        return {
            'message': User.delete_all()
        }

class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }