from flask import Flask
from flask_cors import CORS
import logging
from app.routes import routes

logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Register blueprint
app.register_blueprint(routes)

if __name__=='__main__':
    logger.info("Starting Observo backend server")
    app.run(host='0.0.0.0', port=5000, debug=True)