import os
import sys
from ultralytics import YOLO
import torch
import yaml

def patch_torchvision_nms_to_cpu():
    try:
        import torchvision
        if hasattr(torchvision.ops, 'nms') and torch.cuda.is_available():
            original_nms = torchvision.ops.nms
            
            def cpu_nms(boxes, scores, iou_threshold):
                
                boxes_cpu = boxes.cpu() if boxes.is_cuda else boxes
                scores_cpu = scores.cpu() if scores.is_cuda else scores
                indices = original_nms(boxes_cpu, scores_cpu, iou_threshold)
                return indices
            
   
            torchvision.ops.nms = cpu_nms
            print("Patched torchvision NMS to use CPU backend")
    except Exception as e:
        print(f"Warning: Could not patch torchvision NMS: {e}")

def main():
    try:
        device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
        print(f"Using device: {device}")
        if device == 'cuda:0':
            print(f"GPU: {torch.cuda.get_device_name(0)}")
            patch_torchvision_nms_to_cpu()
            
        data_config = os.path.join(os.path.dirname(__file__), '../data/raw/yolo_params.yaml')
        
        if not os.path.exists(data_config):
            raise FileNotFoundError(f"Configuration file not found: {data_config}")

        # Use YOLOv8n for better performance without size increase
        model = YOLO('yolov8n.pt')
        
        print(f"Starting training with configuration from {data_config}")

        # Improved training parameters for better mAP@0.5
        results = model.train(
            data=data_config,
            epochs=300,  # Increase epochs
            imgsz=640,   # Increase image size back to 640
            batch=8,     # Increase if GPU memory allows
            
            # Advanced augmentation
            mosaic=0.9,      # Increase mosaic
            mixup=0.15,      # Fine-tune mixup
            copy_paste=0.3,  # Add copy-paste augmentation
            
            # Optimized hyperparameters
            hsv_h=0.015,     # HSV-Hue augmentation
            hsv_s=0.7,       # HSV-Saturation
            hsv_v=0.4,       # HSV-Value
            degrees=0.0,     # Rotation
            translate=0.1,   # Translation
            scale=0.9,       # Scale
            shear=0.0,       # Shear
            perspective=0.0, # Perspective
            flipud=0.0,      # Flip up-down
            fliplr=0.5,      # Flip left-right
            
            # Learning rate scheduling
            lr0=0.01,
            lrf=0.001,
            momentum=0.937,
            weight_decay=0.0005,
            warmup_epochs=3.0,
            warmup_momentum=0.8,
            warmup_bias_lr=0.1,
            
            # Loss function weights for better mAP
            box=7.5,             # Box loss weight
            cls=0.5,             # Classification loss weight
            dfl=1.5,             # Distribution focal loss weight
            
            # Training strategy
            patience=50,         # Early stopping patience
            close_mosaic=10,     # Close mosaic in last N epochs
            amp=True,            # Automatic mixed precision
            fraction=1.0,        # Use full dataset
            
            # Validation settings
            val=True,
            plots=True,
            save=True,
            save_period=10,      # Save checkpoint every 10 epochs
            cache=True,          # Cache images for faster training
            device=device,
            workers=4,           # Data loading workers
            
            # NMS settings for better detection
            conf=0.001,          # Lower confidence threshold for training
            iou=0.7,             # IoU threshold for NMS
            max_det=300,         # Maximum detections per image
            
            # Multi-scale training
            rect=False,          # Disable rectangular training for multi-scale
        )
        
        print('Training complete. Model weights and logs saved to ../models/logs/yolov8_vista_optimized/')
        
        image_path = '../data/images/sample.jpg'  # Path to your test image
        
        # In detection
        results = model.predict(
            source=image_path,
            conf=0.25,      # Lower confidence threshold
            iou=0.45,       # Optimized IoU for NMS
            max_det=1000,   # Maximum detections
            agnostic_nms=False,  # Class-agnostic NMS
        )
        
        return results
        
    except Exception as e:
        print(f"An error occurred during training: {e}")
        sys.exit(1)

def detect(image_path, model_path='models/weights/best.pt', save_dir=None):
    model = YOLO(model_path)
    # Enable TTA for better accuracy
    results = model.predict(
        source=image_path, 
        save=True, 
        save_dir=save_dir, 
        imgsz=640,
        augment=True,  # Enable TTA
        conf=0.25,     # Lower confidence threshold
        iou=0.45       # Optimized IoU threshold
    )
    return results

if __name__ == '__main__':
    main()
