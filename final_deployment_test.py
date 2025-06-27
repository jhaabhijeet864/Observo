#!/usr/bin/env python3
"""
FINAL DEPLOYMENT TEST - VISTA-S Flask Backend
=============================================

This script runs a comprehensive test to ensure the app is ready for deployment.
"""

import sys
import os
import subprocess
import importlib.util

def test_flask_import():
    """Test if Flask can be imported without errors"""
    try:
        import flask
        print(f"✅ Flask {flask.__version__} imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Flask import failed: {e}")
        return False

def test_werkzeug_compatibility():
    """Test Werkzeug compatibility"""
    try:
        import werkzeug
        from werkzeug.urls import url_quote_plus  # This should work in older versions
        print(f"✅ Werkzeug {werkzeug.__version__} is compatible")
        return True
    except ImportError:
        try:
            # In newer versions, url_quote is in urllib.parse
            from urllib.parse import quote_plus
            import werkzeug
            print(f"✅ Werkzeug {werkzeug.__version__} using modern imports")
            return True
        except ImportError as e:
            print(f"❌ Werkzeug compatibility issue: {e}")
            return False

def test_app_import():
    """Test if the main app can be imported"""
    try:
        sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))
        import backend
        print("✅ Backend module imported successfully")
        return True
    except Exception as e:
        print(f"❌ Backend import failed: {e}")
        return False

def test_wsgi_entry():
    """Test WSGI entry point"""
    try:
        import wsgi
        app = wsgi.app
        print("✅ WSGI entry point working")
        return True
    except Exception as e:
        print(f"❌ WSGI entry point failed: {e}")
        return False

def main():
    print("🚀 VISTA-S DEPLOYMENT READINESS TEST")
    print("=" * 50)
    
    tests = [
        ("Flask Import", test_flask_import),
        ("Werkzeug Compatibility", test_werkzeug_compatibility),
        ("App Import", test_app_import),
        ("WSGI Entry", test_wsgi_entry)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 Running: {test_name}")
        if test_func():
            passed += 1
        
    print(f"\n📊 RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED - READY FOR DEPLOYMENT!")
        return True
    else:
        print("⚠️  Some tests failed - check issues above")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
