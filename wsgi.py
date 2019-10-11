from app import create_app
from swagger_ui import api_doc
app = create_app()
api_doc(app, config_path='./api.yaml', url_prefix='/api/doc', title='API doc')
