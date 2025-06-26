"""WSGI entry point for Render deployment"""

from app.simple_backend import app

if __name__ == "__main__":
    app.run()
