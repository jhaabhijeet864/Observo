"""WSGI entry point for Render deployment"""
import os
import sys

print("[WSGI] wsgi.py is being executed.")

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask application
from app.backend import app

# This is what Gunicorn will use
application = app

# Only run directly if not through Gunicorn
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    print(f"WSGI: Running directly on PORT: {port}", file=sys.stderr)
    app.run(host='0.0.0.0', port=port, debug=False)

bind = "0.0.0.0:" + os.environ.get('PORT', '10000')  # Match render.yaml
# Only run directly if not through Gunicorn
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    print(f"WSGI: Running directly on PORT: {port}", file=sys.stderr)
    app.run(host='0.0.0.0', port=port, debug=False)

bind = "0.0.0.0:" + os.environ.get('PORT', '10000')  # Match render.yaml
