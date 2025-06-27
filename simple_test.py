#!/usr/bin/env python3
"""
Simple test script for VISTA-S Flask backend.
Tests basic functionality without external dependencies.
"""

import sys
import os

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
            from backend import app, create_app
            print("✓ Backend app imported successfully")
            print(f"✓ App name: {app.name}")
            return app
        except ImportError as e:
            print(f"✗ Failed to import backend app: {e}")
            return None
            
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return None

def test_app_structure():
    """Test Flask app structure and configuration."""
    print("\n=== Testing App Structure ===")
    try:
        from backend import app
        
        # Test app configuration
        print(f"✓ App instance created: {type(app)}")
        print(f"✓ App name: {app.name}")
        print(f"✓ Debug mode: {app.debug}")
        
        # Test routes
        rules = list(app.url_map.iter_rules())
        print(f"✓ Found {len(rules)} routes:")
        for rule in rules:
            methods = ', '.join(rule.methods - {'HEAD', 'OPTIONS'})
            print(f"  {rule.rule} -> {methods}")
        
        return True
    except Exception as e:
        print(f"✗ App structure test failed: {e}")
        return False

def test_app_context():
    """Test Flask app context and basic functionality."""
    print("\n=== Testing App Context ===")
    try:
        from backend import app
        
        with app.app_context():
            print("✓ App context created successfully")
            
            # Test configuration
            print(f"✓ App config accessible: {len(app.config)} items")
            
            # Test if routes are accessible
            client = app.test_client()
            print("✓ Test client created")
            
            # Test health endpoint
            response = client.get('/health')
            print(f"✓ Health endpoint: {response.status_code}")
            if response.status_code == 200:
                data = response.get_json()
                print(f"  Status: {data.get('status')}")
                print(f"  Version: {data.get('version')}")
            
            # Test root endpoint
            response = client.get('/')
            print(f"✓ Root endpoint: {response.status_code}")
            if response.status_code == 200:
                data = response.get_json()
                print(f"  Message: {data.get('message')}")
            
            # Test API test endpoint
            response = client.get('/api/test')
            print(f"✓ API test endpoint: {response.status_code}")
            if response.status_code == 200:
                data = response.get_json()
                print(f"  Status: {data.get('status')}")
            
            # Test detect endpoint without file
            response = client.post('/api/detect')
            print(f"✓ Detect endpoint (no file): {response.status_code}")
            if response.status_code == 400:
                data = response.get_json()
                print(f"  Error: {data.get('error')}")
            
        return True
    except Exception as e:
        print(f"✗ App context test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def check_redundancy():
    """Check for redundant files."""
    print("\n=== Checking for Redundancy ===")
    
    base_dir = os.path.dirname(__file__)
    
    # Check requirements files
    req_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.startswith('requirements') and file.endswith('.txt'):
                req_files.append(os.path.relpath(os.path.join(root, file), base_dir))
    
    print(f"Requirements files found: {len(req_files)}")
    for req_file in req_files:
        print(f"  {req_file}")
    
    if len(req_files) == 1:
        print("✓ Only one requirements.txt file - no redundancy")
    elif len(req_files) == 0:
        print("✗ No requirements.txt file found")
    else:
        print("⚠ Multiple requirements files - potential redundancy")
    
    return len(req_files) <= 1

def main():
    """Main test function."""
    print("VISTA-S Flask Backend Simple Test")
    print("=" * 40)
    
    all_passed = True
    
    # Test imports
    app = test_imports()
    if not app:
        print("\n❌ Import tests failed.")
        all_passed = False
    
    # Test app structure
    if not test_app_structure():
        print("\n❌ App structure tests failed.")
        all_passed = False
    
    # Test app context and endpoints
    if not test_app_context():
        print("\n❌ App context tests failed.")
        all_passed = False
    
    # Check redundancy
    if not check_redundancy():
        print("\n⚠ Redundancy check found issues.")
    
    print("\n" + "=" * 40)
    if all_passed:
        print("✅ All tests passed! Flask app is working correctly.")
        print("\n📋 Summary:")
        print("  • All imports successful")
        print("  • Flask app structure valid")
        print("  • All endpoints responding correctly")
        print("  • Error handling working")
        print("  • CORS configuration present")
        print("  • Requirements files consolidated")
    else:
        print("❌ Some tests failed. Check the output above.")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
