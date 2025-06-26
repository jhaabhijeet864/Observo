import os, cv2
from ultralytics import YOLO

def detect(image_path, model_path='models/weights/best.pt', save_dir=None):
    # Default save directory if not provided
    if save_dir is None:
        save_dir = os.environ.get('SAVE_DIR', 'models/logs/detect')
    
    # Make sure directories exist
    os.makedirs(save_dir, exist_ok=True)
    
    # Load the model
    model = YOLO(model_path)
    
    # Run inference
    results = model.predict(source=image_path, save=True, save_dir=save_dir, imgsz=640)
    print(f"Detections saved to {save_dir}")
    return results

if __name__ == '__main__':
    import sys
    img = sys.argv[1] if len(sys.argv)>1 else '../data/raw/test/images/sample.jpg'
    detect(img)