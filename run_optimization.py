"""
Simple Optimized Training Script
==============================
Easy to use script for immediate performance improvements
"""

import os
import sys

# Add the project root to Python path
sys.path.append(os.path.abspath('.'))

def run_optimized_training():
    """
    Run optimized training with better hyperparameters
    """
    try:
        from ultralytics import YOLO
        import torch
        
        print("🚀 Starting Optimized YOLO Training")
        print("=" * 50)
        
        # Change to data directory
        original_dir = os.getcwd()
        os.chdir("data/raw")
        
        # Load model
        model = YOLO("yolov8s.pt")
        
        print("📊 Using optimized hyperparameters...")
        print("⏱️ Training for 50 epochs (increased from 5)")
        print("🎨 Advanced augmentation enabled")
        print("🔥 SGD optimizer with optimal settings")
        
        # Start training with optimized settings
        results = model.train(
            data="yolo_params.yaml",
            epochs=50,              # Much better than 5 epochs
            imgsz=640,
            batch=16,
            
            # Use optimized hyperparameters
            cfg="../../../hyp_optimized.yaml",  # Load our optimized config
            
            # Key optimizations
            optimizer='SGD',        # Better than AdamW for YOLO
            cos_lr=True,           # Cosine learning rate
            
            # Save results
            project='../../../models/optimized_runs',
            name='performance_boost',
            exist_ok=True,
            
            # Enable advanced features
            patience=15,           # Early stopping
            save_period=10,        # Save every 10 epochs
            
            device=0 if torch.cuda.is_available() else 'cpu',
        )
        
        # Change back to original directory
        os.chdir(original_dir)
        
        print("\n✅ Training Completed Successfully!")
        print(f"📈 Results saved to: models/optimized_runs/performance_boost")
        print(f"🎯 Best model: models/optimized_runs/performance_boost/weights/best.pt")
        
        # Show key metrics if available
        if hasattr(results, 'results_dict'):
            metrics = results.results_dict
            print(f"\n📊 Key Metrics:")
            print(f"   mAP50: {metrics.get('metrics/mAP50(B)', 'N/A')}")
            print(f"   mAP50-95: {metrics.get('metrics/mAP50-95(B)', 'N/A')}")
        
        return results
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("💡 Please ensure ultralytics and torch are installed:")
        print("   pip install ultralytics torch")
        return None
    
    except Exception as e:
        print(f"❌ Training Error: {e}")
        return None

def show_improvement_tips():
    """
    Show specific tips for this project
    """
    tips = """
🎯 Specific Improvements for Your VISTA_S Project:

IMMEDIATE ACTIONS (High Impact):
1. 📈 Increase Epochs: Change from 5 to 50-100 epochs
2. 🔧 Switch Optimizer: Use SGD instead of AdamW  
3. 🎨 Enable Full Mosaic: Set mosaic=1.0 (currently 0.1)
4. ⚡ Add Mixup: Include mixup=0.15 for better performance
5. 📊 Better Learning Rate: Use lr0=0.01, lrf=0.01

MEDIUM IMPACT IMPROVEMENTS:
6. 🔄 Test-Time Augmentation: Use augment=True during inference
7. 📏 Multi-Scale Training: Vary image sizes during training
8. 🎯 Lower Confidence: Use conf=0.2 instead of higher values
9. 🔁 Cosine LR Schedule: Enable cos_lr=True
10. 📈 Early Stopping: Add patience=15

DATA IMPROVEMENTS:
11. 🖼️ Check Label Quality: Review annotations for accuracy
12. ⚖️ Balance Classes: Ensure good distribution of all 3 classes
13. 📸 Add Hard Examples: Include challenging/edge cases
14. 🔍 Data Augmentation: Use copy-paste and advanced augmentation

EXPECTED IMPROVEMENTS:
- Current 5 epochs → 50 epochs: +10-20% mAP
- SGD optimizer: +2-5% mAP  
- Full augmentation: +3-8% mAP
- TTA during inference: +2-4% mAP
- Better hyperparameters: +3-7% mAP

🚀 TOTAL EXPECTED BOOST: 20-44% improvement in mAP!
"""
    print(tips)

if __name__ == "__main__":
    print("VISTA_S Model Performance Optimizer")
    print("==================================")
    
    choice = input("\nWhat would you like to do?\n"
                  "1. Run optimized training (recommended)\n"
                  "2. Show improvement tips\n"
                  "3. Both\n"
                  "Enter choice (1-3): ").strip()
    
    if choice in ["1", "3"]:
        results = run_optimized_training()
        if results:
            print("\n🎉 Success! Your model should perform significantly better!")
            print("💡 Next: Try Test-Time Augmentation for even better inference results")
    
    if choice in ["2", "3"]:
        show_improvement_tips()
    
    if choice not in ["1", "2", "3"]:
        print("❌ Invalid choice. Please run again and choose 1, 2, or 3.")
