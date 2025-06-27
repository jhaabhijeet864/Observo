"""Gunicorn configuration for Render deployment"""
import os

# Worker configuration optimized for free tier
workers = 1  # Single worker for free tier memory limits
threads = 2  # Minimal threads to handle concurrent requests
worker_class = 'sync'
worker_connections = 50  # Reduced for free tier
timeout = 30  # Shorter timeout for free tier
keepalive = 2
max_requests = 100  # Restart worker after 100 requests
max_requests_jitter = 10  # Add jitter to prevent thundering herd

# Server socket
bind = "0.0.0.0:" + os.environ.get('PORT', '10000')  # Match render.yaml
backlog = 64  # Reduced backlog

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Process naming
proc_name = 'vista-s-backend'

# Misc
forwarded_allow_ips = '*'
secure_scheme_headers = {'X-Forwarded-Proto': 'https'}

# Preload app for memory efficiency
preload_app = True

# Graceful shutdown
graceful_timeout = 30

# WSGI module - updated to point to correct app
wsgi_module = "wsgi:application"
