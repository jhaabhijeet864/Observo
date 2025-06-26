"""WSGI entry point for Render deployment"""
print("[WSGI] wsgi.py is being executed.")
try:
    import os
    import sys
    from app.simple_backend import app
except Exception as e:
    print(f"[WSGI] Import error: {e}", file=sys.stderr)
    raise

# Explicitly print the port for debugging
port = int(os.environ.get('PORT', 10000))
print(f"WSGI: Attempting to bind to PORT: {port}", file=sys.stderr)

# For Gunicorn - this allows the application to be imported
# Do not remove this app variable
application = app

# This is only used when running directly (not through Gunicorn)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
