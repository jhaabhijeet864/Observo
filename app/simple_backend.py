from flask import Flask, jsonify
from flask_cors import CORS
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO,
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create the Flask application
app = Flask(__name__, static_folder=None)

# Configure CORS - add your Netlify URL
CORS(app, origins=['*', 'https://vista-s.netlify.app', 'http://localhost:3000'])

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

# Basic API endpoint for testing
@app.route('/api/test', methods=['GET'])
def test_endpoint():
    return jsonify({
        'message': 'Observo API is running',
        'status': 'success'
    })

# Root endpoint for basic access
@app.route('/', methods=['GET'])
def root():
    return jsonify({
        'message': 'Welcome to Observo API',
        'status': 'online',
        'endpoints': ['/health', '/api/test']
    })

# This makes the app work both locally and on Render
if __name__=='__main__':
    port = int(os.environ.get('PORT', 10000))
    logger.info(f"Starting minimal Observo backend server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
