import os
from ultralytics import YOLO

def main():
    # load model (you can swap to 'yolov8n.pt' for speed or 'yolov8s.pt' for accuracy)
    model = YOLO('yolov8s.pt')
    
    # train
    results = model.train(
        data=os.path.join(os.path.dirname(__file__), '../config/observo.yaml'),
        epochs=50,
        imgsz=640,
        batch=16,
        project='../models/logs',
        name='yolov8_observo',
        exist_ok=True  # overwrite if re-running
    )
    print('Training complete. Results at:', results.path)

if __name__ == '__main__':
    main()