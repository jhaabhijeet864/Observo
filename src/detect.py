import os, cv2
from ultralytics import YOLO

def detect(image_path, model_path='models/weights/best.pt', save_dir='models/logs/detect'):
    os.makedirs(save_dir, exist_ok=True)
    model = YOLO(model_path)
    results = model.predict(source=image_path, save=True, save_dir=save_dir, imgsz=640)
    print(f"Detections saved to {save_dir}")
    return results

if __name__ == '__main__':
    import sys
    img = sys.argv[1] if len(sys.argv)>1 else '../data/raw/test/images/sample.jpg'
    detect(img)