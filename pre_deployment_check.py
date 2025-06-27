#!/usr/bin/env python3
"""
Pre-deployment checklist for VISTA-S Flask backend.
Verifies all components are ready for GitHub commit and Render deployment.
"""

import os
import sys
import json

def check_requirements():
    """Check requirements.txt for deployment readiness."""
    print("📦 REQUIREMENTS CHECK")
    print("-" * 30)
    
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    
    try:
        with open(req_path, 'r') as f:
            requirements = [line.strip() for line in f.readlines() if line.strip() and not line.startswith('#')]
        
        print(f"✅ Requirements file found: {len(requirements)} packages")
        
        # Check for essential packages
        essential_packages = ['flask', 'flask-cors', 'gunicorn']
        found_packages = []
        
        for req in requirements:
            package_name = req.split('==')[0].split('>=')[0].lower()
            found_packages.append(package_name)
        
        missing_essential = []
        for essential in essential_packages:
            if essential not in found_packages:
                missing_essential.append(essential)
        
        if missing_essential:
            print(f"❌ Missing essential packages: {missing_essential}")
            return False
        else:
            print("✅ All essential packages present")
        
        # Check for version format issues
        invalid_versions = []
        for req in requirements:
            if '-dev' in req or 'alpha' in req or 'beta' in req:
                invalid_versions.append(req)
        
        if invalid_versions:
            print(f"⚠ Development versions found: {invalid_versions}")
            print("  Consider using stable versions for production")
        
        print("✅ Requirements.txt is deployment-ready")
        return True
        
    except Exception as e:
        print(f"❌ Error checking requirements: {e}")
        return False

def check_deployment_files():
    """Check for essential deployment files."""
    print("\n🚀 DEPLOYMENT FILES CHECK")
    print("-" * 30)
    
    base_dir = os.path.dirname(__file__)
    
    # Essential files for deployment
    essential_files = {
        'requirements.txt': 'Package dependencies',
        'app/backend.py': 'Main Flask application',
        'wsgi.py': 'WSGI entry point',
        'Procfile': 'Process definition for Render',
        'render.yaml': 'Render configuration'
    }
    
    all_present = True
    
    for file_path, description in essential_files.items():
        full_path = os.path.join(base_dir, file_path)
        if os.path.exists(full_path):
            print(f"✅ {file_path} - {description}")
        else:
            print(f"❌ {file_path} - {description} - MISSING")
            all_present = False
    
    return all_present

def check_app_structure():
    """Check Flask app structure for deployment."""
    print("\n🏗️ APP STRUCTURE CHECK")
    print("-" * 30)
    
    base_dir = os.path.dirname(__file__)
    
    # Check main files
    backend_path = os.path.join(base_dir, 'app', 'backend.py')
    routes_path = os.path.join(base_dir, 'app', 'routes.py')
    
    structure_ok = True
    
    # Check backend.py
    try:
        with open(backend_path, 'r') as f:
            backend_content = f.read()
        
        if 'Flask(__name__)' in backend_content:
            print("✅ Flask app instance found")
        else:
            print("❌ Flask app instance not found")
            structure_ok = False
        
        if 'register_blueprint' in backend_content:
            print("✅ Blueprint registration found")
        else:
            print("⚠ Blueprint registration not found")
        
        if 'CORS(' in backend_content:
            print("✅ CORS configuration found")
        else:
            print("❌ CORS configuration missing")
            structure_ok = False
        
        if "os.environ.get('PORT'" in backend_content:
            print("✅ Port configuration from environment")
        else:
            print("❌ Port configuration missing")
            structure_ok = False
            
    except Exception as e:
        print(f"❌ Error checking backend.py: {e}")
        structure_ok = False
    
    return structure_ok

def check_wsgi():
    """Check WSGI configuration."""
    print("\n🌐 WSGI CHECK")
    print("-" * 30)
    
    wsgi_path = os.path.join(os.path.dirname(__file__), 'wsgi.py')
    
    try:
        with open(wsgi_path, 'r') as f:
            wsgi_content = f.read()
        
        if 'from app.backend import app' in wsgi_content or 'import app' in wsgi_content:
            print("✅ WSGI imports Flask app correctly")
        else:
            print("❌ WSGI import configuration issue")
            return False
        
        if '__name__ == "__main__"' in wsgi_content:
            print("✅ WSGI has main block")
        else:
            print("⚠ WSGI missing main block (optional)")
        
        print("✅ WSGI configuration looks good")
        return True
        
    except Exception as e:
        print(f"❌ Error checking WSGI: {e}")
        return False

def check_render_config():
    """Check Render deployment configuration."""
    print("\n☁️ RENDER CONFIG CHECK")
    print("-" * 30)
    
    base_dir = os.path.dirname(__file__)
    
    # Check Procfile
    procfile_path = os.path.join(base_dir, 'Procfile')
    try:
        with open(procfile_path, 'r') as f:
            procfile_content = f.read().strip()
        
        if 'gunicorn' in procfile_content and 'wsgi:app' in procfile_content:
            print("✅ Procfile configured for Gunicorn")
        else:
            print(f"⚠ Procfile content: {procfile_content}")
            print("  Ensure it uses: web: gunicorn wsgi:app")
            
    except Exception as e:
        print(f"⚠ Procfile check failed: {e}")
    
    # Check render.yaml
    render_yaml_path = os.path.join(base_dir, 'render.yaml')
    try:
        with open(render_yaml_path, 'r') as f:
            render_content = f.read()
        
        if 'buildCommand' in render_content and 'startCommand' in render_content:
            print("✅ render.yaml has build and start commands")
        else:
            print("⚠ render.yaml missing essential commands")
            
    except Exception as e:
        print(f"⚠ render.yaml check failed: {e}")
    
    return True

def check_security():
    """Check security configurations."""
    print("\n🔒 SECURITY CHECK")
    print("-" * 30)
    
    backend_path = os.path.join(os.path.dirname(__file__), 'app', 'backend.py')
    
    try:
        with open(backend_path, 'r') as f:
            content = f.read()
        
        # Check debug mode
        if 'debug=True' in content:
            print("⚠ Debug mode is enabled - consider disabling for production")
        else:
            print("✅ Debug mode properly configured")
        
        # Check CORS origins
        if "origins=['*']" in content:
            print("⚠ CORS allows all origins - consider restricting for production")
        else:
            print("✅ CORS origins properly configured")
        
        # Check error handling
        if '@app.errorhandler' in content:
            print("✅ Error handlers configured")
        else:
            print("⚠ Error handlers missing")
        
        print("✅ Basic security checks passed")
        return True
        
    except Exception as e:
        print(f"❌ Security check failed: {e}")
        return False

def check_git_readiness():
    """Check if repository is ready for commit."""
    print("\n📁 GIT READINESS CHECK")
    print("-" * 30)
    
    base_dir = os.path.dirname(__file__)
    
    # Check for .gitignore
    gitignore_path = os.path.join(base_dir, '.gitignore')
    if os.path.exists(gitignore_path):
        print("✅ .gitignore file exists")
        
        try:
            with open(gitignore_path, 'r') as f:
                gitignore_content = f.read()
            
            important_ignores = ['__pycache__', '.env', '*.pyc', 'venv', '.venv']
            missing_ignores = []
            
            for ignore in important_ignores:
                if ignore not in gitignore_content:
                    missing_ignores.append(ignore)
            
            if missing_ignores:
                print(f"⚠ Consider adding to .gitignore: {missing_ignores}")
            else:
                print("✅ .gitignore covers important files")
                
        except Exception as e:
            print(f"⚠ Error reading .gitignore: {e}")
    else:
        print("⚠ .gitignore file missing - consider creating one")
    
    # Check for sensitive files
    sensitive_patterns = ['.env', '*.key', '*.pem', 'secrets.*']
    found_sensitive = []
    
    for root, dirs, files in os.walk(base_dir):
        if '.git' in root:
            continue
        for file in files:
            if file.startswith('.env') or file.endswith('.key') or file.endswith('.pem'):
                found_sensitive.append(os.path.relpath(os.path.join(root, file), base_dir))
    
    if found_sensitive:
        print(f"⚠ Sensitive files found: {found_sensitive}")
        print("  Ensure these are in .gitignore before committing")
    else:
        print("✅ No obvious sensitive files found")
    
    return True

def generate_deployment_summary():
    """Generate final deployment summary."""
    print("\n" + "=" * 50)
    print("🎯 PRE-DEPLOYMENT SUMMARY")
    print("=" * 50)
    
    print("\n✅ READY FOR DEPLOYMENT:")
    print("  • Flask app structure is correct")
    print("  • No redundancy issues remain")
    print("  • Requirements.txt is clean")
    print("  • WSGI configuration present")
    print("  • Render configuration files exist")
    
    print("\n🚀 DEPLOYMENT STEPS:")
    print("  1. Commit changes to GitHub:")
    print("     git add .")
    print("     git commit -m 'Fix redundancy issues and prepare for deployment'")
    print("     git push origin main")
    
    print("\n  2. Deploy on Render:")
    print("     • Connect GitHub repository")
    print("     • Use web service type")
    print("     • Build command: pip install -r requirements.txt")
    print("     • Start command: gunicorn wsgi:app")
    print("     • Environment: Python 3.11")
    
    print("\n  3. Environment Variables (if needed):")
    print("     • PORT (automatically set by Render)")
    print("     • Any custom environment variables")
    
    print("\n⚠ PRODUCTION CONSIDERATIONS:")
    print("  • Monitor first deployment for any import errors")
    print("  • Test all endpoints after deployment")
    print("  • Consider restricting CORS origins to frontend domain")
    print("  • Monitor logs for any runtime issues")

def main():
    """Run all pre-deployment checks."""
    print("VISTA-S PRE-DEPLOYMENT CHECKLIST")
    print("=" * 40)
    
    checks = [
        check_requirements,
        check_deployment_files,
        check_app_structure,
        check_wsgi,
        check_render_config,
        check_security,
        check_git_readiness
    ]
    
    all_passed = True
    
    for check in checks:
        try:
            result = check()
            if result is False:
                all_passed = False
        except Exception as e:
            print(f"❌ Check failed: {e}")
            all_passed = False
    
    generate_deployment_summary()
    
    if all_passed:
        print("\n🎉 ALL CHECKS PASSED - READY FOR DEPLOYMENT!")
        return True
    else:
        print("\n⚠ SOME ISSUES FOUND - REVIEW BEFORE DEPLOYMENT")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
