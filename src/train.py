import os
import sys
from ultralytics import YOLO
import yaml
import torch

# Force torchvision to use CPU for NMS operation
def patch_torchvision_nms_to_cpu():
    try:
        import torchvision
        if hasattr(torchvision.ops, 'nms') and torch.cuda.is_available():
            original_nms = torchvision.ops.nms
            
            def cpu_nms(boxes, scores, iou_threshold):
                # Move tensors to CPU before NMS
                boxes_cpu = boxes.cpu() if boxes.is_cuda else boxes
                scores_cpu = scores.cpu() if scores.is_cuda else scores
                indices = original_nms(boxes_cpu, scores_cpu, iou_threshold)
                return indices
            
            # Replace the original NMS with our CPU version
            torchvision.ops.nms = cpu_nms
            print("Patched torchvision NMS to use CPU backend")
    except Exception as e:
        print(f"Warning: Could not patch torchvision NMS: {e}")

def main():
    try:
        # Check for GPU availability
        device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
        print(f"Using device: {device}")
        if device == 'cuda:0':
            print(f"GPU: {torch.cuda.get_device_name(0)}")
            # Apply NMS patch if using CUDA
            patch_torchvision_nms_to_cpu()
            
        # Path to YOLO configuration file
        data_config = os.path.join(os.path.dirname(__file__), '../data/raw/yolo_params.yaml')
        
        # Ensure the config file exists
        if not os.path.exists(data_config):
            raise FileNotFoundError(f"Configuration file not found: {data_config}")
        
        # Initialize the YOLO model with pre-trained weights
        model = YOLO('yolov8s.pt')  # Using YOLOv8 small model
        
        print(f"Starting training with configuration from {data_config}")
          # Train the model with specified parameters        # Force CUDA operations but with CPU NMS
        results = model.train(
            data=data_config,
            epochs=100,
            imgsz=640,
            batch=16,
            project='../models/logs',
            name='yolov8_observo',
            exist_ok=True,
            mosaic=0.1,
            optimizer='AdamW',
            lr0=0.001,
            lrf=0.0001,
            momentum=0.2,
            patience=15,
            save=True,
            single_cls=False,
            device=device,
            nms=False  # Disable NMS in CUDA to avoid issues
        )
        print('Training complete. Model weights and logs saved to ../models/logs/yolov8_observo/')
        return results
        
    except ModuleNotFoundError as e:
        print(f"Error: {e}. Please install required packages with: pip install ultralytics")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred during training: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
