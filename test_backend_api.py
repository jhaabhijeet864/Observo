"""
Backend API Test Script
======================
Test your deployed VISTA_S backend API
"""

import requests
import json
import os

def test_backend_api():
    """Test the deployed backend API endpoints"""
    base_url = "https://vista-s.onrender.com"
    
    print("🧪 Testing VISTA_S Backend API")
    print("=" * 40)
    print(f"🌐 Base URL: {base_url}")
    
    # Test 1: Health Check
    print("\n1️⃣ Testing Health Endpoint...")
    try:
        response = requests.get(f"{base_url}/api/health", timeout=10)
        if response.status_code == 200:
            print("✅ Health check passed!")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health check error: {e}")
    
    # Test 2: Image Detection (if you have a test image)
    print("\n2️⃣ Testing Image Detection Endpoint...")
    
    # Check if we have any test images
    test_images = []
    for ext in ['jpg', 'jpeg', 'png']:
        for path in ['uploads/', 'data/images/', 'test_images/']:
            if os.path.exists(path):
                for file in os.listdir(path):
                    if file.lower().endswith(ext):
                        test_images.append(os.path.join(path, file))
                        break
        if test_images:
            break
    
    if test_images:
        test_image = test_images[0]
        print(f"   Using test image: {test_image}")
        
        try:
            with open(test_image, 'rb') as img_file:
                files = {'image': img_file}
                response = requests.post(f"{base_url}/api/detect", files=files, timeout=30)
                
                if response.status_code == 200:
                    result = response.json()
                    print("✅ Detection endpoint working!")
                    print(f"   Detections found: {len(result.get('detections', []))}")
                    
                    for i, detection in enumerate(result.get('detections', [])[:3]):  # Show first 3
                        print(f"   Detection {i+1}: {detection['label']} "
                              f"(confidence: {detection['confidence']:.2f})")
                else:
                    print(f"❌ Detection failed: {response.status_code}")
                    print(f"   Response: {response.text}")
        except Exception as e:
            print(f"❌ Detection test error: {e}")
    else:
        print("⚠️  No test images found. Upload an image to test detection.")
        print("   You can test manually by uploading an image to:")
        print(f"   {base_url}/api/detect")
    
    # Test 3: Root endpoint
    print("\n3️⃣ Testing Root Endpoint...")
    try:
        response = requests.get(base_url, timeout=10)
        if response.status_code == 200:
            print("✅ Root endpoint accessible!")
        else:
            print(f"⚠️  Root endpoint returned: {response.status_code}")
    except Exception as e:
        print(f"❌ Root endpoint error: {e}")
    
    print("\n📋 API Integration Summary:")
    print("=" * 40)
    print("For your frontend team, share these details:")
    print(f"🔗 API Base URL: {base_url}")
    print("📡 Available Endpoints:")
    print("   GET  /api/health        - Health check")
    print("   POST /api/detect        - Object detection")
    print("   GET  /api/images/<file> - Get processed images")
    print("   GET  /uploads/<file>    - Get uploaded files")
    print("\n📤 Detection API Usage:")
    print("   Method: POST")
    print("   Endpoint: /api/detect")
    print("   Content-Type: multipart/form-data")
    print("   Body: FormData with 'image' field")
    print("\n🔄 Expected Response Format:")
    print(json.dumps({
        "success": True,
        "detections": [
            {
                "id": "0",
                "label": "FireExtinguisher",
                "confidence": 0.85,
                "bbox": {"x": 100, "y": 50, "width": 200, "height": 300},
                "risk_level": "low"
            }
        ],
        "image_url": "/api/images/processed_image.jpg"
    }, indent=2))

if __name__ == "__main__":
    test_backend_api()
