from flask import Blueprint, request, render_template, send_from_directory, jsonify
import os
import sys
import logging
import uuid
from datetime import datetime

# Add the parent directory to sys.path to import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.detect import detect

logger = logging.getLogger(__name__)

routes = Blueprint('routes', __name__)

# Use absolute path for uploads in production, or relative path in development
UPLOAD = os.environ.get('UPLOAD_DIR', 'uploads')
os.makedirs(UPLOAD, exist_ok=True)

# Define model path based on environment
MODEL_PATH = os.environ.get('MODEL_PATH', os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'models', 'weights', 'best.pt'))

@routes.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        file = request.files['image']
        path = os.path.join(UPLOAD, file.filename)
        file.save(path)
        results = detect(path, model_path=MODEL_PATH)
        saved = results[0].masks.data if results else None
        return render_template('index.html', img_out=os.path.basename(results[0].path[0]))
    return render_template('index.html')

@routes.route('/api/detect', methods=['POST'])
def api_detect():
    import time
    start_time = time.time()
    try:
        logger.info("API detect endpoint called")
        if 'image' not in request.files:
            logger.warning("No image file in request")
            return jsonify({'error': 'No image file provided'}), 400
        file = request.files['image']
        if file.filename == '':
            logger.warning("Empty filename")
            return jsonify({'error': 'No image selected'}), 400
        filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}_{file.filename}"
        path = os.path.join(UPLOAD, filename)
        file.save(path)
        logger.info(f"File saved to {path}")
        results = detect(path, model_path=MODEL_PATH)
        logger.info(f"Detection complete, processing results")
        detections = []
        if results and len(results) > 0:
            result = results[0]
            for i, box in enumerate(result.boxes):
                class_id = int(box.cls.item())
                label = result.names[class_id]
                confidence = float(box.conf.item())
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                risk_level = 'high' if confidence < 0.7 else 'medium' if confidence < 0.9 else 'low'
                detections.append({
                    'id': str(i),
                    'label': label,
                    'confidence': confidence,
                    'bbox': {'x': x1, 'y': y1, 'width': x2-x1, 'height': y2-y1},
                    'risk_level': risk_level
                })
            output_image_path = result.path[0] if hasattr(result, 'path') and len(result.path) > 0 else None
            image_id = os.path.basename(output_image_path) if output_image_path else None
            processing_time = int((time.time() - start_time) * 1000)
            return jsonify({
                'success': True,
                'results': detections,
                'processing_time': processing_time,
                'image_id': image_id
            })
        else:
            logger.warning("No detection results")
            processing_time = int((time.time() - start_time) * 1000)
            return jsonify({
                'success': True,
                'results': [],
                'processing_time': processing_time,
                'image_id': None
            })
    except Exception as e:
        logger.error(f"Error in API detection: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500

@routes.route('/uploads/<path:filename>')
def uploads(filename):
    return send_from_directory('models/logs/detect', filename)

@routes.route('/api/images/<path:filename>')
def api_images(filename):
    return send_from_directory('../models/logs/detect', filename)

@routes.route('/api/health', methods=['GET'])
def api_health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0',
        'source': 'routes_blueprint'
    })

@routes.route('/api/statistics', methods=['GET'])
def api_statistics():
    """Return statistics in the format expected by the frontend."""
    base_data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'raw', 'data')
    stats = {}
    for split in ['train', 'val', 'test']:
        split_dir = os.path.join(base_data_dir, split)
        if os.path.exists(split_dir):
            stats[f'{split}_images'] = len([f for f in os.listdir(split_dir) if os.path.isfile(os.path.join(split_dir, f))])
        else:
            stats[f'{split}_images'] = 0

    return jsonify({
        'total_detections': sum(stats.values()),
        'accuracy_rate': 95.8,  # Replace with actual accuracy if available
        'avg_processing_time': 1200,  # ms, replace with real value if available
        'uptime': '99.9%',  # Replace with actual uptime if available
        'model_version': '1.0.0'
    })

@routes.route('/api/models', methods=['GET'])
def api_models():
    weights_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'models', 'weights')
    if os.path.exists(weights_dir):
        weights = [f for f in os.listdir(weights_dir) if os.path.isfile(os.path.join(weights_dir, f)) and f.endswith('.pt')]
    else:
        weights = []
    active_model = os.path.basename(MODEL_PATH) if os.path.exists(MODEL_PATH) else None
    return jsonify({
        'models': weights,
        'active_model': active_model
    })
