"""
Training Launcher for VISTA_S
============================
This script ensures we use the correct Python environment
"""

import subprocess
import sys
import os

def find_working_python():
    """Find Python executable with ultralytics installed"""
    python_candidates = [
        "python",
        "python3", 
        "python.exe",
        r"C:\Users\hp\AppData\Local\Microsoft\WindowsApps\python.exe",
        r"C:\Python311\python.exe",
        r"C:\Program Files\Python311\python.exe"
    ]
    
    for python_exe in python_candidates:
        try:
            # Test if this Python has ultralytics
            result = subprocess.run([python_exe, '-c', 'import ultralytics; print("OK")'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0 and "OK" in result.stdout:
                print(f"✅ Found working Python: {python_exe}")
                return python_exe
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            continue
    
    return None

def run_training():
    """Run the training with the correct Python"""
    print("🔍 Finding Python with ultralytics...")
    python_exe = find_working_python()
    
    if python_exe is None:
        print("❌ Could not find Python with ultralytics installed")
        print("💡 Please install ultralytics: pip install ultralytics torch torchvision")
        return False
    
    # Change to project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    
    print(f"🚀 Starting training with {python_exe}...")
    print("📊 Training will run for 300 epochs with optimized settings")
    print("⏱️  This may take several hours depending on your hardware")
    
    # Run the training
    try:
        subprocess.run([python_exe, 'src/train.py'], check=True)
        print("🎉 Training completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Training failed with error: {e}")
        return False
    except KeyboardInterrupt:
        print("\n⏹️  Training interrupted by user")
        return False

if __name__ == "__main__":
    success = run_training()
    if success:
        print("\n✅ Your model is ready!")
        print("📁 Check the 'runs' directory for results")
    else:
        print("\n❌ Training failed. Please check the error messages above.")
