from config import app_config
from app import create_app
import os

app = create_app(app_config[os.getenv('FLASK_ENV')])

@app.route('/')
def hello():
    return 'Hello!Flask-Shop!'
    
if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 8787)))