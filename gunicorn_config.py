"""Gunicorn configuration for Render deployment"""
import os

# Worker configuration
workers = int(os.environ.get('GUNICORN_WORKERS', 1))
threads = int(os.environ.get('GUNICORN_THREADS', 2))
worker_class = 'sync'
worker_connections = 1000
timeout = 120
keepalive = 5

# Server socket
bind = "0.0.0.0:" + os.environ.get('PORT', '5000')
backlog = 2048

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Misc
forwarded_allow_ips = '*'
secure_scheme_headers = {'X-Forwarded-Proto': 'https'}
