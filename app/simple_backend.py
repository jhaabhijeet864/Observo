
from flask import Flask, jsonify
from flask_cors import CORS
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "message": "Observo Backend API is running!",
        "status": "healthy",
        "endpoints": [
            "/api/health",
            "/api/detect"
        ]
    })

@app.route('/api/health')
def health():
    return jsonify({
        "status": "healthy",
        "message": "API is working correctly"
    })

@app.route('/api/detect', methods=['POST'])
def detect_placeholder():
    return jsonify({
        "message": "Detection endpoint placeholder - full functionality will be added once deployment is working",
        "status": "success"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Starting Flask app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
