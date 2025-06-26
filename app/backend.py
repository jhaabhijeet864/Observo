from flask import Flask
from flask_cors import CORS
import logging
from app.routes import routes
import os

logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
# Allow requests from any origin during development, or from specific frontend in production
CORS(app, origins=['*', 'https://your-friends-frontend-domain.com', 'http://localhost:3000'])

# Register blueprint
app.register_blueprint(routes)

# This makes the app work both locally and on Render
if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Starting Observo backend server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)