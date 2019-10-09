import os
from flask import Blueprint, request

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/test', methods=['GET'])
def test():
    return 'blueprint_admin'