#!/usr/bin/env python3
"""
Test script for VISTA-S Flask backend.
This script performs comprehensive testing of all endpoints and functionality.
"""

import sys
import os
import time
import subprocess
import requests
import json
from threading import Thread
import tempfile

# Add the app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

def test_imports():
    """Test that all required modules can be imported."""
    print("=== Testing Imports ===")
    try:
        import flask
        print(f"✓ Flask version: {flask.__version__}")
        
        import flask_cors
        print("✓ Flask-CORS imported successfully")
        
        # Test backend import
        try:
            from app.backend import app
            print("✓ Backend app imported successfully")
            return app
        except ImportError as e:
            print(f"✗ Failed to import backend app: {e}")
            return None
            
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return None

def test_flask_app_creation():
    """Test Flask app creation and configuration."""
    print("\n=== Testing Flask App Creation ===")
    try:
        from app.backend import app
        print("✓ Flask app created successfully")
        print(f"✓ App name: {app.name}")
        print(f"✓ Debug mode: {app.debug}")
        
        # Test app configuration
        if hasattr(app, 'config'):
            print("✓ App configuration accessible")
        
        return True
    except Exception as e:
        print(f"✗ Flask app creation failed: {e}")
        return False

def start_test_server():
    """Start the Flask app in a separate process for testing."""
    print("\n=== Starting Test Server ===")
    try:
        # Set environment variables for testing
        env = os.environ.copy()
        env['PORT'] = '5555'  # Use a different port for testing
        env['FLASK_ENV'] = 'testing'
        
        # Start the server
        process = subprocess.Popen([
            sys.executable, 'app/backend.py'
        ], env=env, cwd=os.path.dirname(__file__))
        
        # Give the server time to start
        time.sleep(3)
        
        # Check if process is still running
        if process.poll() is None:
            print("✓ Test server started successfully on port 5555")
            return process
        else:
            print("✗ Test server failed to start")
            return None
            
    except Exception as e:
        print(f"✗ Failed to start test server: {e}")
        return None

def test_endpoints():
    """Test all Flask endpoints."""
    print("\n=== Testing Endpoints ===")
    base_url = "http://localhost:5555"
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("✓ Health endpoint working")
            print(f"  Status: {data.get('status')}")
            print(f"  Version: {data.get('version')}")
        else:
            print(f"✗ Health endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"✗ Health endpoint error: {e}")
    
    # Test root endpoint
    try:
        response = requests.get(f"{base_url}/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("✓ Root endpoint working")
            print(f"  Message: {data.get('message')}")
        else:
            print(f"✗ Root endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"✗ Root endpoint error: {e}")
    
    # Test API test endpoint
    try:
        response = requests.get(f"{base_url}/api/test", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("✓ API test endpoint working")
            print(f"  Status: {data.get('status')}")
        else:
            print(f"✗ API test endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"✗ API test endpoint error: {e}")
    
    # Test detect endpoint (POST with no file)
    try:
        response = requests.post(f"{base_url}/api/detect", timeout=10)
        if response.status_code == 400:
            data = response.json()
            print("✓ Detect endpoint properly rejects empty requests")
            print(f"  Error: {data.get('error')}")
        else:
            print(f"? Detect endpoint unexpected response: {response.status_code}")
    except Exception as e:
        print(f"✗ Detect endpoint error: {e}")
    
    # Test detect endpoint with dummy file
    try:
        # Create a temporary image file for testing
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp_file:
            tmp_file.write(b'dummy image data')
            tmp_file_path = tmp_file.name
        
        with open(tmp_file_path, 'rb') as f:
            files = {'image': ('test.jpg', f, 'image/jpeg')}
            response = requests.post(f"{base_url}/api/detect", files=files, timeout=10)
            
        if response.status_code == 200:
            data = response.json()
            print("✓ Detect endpoint accepts file uploads")
            print(f"  Success: {data.get('success')}")
            print(f"  Filename: {data.get('filename')}")
        else:
            print(f"✗ Detect endpoint file upload failed: {response.status_code}")
            
        # Cleanup
        os.unlink(tmp_file_path)
        
    except Exception as e:
        print(f"✗ Detect endpoint file test error: {e}")

def test_cors():
    """Test CORS configuration."""
    print("\n=== Testing CORS ===")
    base_url = "http://localhost:5555"
    
    try:
        # Test preflight request
        headers = {
            'Origin': 'http://localhost:3000',
            'Access-Control-Request-Method': 'POST',
            'Access-Control-Request-Headers': 'Content-Type'
        }
        response = requests.options(f"{base_url}/api/test", headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("✓ CORS preflight request handled")
            cors_headers = {k: v for k, v in response.headers.items() if k.startswith('Access-Control')}
            if cors_headers:
                print("✓ CORS headers present:")
                for header, value in cors_headers.items():
                    print(f"  {header}: {value}")
            else:
                print("? CORS headers not found in response")
        else:
            print(f"✗ CORS preflight failed: {response.status_code}")
            
    except Exception as e:
        print(f"✗ CORS test error: {e}")

def test_error_handling():
    """Test error handling."""
    print("\n=== Testing Error Handling ===")
    base_url = "http://localhost:5555"
    
    # Test non-existent endpoint
    try:
        response = requests.get(f"{base_url}/nonexistent", timeout=10)
        print(f"✓ Non-existent endpoint returns: {response.status_code}")
    except Exception as e:
        print(f"✗ Error handling test failed: {e}")

def check_file_redundancy():
    """Check for redundant files."""
    print("\n=== Checking File Redundancy ===")
    
    # Check for multiple requirements files
    req_files = []
    base_dir = os.path.dirname(__file__)
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.startswith('requirements') and file.endswith('.txt'):
                req_files.append(os.path.join(root, file))
    
    print(f"Found {len(req_files)} requirements files:")
    for req_file in req_files:
        rel_path = os.path.relpath(req_file, base_dir)
        print(f"  {rel_path}")
    
    if len(req_files) == 1:
        print("✓ Only one requirements.txt file found - no redundancy")
    else:
        print("? Multiple requirements files found - consider consolidating")

def main():
    """Main test function."""
    print("VISTA-S Flask Backend Test Suite")
    print("=" * 40)
    
    # Test imports
    app = test_imports()
    if not app:
        print("\n❌ Import tests failed. Cannot proceed with server tests.")
        return False
    
    # Test app creation
    if not test_flask_app_creation():
        print("\n❌ Flask app creation failed. Cannot proceed with server tests.")
        return False
    
    # Check file redundancy
    check_file_redundancy()
    
    # Start test server and run endpoint tests
    print("\n🚀 Starting server tests...")
    server_process = start_test_server()
    
    if server_process:
        try:
            # Run endpoint tests
            test_endpoints()
            test_cors()
            test_error_handling()
            
            print("\n✅ All tests completed!")
            
        finally:
            # Cleanup: terminate the test server
            print("\n🔄 Cleaning up test server...")
            server_process.terminate()
            server_process.wait()
            print("✓ Test server stopped")
            
        return True
    else:
        print("\n❌ Could not start test server. Server tests skipped.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
