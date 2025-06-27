"""
Simple Training Script for VISTA_S - Direct Version
=================================================== 
This script runs training directly without auto-installation
"""

import os

def main():
    print("🚀 VISTA_S Model Training")
    print("=" * 40)
    
    try:
        # Import required packages
        from ultralytics import YOLO
        import torch
        
        print("✅ All packages loaded successfully")
        
        # Check device
        device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
        print(f"🖥️  Using device: {device}")
        if device == 'cuda:0':
            print(f"🎮 GPU: {torch.cuda.get_device_name(0)}")
        
        # Configure paths
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_config = os.path.join(current_dir, 'data', 'raw', 'yolo_params.yaml')
        
        if not os.path.exists(data_config):
            print(f"❌ Configuration file not found: {data_config}")
            print(f"📁 Current directory: {current_dir}")
            return False
        
        print(f"📊 Using data config: {data_config}")
        
        # Load model
        model = YOLO('yolov8n.pt')
        print("📥 Model loaded: YOLOv8n (optimized for performance)")
        
        print("\n🎯 Training Configuration:")
        print("   📈 Epochs: 200")
        print("   🖼️  Image Size: 640x640")
        print("   📦 Batch Size: 8")
        print("   🎨 Advanced Augmentation: Enabled")
        print("   ⚡ Optimized Hyperparameters: Applied")
        
        print("\n🔥 Starting training...")
        
        # Start training with optimized parameters
        results = model.train(
            data=data_config,
            epochs=200,          # Optimal epochs for good performance
            imgsz=640,
            batch=8,
            
            # Advanced augmentation (PERFORMANCE BOOSTERS)
            mosaic=0.9,          # High mosaic for better learning
            mixup=0.15,          # Mixup for improved generalization
            copy_paste=0.3,      # Copy-paste augmentation
            
            # Optimized hyperparameters
            hsv_h=0.015,         # Color augmentation
            hsv_s=0.7,
            hsv_v=0.4,
            degrees=0.0,         # No rotation (may hurt some objects)
            translate=0.1,       # Translation augmentation
            scale=0.9,           # Scale augmentation
            shear=0.0,           # No shear
            perspective=0.0,     # No perspective
            flipud=0.0,          # No vertical flip
            fliplr=0.5,          # Horizontal flip enabled
            
            # Learning rate scheduling (CRITICAL FOR PERFORMANCE)
            lr0=0.01,            # Initial learning rate
            lrf=0.001,           # Final learning rate
            momentum=0.937,      # SGD momentum
            weight_decay=0.0005, # L2 regularization
            warmup_epochs=3.0,   # Warmup training
            warmup_momentum=0.8,
            warmup_bias_lr=0.1,
            
            # Loss function weights (TUNED FOR BETTER mAP)
            box=7.5,             # Box loss weight
            cls=0.5,             # Classification loss weight
            dfl=1.5,             # Distribution focal loss weight
            
            # Training strategy
            patience=40,         # Early stopping patience
            close_mosaic=10,     # Close mosaic in last 10 epochs
            amp=True,            # Automatic mixed precision
            fraction=1.0,        # Use full dataset
            
            # Validation settings
            val=True,
            plots=True,
            save=True,
            save_period=20,      # Save every 20 epochs
            cache=True,          # Cache images for faster training
            device=device,
            workers=4,           # Data loading workers
            
            # NMS settings for better detection
            conf=0.001,          # Lower confidence for training
            iou=0.7,             # IoU threshold for NMS
            max_det=300,         # Maximum detections per image
            
            # Multi-scale training
            rect=False,          # Disable rectangular training
            
            # Save location
            project='models/training_runs',
            name='vista_optimized_200epochs',
            exist_ok=True,
            
            # Additional optimizations
            cos_lr=True,         # Cosine learning rate scheduler
            optimizer='SGD',     # SGD often better than AdamW for YOLO
        )
        
        print("\n🎉 Training completed successfully!")
        print(f"📈 Best model saved to: models/training_runs/vista_optimized_200epochs/weights/best.pt")
        
        # Show key metrics
        try:
            # Get the last validation results
            print("\n📊 Final Training Metrics:")
            print(f"   📁 Results saved in: models/training_runs/vista_optimized_200epochs/")
            print(f"   🎯 Best weights: models/training_runs/vista_optimized_200epochs/weights/best.pt")
            print(f"   📈 Last weights: models/training_runs/vista_optimized_200epochs/weights/last.pt")
            
        except Exception as e:
            print(f"   ℹ️  Metrics display error: {e}")
        
        print("\n✅ Model is ready for inference!")
        print("💡 Use the best.pt weights for your object detection tasks")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Please install required packages:")
        print("   pip install ultralytics torch torchvision")
        return False
        
    except Exception as e:
        print(f"❌ Training error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🚀 Training completed successfully! Your model is ready to use.")
    else:
        print("\n❌ Training failed. Please check the error messages above.")
