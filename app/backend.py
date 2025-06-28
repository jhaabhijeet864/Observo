from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import os
import sys
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Create the Flask application
app = Flask(__name__)

# Configure CORS for frontend connection
CORS(app, 
     origins=[
         'https://vista-s-frontend-cwx5jsxdy-abhijeet-jhas-projects.vercel.app',
         'https://vista-s-frontend.vercel.app',
         'https://vista-s-frontend-jhaabhijeet864-abhijeet-jhas-projects.vercel.app/',
         'https://vista-s-frontend-abhijeet-jhas-projects.vercel.app/',
         'http://localhost:3000',
         'http://localhost:8080'
     ],
     methods=['GET', 'POST', 'OPTIONS'],
     allow_headers=['Content-Type', 'Authorization'])



# Import and register routes Blueprint
try:
    from app.routes import routes  # Correct import for Render and most production setups
    app.register_blueprint(routes)
    logger.info("✅ Routes Blueprint registered successfully")
except ImportError as e:
    logger.error(f"❌ Could not import routes Blueprint: {e}")
    # Fallback routes...
    # Create fallback routes
    @app.route('/')
    def home():
        return jsonify({
            'message': 'VISTA-S Backend is running',
            'status': 'healthy',
            'version': '1.0.0'
        })
    
    @app.route('/api/health')
    def health():
        return jsonify({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'version': '1.0.0'
        })
    



    logger.warning("⚠️ Using fallback routes due to import error")

# Error handler
@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled exception: {e}", exc_info=True)
    return jsonify({
        'error': 'Internal server error',
        'message': str(e) if app.debug else 'An error occurred'
    }), 500

# Basic health check endpoint (backup in case routes.py is not available)
@app.route('/health', methods=['GET'])
def health_check():
    logger.info("Health check requested")
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'port': os.environ.get('PORT', 'unknown'),
        'version': '1.0.0'
    }), 200

# CORS preflight handler
@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        response = jsonify({'status': 'ok'})
        response.headers.add("Access-Control-Allow-Origin", "https://vista-s-frontend-cwx5jsxdy-abhijeet-jhas-projects.vercel.app")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response

# Get port from environment
port = int(os.environ.get('PORT', 10000))
logger.info(f"VISTA-S Backend initialized on port {port}")

# Application factory pattern (good practice)
def create_app():
    return app

if __name__ == '__main__':
    logger.info(f"Starting VISTA-S backend server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)