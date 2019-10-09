import os
from flask import Blueprint, request

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/test', methods=['GET'])
def test():
    return 'api_blueprint'