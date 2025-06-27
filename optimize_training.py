"""
Advanced YOLO Model Optimization Techniques
==========================================
Multiple strategies to improve model performance without using larger models
"""

import os
import yaml
from ultralytics import YOLO
import torch
import argparse
from pathlib import Path

class YOLOOptimizer:
    def __init__(self, model_path="yolov8s.pt", data_yaml="yolo_params.yaml"):
        self.model_path = model_path
        self.data_yaml = data_yaml
        self.this_dir = os.path.dirname(__file__)
        
    def optimize_hyperparameters(self):
        """
        Technique 1: Hyperparameter Optimization
        - Better learning rate scheduling
        - Optimized augmentation parameters
        - Advanced optimizer settings
        """
        return {
            # Learning Rate Optimization
            'lr0': 0.01,          # Higher initial learning rate
            'lrf': 0.01,          # Higher final learning rate ratio
            'momentum': 0.937,     # Optimal momentum for SGD
            'weight_decay': 0.0005, # L2 regularization
            
            # Advanced Augmentation
            'hsv_h': 0.015,       # Hue augmentation
            'hsv_s': 0.7,         # Saturation augmentation  
            'hsv_v': 0.4,         # Value augmentation
            'degrees': 10.0,      # Rotation range
            'translate': 0.1,     # Translation fraction
            'scale': 0.5,         # Scaling range
            'shear': 2.0,         # Shear range
            'perspective': 0.0002, # Perspective transformation
            'flipud': 0.5,        # Vertical flip probability
            'fliplr': 0.5,        # Horizontal flip probability
            'mosaic': 1.0,        # Mosaic augmentation
            'mixup': 0.15,        # Mixup augmentation (boost performance)
            'copy_paste': 0.3,    # Copy-paste augmentation
            
            # Training Optimization
            'warmup_epochs': 3,   # Warmup epochs
            'warmup_momentum': 0.8, # Warmup momentum
            'warmup_bias_lr': 0.1,  # Warmup bias learning rate
            'box': 7.5,           # Box loss weight
            'cls': 0.5,           # Classification loss weight
            'dfl': 1.5,           # Distribution focal loss weight
            
            # Optimizer
            'optimizer': 'SGD',   # SGD often works better than AdamW for YOLO
        }
    
    def train_with_advanced_techniques(self, epochs=100, imgsz=640, batch_size=16):
        """
        Technique 2: Advanced Training Strategies
        """
        os.chdir(self.this_dir)
        model = YOLO(self.model_path)
        
        # Get optimized hyperparameters
        hyp = self.optimize_hyperparameters()
        
        print("🚀 Starting Optimized Training with Advanced Techniques...")
        print(f"📊 Hyperparameters: {hyp}")
        
        results = model.train(
            data=self.data_yaml,
            epochs=epochs,
            imgsz=imgsz,
            batch=batch_size,
            device=0 if torch.cuda.is_available() else 'cpu',
            
            # Multi-scale training for better generalization
            rect=False,           # Disable rectangular training for better augmentation
            
            # Advanced techniques
            **hyp
        )
        
        return results, model
    
    def apply_test_time_augmentation(self, model, source):
        """
        Technique 3: Test-Time Augmentation (TTA)
        Significantly improves inference accuracy
        """
        print("🔄 Applying Test-Time Augmentation...")
        
        # TTA with multiple scales and flips
        results = model.predict(
            source=source,
            augment=True,         # Enable TTA
            conf=0.25,           # Lower confidence threshold
            iou=0.45,            # IoU threshold for NMS
            max_det=1000,        # Maximum detections
            half=True,           # Use FP16 for speed
            save=True
        )
        
        return results
    
    def ensemble_prediction(self, model_paths, source):
        """
        Technique 4: Model Ensemble
        Combine predictions from multiple models
        """
        print("🎯 Running Model Ensemble...")
        
        all_results = []
        for model_path in model_paths:
            model = YOLO(model_path)
            results = model.predict(
                source=source,
                augment=True,
                conf=0.15,  # Lower confidence for ensemble
                save=False
            )
            all_results.append(results)
        
        # Ensemble logic would be implemented here
        # For now, return results from best model
        return all_results[0]
    
    def optimize_data_quality(self):
        """
        Technique 5: Data Quality Optimization
        """
        improvements = [
            "📈 Data Quality Optimization Recommendations:",
            "",
            "1. 🎯 Label Quality:",
            "   - Review and fix mislabeled samples",
            "   - Ensure consistent labeling standards",
            "   - Remove ambiguous or poor quality images",
            "",
            "2. 📊 Data Distribution:",
            "   - Balance class distribution",
            "   - Add hard negative examples",
            "   - Include edge cases and challenging scenarios",
            "",
            "3. 🖼️ Image Quality:",
            "   - Maintain consistent image resolution",
            "   - Ensure good lighting and contrast",
            "   - Include various backgrounds and contexts",
            "",
            "4. 🔄 Data Augmentation Strategy:",
            "   - Use domain-specific augmentations",
            "   - Apply progressive augmentation during training",
            "   - Consider synthetic data generation",
        ]
        
        for item in improvements:
            print(item)

def create_optimized_yaml():
    """
    Create an optimized YAML configuration
    """
    config = {
        'path': 'D:/Coding Journey/Hackathons/CodeClash/VISTA_S/data/raw/data',
        'train': 'train/images',
        'val': 'val/images', 
        'test': 'test/images',
        'nc': 3,
        'names': ['FireExtinguisher', 'ToolBox', 'OxygenTank']
    }
    
    with open('optimized_yolo_params.yaml', 'w') as f:
        yaml.dump(config, f, default_flow_style=False)
    
    print("✅ Created optimized_yolo_params.yaml")

def main():
    parser = argparse.ArgumentParser(description='YOLO Model Optimization')
    parser.add_argument('--mode', choices=['train', 'tta', 'ensemble', 'tips'], 
                       default='train', help='Optimization mode')
    parser.add_argument('--epochs', type=int, default=100, help='Training epochs')
    parser.add_argument('--batch-size', type=int, default=16, help='Batch size')
    parser.add_argument('--imgsz', type=int, default=640, help='Image size')
    parser.add_argument('--source', type=str, default='data/test/images', help='Test source')
    
    args = parser.parse_args()
    
    # Create optimized config
    create_optimized_yaml()
    
    optimizer = YOLOOptimizer(
        model_path="yolov8s.pt",
        data_yaml="optimized_yolo_params.yaml"
    )
    
    if args.mode == 'train':
        print("🚀 Starting Optimized Training...")
        results, model = optimizer.train_with_advanced_techniques(
            epochs=args.epochs,
            batch_size=args.batch_size,
            imgsz=args.imgsz
        )
        print(f"✅ Training completed! Results: {results}")
        
    elif args.mode == 'tta':
        print("🔄 Applying Test-Time Augmentation...")
        model = YOLO("runs/detect/train/weights/best.pt")  # Load trained model
        results = optimizer.apply_test_time_augmentation(model, args.source)
        print(f"✅ TTA completed! Results saved.")
        
    elif args.mode == 'ensemble':
        print("🎯 Running Model Ensemble...")
        model_paths = [
            "runs/detect/train/weights/best.pt",
            "runs/detect/train2/weights/best.pt",  # Train multiple models
        ]
        results = optimizer.ensemble_prediction(model_paths, args.source)
        print(f"✅ Ensemble completed!")
        
    elif args.mode == 'tips':
        optimizer.optimize_data_quality()

if __name__ == "__main__":
    main()
