"""
Simple Training Script for VISTA_S
==================================
This script will handle environment setup and training
"""

import sys
import os
import subprocess

def install_requirements():
    """Install required packages"""
    packages = ['ultralytics', 'torch', 'torchvision', 'opencv-python', 'PyYAML']
    
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package} already installed")
        except ImportError:
            print(f"🔄 Installing {package}...")
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                print(f"✅ {package} installed successfully")
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to install {package}: {e}")
                return False
    return True

def run_training():
    """Run the optimized training"""
    try:
        # Import after installation
        from ultralytics import YOLO
        import torch
        
        print("🚀 Starting VISTA_S Model Training")
        print("=" * 50)
        
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
            return False
        
        print(f"📊 Using data config: {data_config}")
        
        # Load model
        model = YOLO('yolov8n.pt')  # Smaller model for faster training
        print("📥 Model loaded: YOLOv8n")
        
        print("🎯 Starting training with optimized parameters...")
        
        # Start training with your optimized parameters
        results = model.train(
            data=data_config,
            epochs=200,          # Increased for better performance
            imgsz=640,
            batch=8,
            
            # Advanced augmentation
            mosaic=0.9,
            mixup=0.15,
            copy_paste=0.3,
            
            # Optimized hyperparameters
            hsv_h=0.015,
            hsv_s=0.7,
            hsv_v=0.4,
            degrees=0.0,
            translate=0.1,
            scale=0.9,
            shear=0.0,
            perspective=0.0,
            flipud=0.0,
            fliplr=0.5,
            
            # Learning rate scheduling
            lr0=0.01,
            lrf=0.001,
            momentum=0.937,
            weight_decay=0.0005,
            warmup_epochs=3.0,
            warmup_momentum=0.8,
            warmup_bias_lr=0.1,
            
            # Loss function weights
            box=7.5,
            cls=0.5,
            dfl=1.5,
            
            # Training strategy
            patience=30,         # Reduced patience
            close_mosaic=10,
            amp=True,
            fraction=1.0,
            
            # Validation settings
            val=True,
            plots=True,
            save=True,
            save_period=10,
            cache=True,
            device=device,
            workers=4,
            
            # NMS settings
            conf=0.001,
            iou=0.7,
            max_det=300,
            
            # Multi-scale training
            rect=False,
            
            # Save location
            project='models/training_runs',
            name='vista_optimized',
            exist_ok=True
        )
        
        print("🎉 Training completed successfully!")
        print(f"📈 Best model saved to: models/training_runs/vista_optimized/weights/best.pt")
        
        # Show results if available
        if hasattr(results, 'results_dict'):
            metrics = results.results_dict
            print("\n📊 Training Results:")
            for key, value in metrics.items():
                if 'mAP' in key:
                    print(f"   {key}: {value:.4f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Training error: {e}")
        return False

def main():
    print("VISTA_S Model Training Setup")
    print("=" * 30)
    
    # Step 1: Install requirements
    print("📦 Checking and installing requirements...")
    if not install_requirements():
        print("❌ Failed to install requirements")
        return
    
    # Step 2: Run training
    print("\n🚀 Starting training...")
    success = run_training()
    
    if success:
        print("\n✅ Training completed successfully!")
        print("💡 Your model is now ready for inference!")
    else:
        print("\n❌ Training failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
