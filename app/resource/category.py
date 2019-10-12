from flask_restful import Resource
from flask import request
from app.models.schema.Category import CategorySchema
from app.models.Category import Category
from marshmallow import ValidationError

category_schema = CategorySchema(many=False)

def get_param():
    data = request.get_json(force=False)
    if data is None:
        data = request.form
    return data

class category(Resource):
    def get(self, categoryid):
        category = Category.query.get(categoryid)
        if not category:
            return {
                'message': 'category not exits!'
            }, 403
        return {
            'message': 'get category success',
            'category': category_schema.dump(category),
            'products': list(i.json for i in category.products)
        }
    def put(self, categoryid):
        try:
            data = category_schema.load(get_param())
            category = Category.query.get(categoryid)
            category.name = data['name']
            category.update()
            return {
                'message': 'update category success!',
                'category': category.json
            }
        except ValidationError as error:
            return {
                'message': error.messages
            }, 404
        except Exception as error:
            return {
                'message': 'Exception Error'
            }, 404
    def delete(self, categoryid):
        category = Category.query.get(categoryid)
        if not category:
            return {
                'message': 'category not exist!'
            }
        category.delete()
        return {
            'message': 'delete category success',
            'category': category.json
        }
class categories(Resource):
    def post(self):
        try:
            data = category_schema.load(get_param())
            category = Category(name=data['name'])
            category.add()
            return {
                'message': 'create success',
                'category': category.json
            }
        except ValidationError as error:
            return {
                'message': error.messages
            }, 404
    def get(self):
        return {
            'message': 'get all categories success',
            'categories': Category.get_all_categories()
        }